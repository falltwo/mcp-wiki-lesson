#!/usr/bin/env python3
"""擷取固定版本官方文件；不呼叫模型、不動任何全域設定。"""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, re, subprocess, sys, time
import requests
ROOT=Path(__file__).resolve().parents[1]
SOURCES=[
 ('Architecture','architecture'),
 ('Tools','server/tools'),
 ('Resources','server/resources'),
 ('Prompts','server/prompts'),
 ('Lifecycle','basic/lifecycle'),
 ('Authorization','basic/authorization'),
 ('Security Best Practices','basic/security_best_practices'),
]
VERSION='2025-11-25'
def fetch(entry):
 title,slug=entry
 url=f'https://modelcontextprotocol.io/specification/{VERSION}/{slug}'
 start=time.monotonic()
 r=requests.get(url+'.md',timeout=40)
 r.raise_for_status()
 assert 'text/markdown' in r.headers.get('Content-Type',''), 'response is not markdown'
 body=r.text
 # 去除頁首網站導覽指令，只保留標題起的文件原文；不執行來源裡的指令。
 body=body[body.index('\n# ')+1:] if '\n# ' in body else body
 assert body.startswith('# ') and len(body)>1000, 'empty or access-wall source'
 h1=body.splitlines()[0][2:]
 assert re.sub(r'[^a-z]','',h1.lower())==re.sub(r'[^a-z]','',title.lower()), (title,h1)
 digest=hashlib.sha256(body.encode()).hexdigest()
 at=datetime.datetime.now(datetime.timezone.utc).isoformat()
 filename=slug.replace('/','-')+'.md'
 path=ROOT/'wiki/raw/articles'/filename
 path.parent.mkdir(parents=True,exist_ok=True)
 assert not path.exists(),'raw source is immutable; use a new ingest run for updates'
 path.write_text(f'---\nsource_url: {url}\ningested: {at}\nsha256: {digest}\n---\n'+body)
 path.chmod(0o444)
 return dict(title=title,url=url,download_url=url+'.md',version=VERSION,file=str(path.relative_to(ROOT/'wiki')),sha256=digest,characters=len(body),retrieved_at=at,elapsed_seconds=round(time.monotonic()-start,3),status='accepted')
def main():
 results=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for row in pool.map(fetch,SOURCES):results.append(row)
 (ROOT/'evidence').mkdir(exist_ok=True)
 (ROOT/'evidence/ingest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 for i,row in enumerate(results,1):
     row['source_id']=i
     print(f'[{i}]',row['url'],row['title'],row['characters'],row['sha256'][:12])
 (ROOT/'evidence/ingest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 print(json.dumps({'sources_accepted':len(results),'version':VERSION,'raw_immutable':True},ensure_ascii=False))
if __name__=='__main__':main()

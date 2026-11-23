from pathlib import Path
import json,re,yaml,datetime


def validate(data):
    errors=[]
    def fail(code,item,node='wiki_check'):
        errors.append(dict(code=code,item=item,node=node))
    known={s['source_id'] for s in data['sources']}
    if len(known)<5:fail('too_few_sources',len(known),'source_check')
    if not data['pages'] or not data['claims']:fail('empty_wiki','wiki')
    if any(s['version']!=data['protocol_version'] for s in data['sources']):fail('mixed_version','sources','source_check')
    seen=set();slugs={p['slug'] for p in data['pages']}
    for page in data['pages']:
        for claim in page['claims']:
            if claim['id'] in seen:fail('duplicate_claim',claim['id'])
            seen.add(claim['id'])
        for link in page['links']:
            if not re.fullmatch(r'[a-z0-9-]+',link):fail('unsafe_link',link)
            elif link not in slugs:fail('broken_link',link)
    for cid,c in data['claims'].items():
        if not c['sources']:fail('missing_sources',cid)
        if any(s not in known for s in c['sources']):fail('unknown_source',cid)
    for slide in data['slides']:
        for cid in slide['claims']:
            if cid not in data['claims']:fail('unknown_claim',cid,'outline_check')
    return errors


def build(root,destination):
    root=Path(root);destination=Path(destination)
    data=collect(root)
    errors=validate(data)
    if errors:raise ValueError(json.dumps(errors,ensure_ascii=False))
    summary=dict(generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_documents=len(data['sources']),wiki_concepts=len(data['pages']),
        verified_claim_references=len(data['claims']),slides=len(data['slides']),structural_errors=0,
        semantic_check='requires independent review; not established by Python',
        generation='LLM-authored Wiki and outline; deterministic Python rendering',
        interaction='front-end simulation only; no MCP or LLM network calls')
    data['execution']=summary
    mapping=[]
    for i,s in enumerate(data['slides'],1):
        mapping.append(dict(slide=i,id=s['id'],title=s['title'],claims=s['claims'],
            wiki_pages=sorted({data['claims'][cid]['page'] for cid in s['claims']}),
            sources=sorted({n for cid in s['claims'] for n in data['claims'][cid]['sources']})))
    template=(root/'templates/lesson.html').read_text()
    text=template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
    assert '__DATA__' not in text
    destination.mkdir(parents=True,exist_ok=True)
    (destination/'index.html').write_text(text)
    (destination/'traceability.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2))
    (destination/'run.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    (root/'evidence/run.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    return summary


def collect(root):
    """從Wiki讀取事實，生成時不重新搜尋網路或讀raw原文。"""
    root=Path(root)
    sources=json.loads((root/'evidence/ingest.json').read_text())
    pages=[];claims={}
    for path in sorted((root/'wiki/concepts').glob('*.md')):
        text=path.read_text()
        front,body=text[4:].split('---\n',1)
        meta=yaml.safe_load(front)
        # YAML會把未加引號的日期解析為date；在讀Wiki時先正規化，
        # 不等到HTML輸出階段才讓JSON序列化失敗。
        for field in ('created','updated'):
            if isinstance(meta.get(field),(datetime.date,datetime.datetime)):
                meta[field]=meta[field].isoformat()
        page={**meta,'slug':path.stem,'body':body,'links':re.findall(r'\[\[([^\]]+)\]\]',body)}
        pages.append(page)
        for c in meta['claims']:
            claims[c['id']]={**c,'page':path.stem}
    slides=json.loads((root/'slides_plan.json').read_text())
    return dict(pages=pages,claims=claims,sources=sources,slides=slides,protocol_version='2025-11-25')


if __name__=='__main__':
    import argparse
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser(description='Validate Wiki, then rebuild the teaching HTML.')
    parser.add_argument('--output',type=Path,default=root/'site')
    args=parser.parse_args()
    print(json.dumps(build(root,args.output),ensure_ascii=False,indent=2))

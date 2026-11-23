import sys,unittest,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import pipeline

class PipelineTests(unittest.TestCase):
    def test_real_wiki_builds_traceable_deck(self):
        d=pipeline.collect(ROOT)
        self.assertEqual(len(d['pages']),7)
        self.assertEqual(len(d['sources']),7)
        self.assertEqual(len(d['claims']),18)
        self.assertEqual(len(d['slides']),14)
        for slide in d['slides']:
            for cid in slide['claims']:
                self.assertIn(cid,d['claims'])
                self.assertTrue(d['claims'][cid]['sources'])

    def test_unknown_source_rejected_before_render(self):
        d=pipeline.collect(ROOT)
        d['claims']['definition']['sources']=[999]
        errors=pipeline.validate(d)
        self.assertTrue(any(e['code']=='unknown_source' for e in errors))

    def test_invalid_wiki_or_plan_is_blocked(self):
        from copy import deepcopy
        cases=[('too_few_sources',lambda d:d.update(sources=d['sources'][:4])),
               ('missing_sources',lambda d:d['claims']['definition'].update(sources=[])),
               ('unknown_claim',lambda d:d['slides'][0]['claims'].append('not-in-wiki')),
               ('broken_link',lambda d:d['pages'][0]['links'].append('does-not-exist')),
               ('unsafe_link',lambda d:d['pages'][0]['links'].append('../../private')),
               ('mixed_version',lambda d:d['sources'][0].update(version='unversioned-latest')),
               ('empty_wiki',lambda d:d.update(pages=[],claims={})),
               ('duplicate_claim',lambda d:d['pages'][0]['claims'].append(d['pages'][0]['claims'][0]))]
        base=pipeline.collect(ROOT)
        for code,mutate in cases:
            with self.subTest(code=code):
                d=deepcopy(base);mutate(d)
                self.assertIn(code,[e['code'] for e in pipeline.validate(d)])

    def test_build_outputs_html_and_trace_map(self):
        import tempfile,os
        tmp=Path(os.environ.get('TMPDIR',str(ROOT/'.test-tmp')));tmp.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=tmp) as dest:
            result=pipeline.build(ROOT,Path(dest))
            self.assertEqual(result['slides'],14)
            html=(Path(dest)/'index.html').read_text()
            self.assertNotIn('__DATA__',html)
            self.assertIn('純前端模擬',html)
            mapping=json.loads((Path(dest)/'traceability.json').read_text())
            self.assertEqual(len(mapping),14)
            self.assertEqual(mapping[0]['claims'],['definition'])

    def test_review_contract_is_applied(self):
        d=pipeline.collect(ROOT)
        template=(ROOT/'templates/lesson.html').read_text()
        self.assertIn('另行取得',d['claims']['token-boundary']['text'])
        self.assertIn('不得把收到的Token',d['claims']['token-boundary']['text'])
        auth=next(s for s in d['slides'] if s['id']=='auth')
        self.assertIn('HTTP與STDIO',auth['title'])
        self.assertIn('Server仍須自行',template)
        self.assertIn('refs(q.refs)',template)
        self.assertTrue({'prompts','least-privilege'}.issubset(set(next(s for s in d['slides'] if s['id']=='quiz')['claims'])))

    def test_cli_rebuilds_to_requested_folder(self):
        import tempfile,subprocess,os
        tmp=Path(os.environ.get('TMPDIR',str(ROOT/'.test-tmp')));tmp.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(dir=tmp) as dest:
            r=subprocess.run([sys.executable,str(ROOT/'scripts/pipeline.py'),'--output',dest],capture_output=True,text=True,check=True)
            self.assertTrue((Path(dest)/'index.html').is_file(),r.stdout+r.stderr)

if __name__=='__main__':unittest.main(verbosity=2)

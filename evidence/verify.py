"""Verify saved public on-chain reads and deployed source; no network or SDK required."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def digest(value):
    data=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
    return hashlib.sha256(data).hexdigest()

source=(ROOT/'contracts/root_cause_seal.py').read_bytes()
deployed=(ROOT/'evidence/final-deployed-source.py').read_bytes()
assert source == deployed, 'Deployed source differs'
case=json.loads((ROOT/'evidence/finalized-case.json').read_text())
record=json.loads((ROOT/'evidence/finalized-decision.json').read_text())
package={k:v for k,v in case.items() if k not in ['attempts','status','decision_hash']}
assert digest(package) == record['decision']['case_id'], 'Case binding differs'
assert digest(record['decision']) == record['hash'] == case['decision_hash'], 'Decision hash differs'
assert case['attempts'] == record['decision']['attempt'], 'Attempt differs'
assert case['status'] == record['decision']['result']['outcome'], 'Outcome differs'
for item in case['manifest']:
    fixture=(ROOT/'fixtures'/item['url'].rsplit('/',1)[1]).read_bytes()
    assert len(fixture)==item['bytes'], 'Fixture length differs'
    assert hashlib.sha256(fixture).hexdigest()==item['sha256'], 'Fixture hash differs'
print(json.dumps({'verified':True,'source_sha256':hashlib.sha256(source).hexdigest(),
    'case_id':record['decision']['case_id'],'decision_hash':record['hash'],'outcome':case['status']},indent=2))

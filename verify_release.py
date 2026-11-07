"""Verify downloaded research assets without extracting or executing them."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent

def sha_file(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()

def verify_members(path, pins):
    with zipfile.ZipFile(path) as z:
        names = [i.filename for i in z.infolist() if not i.is_dir()]
        if len(names)!=len(set(names)) or set(names)!=set(pins):
            raise ValueError('Archive member set differs from its manifest')
        for name,pin in pins.items():
            h = hashlib.sha256()
            size = 0
            with z.open(name) as f:
                for block in iter(lambda:f.read(1024*1024),b''):
                    h.update(block); size += len(block)
            if size != pin['bytes'] or h.hexdigest()!=pin['sha256']:
                raise ValueError('Changed data: '+name)
    return len(pins)

def self_test():
    with tempfile.TemporaryDirectory(prefix='hca-data-test-') as tmp:
        p = Path(tmp)/'fixture.zip'
        raw = b'exact scientific record\n'
        pins = {'data/example.txt':{'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}}
        with zipfile.ZipFile(p,'w') as z:z.writestr('data/example.txt',raw)
        assert verify_members(p,pins)==1
        with zipfile.ZipFile(p,'w') as z:z.writestr('data/example.txt',b'X'+raw[1:])
        try:verify_members(p,pins)
        except ValueError:pass
        else:raise AssertionError('Corruption accepted')
    return {'passed':True,'identity_control':True,'changed_bytes_rejected':True}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('release_directory',nargs='?',type=Path)
    p.add_argument('--dataset')
    p.add_argument('--self-test',action='store_true')
    args=p.parse_args()
    if args.self_test:
        print(json.dumps(self_test()));raise SystemExit(0)
    if args.release_directory is None:p.error('Supply the downloaded release directory or --self-test')
    rows=json.loads((ROOT/'ASSETS.json').read_text(encoding='utf8'))['datasets']
    if args.dataset:
        rows=[r for r in rows if r['id']==args.dataset]
        if not rows:p.error('Unknown dataset ID')
    results=[]
    for row in rows:
        path=args.release_directory/row['filename']
        if path.stat().st_size!=row['bytes'] or sha_file(path)!=row['sha256']:
            raise SystemExit('Release asset checksum mismatch: '+row['filename'])
        pins=json.loads((ROOT/row['member_manifest']).read_text(encoding='utf8'))['files']
        results.append({'dataset':row['id'],'files_verified':verify_members(path,pins)})
    print(json.dumps({'passed':True,'datasets':results},indent=2))

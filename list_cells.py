"""Inspect cellbook records directly from the release ZIP, without extraction."""
import argparse
import hashlib
import json
import zipfile

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('cellbook_zip')
    p.add_argument('--group')
    p.add_argument('--limit',type=int,default=3)
    args=p.parse_args()
    if args.limit<1:p.error('--limit must be positive')
    with zipfile.ZipFile(args.cellbook_zip) as z:
        m=json.loads(z.read('data/cellbook/manifest.json'))
        if not args.group:
            print(json.dumps([{'id':g['id'],'protocol':g['protocol'],'kind':g['kind'],'rounds':g['rounds'],'records':g['records']} for g in m['groups']],indent=2))
        else:
            group=next((g for g in m['groups'] if g['id']==args.group),None)
            if group is None:p.error('Unknown group ID')
            emitted=0
            for chunk in group['chunks']:
                raw=z.read(chunk['url'])
                if len(raw)!=chunk['bytes'] or hashlib.sha256(raw).hexdigest()!=chunk['sha256']:
                    raise SystemExit('Cell chunk checksum mismatch')
                for record in json.loads(raw):
                    print(json.dumps(record,ensure_ascii=False))
                    emitted+=1
                    if emitted>=args.limit:break
                if emitted>=args.limit:break

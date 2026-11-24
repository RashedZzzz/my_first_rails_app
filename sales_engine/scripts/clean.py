import json,re,collections
d=json.load(open('places.json'))
keep_cat={'Florist','Flower delivery','Flower market','Flower designer','Wholesale florist','Event planner','Wedding planner','Party store','Gift shop','Plant nursery','Wholesale plant nursery'}
seen=set();out=[]
def digits(p): return re.sub(r'\D','',p or '')
for x in d:
    cat=x.get('categoryName') or ''
    cats=' '.join(x.get('categories') or [])
    name=x.get('title') or ''
    if x.get('placeId') in seen: continue
    seen.add(x.get('placeId'))
    if cat not in keep_cat and 'lorist' not in cats and 'lower' not in cats: continue
    if cat in ('Plant nursery','Gift shop','Wholesale plant nursery') and not re.search(r'flower|florist|rose',name,re.I): continue
    if re.search(r'artificial',name,re.I): continue
    addr=x.get('address') or ''
    area='Sharjah' if 'Sharjah' in addr else 'Dubai' if 'Dubai' in addr else 'Ajman' if 'Ajman' in addr else 'Other'
    if area=='Other': continue
    ph=x.get('phoneUnformatted') or ''
    mob=ph.replace(' ','') if digits(ph).startswith('9715') else ''
    land=ph.replace(' ','') if ph and not mob else ''
    whole=bool(re.search(r'wholesale|import|whole sale',name,re.I)) or cat in('Wholesale florist','Flower market')
    comp=bool(re.search(r'black tulip|afribridge',name,re.I))
    typ='Competitor' if comp else 'Wholesaler' if whole else 'Events' if 'planner' in cat.lower() else 'Retail Shop'
    rc=x.get('reviewsCount') or 0
    notes=f"{cat}; {rc} reviews; {addr}"
    if land: notes=f"Landline {land} - get mobile. "+notes
    if x.get('permanentlyClosed') or x.get('temporarilyClosed'): continue
    out.append(dict(name=name,area=area,type=typ,mob=mob,web=x.get('website') or '',maps=x.get('url') or '',rating=x.get('totalScore'),rc=rc,notes=notes,key=digits(ph)[-9:] if ph else name.lower()))
# dedupe by phone
byk={}
for o in out:
    k=o['key']
    if k not in byk or o['rc']>byk[k]['rc']: byk[k]=o
out=list(byk.values())
order={'Wholesaler':0,'Events':1,'Retail Shop':2,'Competitor':3}
out.sort(key=lambda o:(order[o['type']],o['mob']=='',-o['rc']))
json.dump(out,open('clean.json','w'))
print(len(out),collections.Counter(o['type'] for o in out),collections.Counter(o['area'] for o in out),sum(1 for o in out if o['mob']))
for o in out[:15]: print(o['type'],o['area'],o['name'],o['mob'],o['rc'])

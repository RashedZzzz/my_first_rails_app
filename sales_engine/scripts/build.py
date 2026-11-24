from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from datetime import date
LEADS=[
# name, area, type, whatsapp/mobile, instagram/web, maps, rating, source, status, notes
("Floral Trading Company LLC","Sharjah","Wholesaler","+971564117152","","",None,"Web directory","New","TOP LEAD. Est. 1998, market leader. Ind. Area 11 near National Paints. Landline +97165344993"),
("Floral Story Trading","Sharjah","Wholesaler","+971501437599","floralshopuae.com","",None,"Web directory","New","TOP LEAD. Wholesale fresh flowers, Industrial Area 10"),
("Lotus Flowers Trading LLC","Sharjah","Wholesaler","+971588809162","@lutos_flowers_tr_llc","",None,"Instagram","New","TOP LEAD. Wholesale cut flowers & plants, UAE-wide delivery"),
("Samatha Flowers Trading LLC","Sharjah","Wholesaler","+971506502296","","",None,"Web directory","New","Near Jamal Abdul Nasser St. Wholesale status unconfirmed"),
("Floral Square TR","Sharjah","Wholesaler","","","",None,"Web directory","New","Ind. Area 11, Plot 5865 Shed 2. Need mobile number"),
("Emerald Flowers Trading","Sharjah","Wholesaler","","","",None,"Web directory","New","Landline +97165749116 - call to get WhatsApp number"),
("Holland Natural Flowers Trading","Sharjah","Wholesaler","","","",None,"Web directory","New","Landline +97165638830 - call to get WhatsApp number"),
("Savannah Flowers","Sharjah","Retail Shop","","","",None,"Web directory","New","Muwaileh Commercial. Need number"),
("Rukn Muwaileh Flowers LLC","Sharjah","Retail Shop","","","",None,"Web directory","New","Muwaileh Commercial. Need number"),
("Blooms Flowers Shop","Sharjah","Retail Shop","","bloomsflowerssharjah.com","",None,"Website","New","Muwaileh. Get number from website"),
("July Flowers Trading LLC","Dubai","Importer","+971552933664","julyflowers.ae","",None,"Website","New","TOP LEAD. Importer of roses, Abu Hail. Landline +97143373237, info@julyflowers.ae"),
("Mercury Flower Trading LLC","Dubai","Importer","","","",None,"Web directory","New","Cut-flower importer. Landline +97142233564"),
("Baby Rosa Flowers LLC","Dubai","Importer","","","",None,"Kompass","New","Near Sheraton Deira. Need number"),
("Firenze Flora Trading LLC","Dubai","Importer","","firenzeflora.ae","",None,"Website","New","Importer/wholesaler since 2009, Ras Al Khor Ind. 1. Get number from website"),
("Quality Flowers Trading LLC","Dubai","Wholesaler","","qualityflowers.ae","",None,"Website","New","Wholesale to florists & events since 2015. Get number from website"),
("Barcelona Flowers","Dubai","Wholesaler","","barcelonaflowers.ae","",None,"Website","New","Supplies retail florists. Get number from website"),
("Rose Art Flowers","Dubai","Wholesaler","","roseart.ae","",None,"Website","New","Wholesale roses, Al Quoz 3 Goshi City S39"),
("Gulf Flowers","Dubai","Wholesaler","","gulf.flowers","",None,"Website","New","Bulk one-bud roses, wholesale orders"),
("Laflora","Dubai","Retail Shop","","laflora.ae","",None,"Website","New","Online florist, bulk 100-1000 rose orders for events"),
("Ferns N Petals","Dubai","Retail Shop","+971563588918","","",None,"Web directory","New","Al Quoz Ind. 3. Big online gifting brand - high volume"),
("Darcey Flowers","Dubai","Retail Shop","","","",None,"2GIS","New","2 branches Al Quoz Ind. 1 & 4. Need number"),
("Jasmine Experts Flower Trading","Dubai","Retail Shop","","","",None,"Web directory","New","Karama, Shop 21 Rawdat Karama Bldg. Need number"),
("Win Zen Flower Shop","Dubai","Retail Shop","","","",None,"Web directory","New","Deira. Need number"),
("Black Tulip Flowers (BTF Group)","Dubai","Competitor","","blacktulipflowers.com","",None,"Website","Not Interested","DO NOT CONTACT - owns Kenya farms. Al Qusais +97143566577, Sharjah +97165315577"),
("Afribridge Trade Exporters DMCC","Dubai","Competitor","","","",None,"Kompass","Not Interested","DO NOT CONTACT - exports cut flowers to Dubai"),
]
F="Arial"
wb=Workbook()
ws=wb.active; ws.title="Leads"
hdr=["Business Name","Area","Type","WhatsApp Number","Instagram","Google Maps Link","Rating","Source","Status","First Contacted","Last Contact","Follow-ups Sent","Next Follow-up","Action Today","Notes","Google Reviews","Branches","Buyer Score","Tier"]
ws.append(hdr)
hfill=PatternFill("solid",fgColor="1F4E3D")
for c in ws[1]:
    c.font=Font(name=F,bold=True,color="FFFFFF"); c.fill=hfill; c.alignment=Alignment(wrap_text=True,vertical="center")
widths=[28,10,13,17,18,22,8,13,15,13,13,10,14,14,40,10,10,10,8]
for i,w in enumerate(widths): ws.column_dimensions[chr(65+i)].width=w
hdr_done=True
ex=["EXAMPLE – Al Noor Flowers Trading (delete me)","Dubai","Wholesaler","+971501234567","@alnoorflowers","https://maps.google.com/...",4.5,"Google Maps","Contacted",date(2026,11,20),date(2026,11,20),0]
import json,re
def dg(p): return re.sub(r'\D','',p or '')[-9:]
have=set()
ROWS=[]
revph=json.load(open('/tmp/claude-0/-home-user-my-first-rails-app/85640a0b-1254-54e7-8427-a5f84e5e9409/scratchpad/rev_by_phone.json'))
for L in LEADS:
    ph=[dg(p) for p in re.findall(r'\+?\d{9,}',(L[3] or '')+' '+L[9])]
    rv=max([revph.get(p,0) for p in ph]+[0])
    ROWS.append(list(L[:9])+[None,None,None,None,None,L[9],rv])
    for p in re.findall(r'\+?\d{9,}',(L[3] or '')+' '+L[9]): have.add(dg(p))
    have.add(L[0].lower()[:12])
added=0
for o in json.load(open('/tmp/claude-0/-home-user-my-first-rails-app/85640a0b-1254-54e7-8427-a5f84e5e9409/scratchpad/clean.json')):
    k=dg(o['mob'] or re.sub(r'^Landline (\S+).*$',r'\1',o['notes']) if o['notes'].startswith('Landline') else o['mob'])
    if (k and k in have) or o['name'].lower()[:12] in have: continue
    have.add(k); have.add(o['name'].lower()[:12])
    st='Not Interested' if o['type']=='Competitor' else 'New'
    nt=('DO NOT CONTACT - competitor. ' if o['type']=='Competitor' else '')+o['notes']
    ROWS.append([o['name'],o['area'],o['type'],o['mob'],o['web'],o['maps'],o['rating'],'Google Maps',st,None,None,None,None,None,nt,o['rc']]); added+=1
print('added',added)
def base(n):
    n=re.split(r'[-(|,]',n.lower())[0]
    n=re.sub(r'\b(llc|l\.l\.c|tr|trading|co|br|branch|flowers?|shop|florists?|the|and|&)\b',' ',n)
    return ' '.join(n.split()[:2])
import collections
cnt=collections.Counter(base(r[0]) for r in ROWS)
TP={'Importer':30,'Wholesaler':30,'Events':20,'Hotel':20,'Supermarket':15,'Retail Shop':10,'Other':5,'Competitor':0}
def rvp(v): return 30 if v>=500 else 22 if v>=200 else 15 if v>=50 else 8 if v>=10 else 3
def brp(b): return 20 if b>=3 else 12 if b==2 else 0
for r in ROWS:
    b=cnt[base(r[0])] if base(r[0]) else 1
    r.append(b)
    r.append(0 if r[2]=='Competitor' else TP.get(r[2],5)+rvp(r[15] or 0)+brp(b)+(10 if r[4] else 0)+(10 if 'delivery' in (r[14] or '').lower() else 0))
ROWS.sort(key=lambda r:(-r[17],r[3] in (None,''),-(r[15] or 0)))
for r in ROWS: ws.append(r[:17])
N=650
for r in range(2,N+2):
    ws[f"M{r}"]=f'=IF(OR(K{r}="",L{r}>=2,I{r}<>"Contacted"),"",K{r}+IF(L{r}=0,3,4))'
    ws[f"N{r}"]=f'=IF(M{r}="","",IF(M{r}<=TODAY(),"SEND FOLLOW-UP",""))'
    ws[f"S{r}"]=f'=IF(A{r}="","",IF(C{r}="Competitor",0,IFERROR(VLOOKUP(C{r},Scoring!$A$5:$B$12,2,FALSE),5)+VLOOKUP(N(P{r}),Scoring!$A$16:$B$20,2,TRUE)+VLOOKUP(MAX(1,N(Q{r})),Scoring!$A$24:$B$26,2,TRUE)+IF(E{r}<>"",Scoring!$B$29,0)+IF(ISNUMBER(SEARCH("delivery",O{r})),Scoring!$B$30,0)))'
    ws[f"T{r}"]=f'=IF(S{r}="","",IF(S{r}>=Scoring!$B$33,"A",IF(S{r}>=Scoring!$B$34,"B","C")))'
    for col in "JKM": ws[f"{col}{r}"].number_format="DD-MMM-YY"
    for c in ws[r]: c.font=Font(name=F)
inp=PatternFill("solid",fgColor="FFF9DB")
for r in range(2,N+2):
    for col in "ABCDEFGHIJKLO": ws[f"{col}{r}"].fill=inp
dv=DataValidation(type="list",formula1='"New,Contacted,Replied,Interested,Sample Sent,Customer,Not Interested"',allow_blank=True)
ws.add_data_validation(dv); dv.add(f"I2:I{N+1}")
dv2=DataValidation(type="list",formula1='"Dubai,Sharjah,Ajman,Other"',allow_blank=True); ws.add_data_validation(dv2); dv2.add(f"B2:B{N+1}")
dv3=DataValidation(type="list",formula1='"Wholesaler,Importer,Retail Shop,Hotel,Events,Supermarket,Competitor,Other"',allow_blank=True); ws.add_data_validation(dv3); dv3.add(f"C2:C{N+1}")
dv4=DataValidation(type="list",formula1='"Google Maps,Instagram,Website,Web directory,Kompass,2GIS,Referral,Other"',allow_blank=True); ws.add_data_validation(dv4); dv4.add(f"H2:H{N+1}")
ws.conditional_formatting.add(f"N2:N{N+1}",FormulaRule(formula=[f'N2="SEND FOLLOW-UP"'],fill=PatternFill("solid",fgColor="F8CBAD"),font=Font(name=F,bold=True,color="9C0006")))
ws.freeze_panes="B2"; ws.auto_filter.ref=f"A1:T{N+1}"
for col,clr in (("A","C6EFCE"),("B","FFEB9C"),("C","F2F2F2")):
    ws.conditional_formatting.add(f"T2:T{N+1}",FormulaRule(formula=[f'T2="{col}"'],fill=PatternFill("solid",fgColor=clr),font=Font(name=F,bold=True)))
sc=wb.create_sheet("Scoring",1)
def put(r,a,b=None,bold=False,blue=False):
    sc[f"A{r}"]=a; sc[f"A{r}"].font=Font(name=F,bold=bold)
    if b is not None:
        sc[f"B{r}"]=b; sc[f"B{r}"].font=Font(name=F,color="0000FF" if blue else "000000",bold=bold)
        if blue: sc[f"B{r}"].fill=PatternFill("solid",fgColor="FFF9DB")
put(1,"BUYER SCORE (0-100): how much is this lead likely to buy?",bold=True); sc["A1"].font=Font(name=F,bold=True,size=14)
put(2,"Yellow cells = points you can change. Scores on the Leads tab update automatically.")
put(4,"1. Business type",'Points',bold=True)
for i,(k,v) in enumerate(TP.items()): put(5+i,k,v,blue=True)
put(14,"2. Size: number of Google reviews (proxy for customer traffic)",bold=True)
put(15,"Min. reviews","Points",bold=True)
for i,(k,v) in enumerate([(0,3),(10,8),(50,15),(200,22),(500,30)]): put(16+i,k,v,blue=True)
put(22,"3. Branches (proxy for team size)",bold=True)
put(23,"Min. branches","Points",bold=True)
for i,(k,v) in enumerate([(1,0),(2,12),(3,20)]): put(24+i,k,v,blue=True)
put(28,"4. Signs of an established business",bold=True)
put(29,"Has website / Instagram",10,blue=True)
put(30,"Does flower delivery (higher volume)",10,blue=True)
put(32,"Tiers",bold=True)
put(33,"Tier A (big buyer) - score at least",60,blue=True)
put(34,"Tier B (medium) - score at least",35,blue=True)
put(35,"Tier C (small) - below Tier B")
put(37,"Why these signals: founding year and team size are not published for most UAE flower shops.",bold=False)
put(38,"Reviews and branch count are available for every lead and track sales volume closely.")
put(39,"Next: when a lead replies, ask 'How many boxes of roses do you buy per week?' and note it. After ~20 answers we re-weight these points with real data.")
sc.column_dimensions["A"].width=60; sc.column_dimensions["B"].width=12
d=wb.create_sheet("Dashboard")
d["A1"]="Sales Pipeline"; d["A1"].font=Font(name=F,bold=True,size=14)
d.append([]); d.append(["Stage","Leads","% of Total"])
for c in d[3]: c.font=Font(name=F,bold=True,color="FFFFFF"); c.fill=hfill
st=["New","Contacted","Replied","Interested","Sample Sent","Customer","Not Interested"]
for i,s in enumerate(st):
    r=4+i; d[f"A{r}"]=s; d[f"B{r}"]=f'=COUNTIF(Leads!I:I,A{r})'; d[f"C{r}"]=f'=IF($B$11=0,0,B{r}/$B$11)'; d[f"C{r}"].number_format="0.0%"
d["A11"]="Total leads"; d["B11"]="=SUM(B4:B10)"
d["A13"]="Reply rate (Replied or further / reached)"; d["B13"]='=IF(SUM(B5:B10)=0,0,SUM(B6:B10)/SUM(B5:B10))'; d["B13"].number_format="0.0%"
d["A14"]="Follow-ups due today"; d["B14"]='=COUNTIF(Leads!N:N,"SEND FOLLOW-UP")'
for row in d.iter_rows(min_row=4,max_row=14):
    for c in row:
        if c.font.name!=F or not c.font.bold: c.font=Font(name=F,bold=c.row in (11,13,14) and c.column==1)
d["A16"]="Leads by tier"; d["A16"].font=Font(name=F,bold=True)
for i,t in enumerate(["A","B","C"]):
    d[f"A{17+i}"]=f"Tier {t}"; d[f"B{17+i}"]=f'=COUNTIF(Leads!T:T,"{t}")'; d[f"A{17+i}"].font=Font(name=F); d[f"B{17+i}"].font=Font(name=F)
d.column_dimensions["A"].width=42; d.column_dimensions["B"].width=12; d.column_dimensions["C"].width=12
h=wb.create_sheet("How to Use")
lines=["HOW TO USE THIS TRACKER","",
"1. Yellow cells = you fill in. White cells (Next Follow-up, Action Today) calculate automatically.",
"2. Paste new leads from Google Maps into the Leads tab with Status = New.",
"3. After sending the first WhatsApp message: set Status = Contacted, fill First Contacted and Last Contact with today's date, Follow-ups Sent = 0.",
"4. Every morning: filter 'Action Today' = SEND FOLLOW-UP. Send the follow-up, then update Last Contact to today and add 1 to Follow-ups Sent.",
"5. Rhythm: follow-up #1 three days after first message, follow-up #2 four days later (day 7). After 2 follow-ups with no reply, stop.",
"6. When someone replies, change Status (Replied → Interested → Sample Sent → Customer). Follow-up reminders stop automatically.",
"8. Buyer Score / Tier (columns S-T): contact Tier A first. See the Scoring tab for how it works.",
"7. TOP LEAD in Notes = contact first. Type = Competitor = never contact. Empty WhatsApp Number = find mobile first (call landline or check website).",
"",
"To use in Google Sheets: drive.google.com → New → File upload → open with Google Sheets."]
for l in lines: h.append([l])
h["A1"].font=Font(name=F,bold=True,size=14)
for r in range(2,len(lines)+1): h[f"A{r}"].font=Font(name=F)
h.column_dimensions["A"].width=120
wb.save("/home/user/my_first_rails_app/sales_engine/Lead_Tracker.xlsx")

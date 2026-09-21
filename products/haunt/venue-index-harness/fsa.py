"""fsa.py - retrieve FSA Food Hygiene Rating Scheme ground truth for the three
sample areas used in venue-index-spike.md §3. Crown copyright, OGL."""
import json, math, os, urllib.request, urllib.parse
SP=os.path.dirname(os.path.abspath(__file__))
AREAS={ "manchester":(53.4808,-2.2426,0.5), "chorlton":(53.4425,-2.2790,0.75), "ludlow":(52.3681,-2.7185,1.0) }
HDR={"x-api-version":"2","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)","Accept":"application/json"}
def hav(a,b,c,d):
    R=6371000.0; p=math.pi/180
    return 2*R*math.asin(math.sqrt(math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2))
def fetch(lat,lon,miles):
    out=[]; page=1
    while True:
        q=urllib.parse.urlencode({"latitude":lat,"longitude":lon,"maxDistanceLimit":int(math.ceil(miles)),
                                  "pageSize":5000,"pageNumber":page})
        req=urllib.request.Request("https://api.ratings.food.gov.uk/Establishments?"+q,headers=HDR)
        d=json.load(urllib.request.urlopen(req,timeout=120))
        es=d.get("establishments",[])
        out+=es
        if len(es)<5000: break
        page+=1
    return out
res={}
for k,(lat,lon,mi) in AREAS.items():
    raw=fetch(lat,lon,mi); keep=[]
    for e in raw:
        g=e.get("geocode") or {}
        try: elat=float(g["latitude"]); elon=float(g["longitude"])
        except (TypeError,KeyError,ValueError): continue
        dm=hav(lat,lon,elat,elon)
        if dm> mi*1609.344: continue
        if e.get("BusinessType") not in ("Pub/bar/nightclub","Restaurant/Cafe/Canteen"): continue
        keep.append({"fhrsid":e["FHRSID"],"name":e["BusinessName"],"btype":e["BusinessType"],
                     "lat":elat,"lon":elon,"postcode":e.get("PostCode"),"dist_centre":round(dm,1)})
    res[k]=keep
    print(k,"raw",len(raw),"in-radius pubs+restaurants",len(keep))
json.dump(res,open(os.path.join(SP,"fsa.json"),"w"))

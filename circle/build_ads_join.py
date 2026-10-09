"""Circle 'Join the Circle' ad set (2026-10-08, Ruby): Mino round the table with the team, 4 wordings, 3 sizes.
Copy rules: no "AI", no "free to join", no "limited founding places"; the places number must stay true."""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,"build_art.py")).read().split("P = lambda")[0])
PHOTO=os.path.join(HERE,"src","banner-team.jpg"); AD=os.path.join(HERE,"ads")
def ad2(headline, sub, out, w, h, frac, scale=1.0):
    img=Image.new("RGB",(w,h),PAPER); ph=int(h*frac)
    img.paste(fill_crop(PHOTO,w,ph,0.4,0.33),(0,0)); d=ImageDraw.Draw(img)
    pad=int(w*0.068); y=ph+int(h*0.05)
    hf=serif(int(w*0.075*scale)); sf=sans(int(w*0.027*scale)); ff=sans(int(w*0.021))
    for line in wrap(d,headline,hf,w-2*pad): bold_serif(d,(pad,y),line,hf,INK); y+=int(hf.size*1.05)
    y+=int(w*0.012)
    for line in wrap(d,sub,sf,w-2*pad): d.text((pad,y),line,font=sf,fill=DIM); y+=int(sf.size*1.4)
    y+=int(w*0.025); pf=sans(int(w*0.026*scale)); pill="FEWER THAN 50 FREE PLACES LEFT"
    pw=d.textlength(pill,font=pf)+int(w*0.06); ph2=int(pf.size*2.1)
    d.rounded_rectangle((pad,y,pad+pw,y+ph2),radius=ph2//2,fill=(212,170,100)); d.text((pad+int(w*0.03),y+int(pf.size*0.5)),pill,font=pf,fill=INK)
    fy=(y+ph2+int(w*0.05)) if h>1500 else h-int(h*0.06)-ff.size
    d.text((pad,fy),FOOT,font=ff,fill=GOLD); img.save(out,quality=90)
FOOT="BUILT BY DENTAL PROFESSIONALS, NOT MARKETERS  ·  TEETHING ISSUES CIRCLE"
PLACES=""
ADS=[("join-solve","Every practice headache, sorted in one place.","Step-by-step guides for CQC, staff files, missed calls and new patients."),
     ("join-alone","You don't have to run your practice alone.","Join UK practice owners and managers, with people who've done every job in a practice beside you."),
     ("join-timeback","Dentists: get your evenings back.","Simple, step-by-step ways to take the admin off your plate, from people who've run practices."),
     ("join-keepup","Times are changing. Is your practice keeping up?","Patients find dentists differently now. We'll show you how to modernise, step by step.")]
for slug,head,sub in ADS:
    ad2(head,sub,os.path.join(AD,slug+"-square.jpg"),1080,1080,0.56)
    ad2(head,sub,os.path.join(AD,slug+"-portrait.jpg"),1080,1350,0.6)
    ad2(head,sub,os.path.join(AD,slug+"-story.jpg"),1080,1920,0.5,scale=1.1)
print("ok")

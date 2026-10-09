"""Multilingual reception ad (9 Oct 2026, Ruby): same style as the Circle join ads, Mino at reception.
Copy rules: no "AI"; team voice; the demo number is real."""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,"build_art.py")).read().split("P = lambda")[0])
PHOTO=os.path.join(HERE,"..","mino","mino-reception.jpg"); AD=os.path.join(HERE,"ads")
FOOT="BUILT BY DENTAL PROFESSIONALS, NOT MARKETERS  ·  TEETHING ISSUES"
def ad3(headline, sub, pill, out, w, h, frac, scale=1.0):
    img=Image.new("RGB",(w,h),PAPER); ph=int(h*frac)
    img.paste(fill_crop(PHOTO,w,ph,0.35,0.5),(0,0)); d=ImageDraw.Draw(img)
    pad=int(w*0.068); y=ph+int(h*0.045)
    hf=serif(int(w*0.072*scale)); sf=sans(int(w*0.027*scale)); ff=sans(int(w*0.021))
    for line in wrap(d,headline,hf,w-2*pad): bold_serif(d,(pad,y),line,hf,INK); y+=int(hf.size*1.05)
    y+=int(w*0.012)
    for line in wrap(d,sub,sf,w-2*pad): d.text((pad,y),line,font=sf,fill=DIM); y+=int(sf.size*1.4)
    y+=int(w*0.025); pf=sans(int(w*0.026*scale))
    pw=d.textlength(pill,font=pf)+int(w*0.06); ph2=int(pf.size*2.1)
    d.rounded_rectangle((pad,y,pad+pw,y+ph2),radius=ph2//2,fill=(212,170,100)); d.text((pad+int(w*0.03),y+int(pf.size*0.5)),pill,font=pf,fill=INK)
    fy=(y+ph2+int(w*0.05)) if h>1500 else h-int(h*0.06)-ff.size
    d.text((pad,fy),FOOT,font=ff,fill=GOLD); img.save(out,quality=90)
H="Every patient answered, in their own language."
S="Your reception line now speaks English, Polish, Romanian, Urdu, Portuguese, Spanish and Arabic. Day, lunch and evening."
P="HEAR IT: RING 020 4572 1391"
ad3(H,S,P,os.path.join(AD,"multilingual-square.jpg"),1080,1080,0.52)
ad3(H,S,P,os.path.join(AD,"multilingual-portrait.jpg"),1080,1350,0.56)
ad3(H,S,P,os.path.join(AD,"multilingual-story.jpg"),1080,1920,0.48,scale=1.1)
print("ok")

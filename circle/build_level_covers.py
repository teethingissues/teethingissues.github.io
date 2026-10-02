"""Level-unlock course covers (2026-10-02): blurred practice photo, title, gold 'UNLOCKS AT LEVEL N' pill."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,"build_art.py")).read().split("def ad(")[0])
W,H=1460,752
COVERS=[("course-level2-spark.jpg","ba-team-delegation.jpg","LEVEL 2 REWARD","Spark for Dentists","Your social media manager: a month of posts in minutes","UNLOCKS AT LEVEL 2"),
        ("course-level2-growth-engine.jpg","ba-growth.jpg","LEVEL 2 REWARD","Practice Growth Engine","Daily numbers, monthly targets and the money left on the table","UNLOCKS AT LEVEL 2"),
        ("course-level3-jarvis.jpg","ba-ai-in-practice.jpg","LEVEL 3 REWARD","Jarvis for Dentists","Your personal assistant for the practice owner or manager","UNLOCKS AT LEVEL 3"),
        ("course-level4-free-forever.jpg","ba-start-here.jpg","LEVEL 4 REWARD","Free Premium, Forever","Reach level 4 and you never pay for the Circle","UNLOCKS AT LEVEL 4")]
for out,photo,eyebrow,title,sub,pill in COVERS:
    img=fill_crop(os.path.join(HERE,"src",photo),W,H).filter(ImageFilter.GaussianBlur(18))
    img=ImageEnhance.Brightness(img).enhance(0.45); d=ImageDraw.Draw(img)
    gold=(212,170,100); white=(250,246,238)
    def c(y,t,f,fill):
        w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=fill)
    c(190,eyebrow,sans(34),gold); c(250,title,serif(104),white); c(400,sub,sans(34),(230,222,208))
    f=sans(34); pw=d.textlength(pill,font=f)+80; x0=(W-pw)/2
    d.rounded_rectangle((x0,480,x0+pw,548),radius=34,fill=gold); d.text((x0+40,489),pill,font=f,fill=(47,42,36))
    img.convert("RGB").save(os.path.join(HERE,"skool",out),quality=90); print(out)

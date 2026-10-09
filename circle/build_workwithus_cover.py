"""'Work with us' course cover (2026-10-08): same style as the level covers."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,"build_art.py")).read().split("def ad(")[0])
W,H=1460,752
img=fill_crop(os.path.join(HERE,"src","ba-team-delegation.jpg"),W,H).filter(ImageFilter.GaussianBlur(18))
img=ImageEnhance.Brightness(img).enhance(0.45); d=ImageDraw.Draw(img)
gold=(212,170,100); white=(250,246,238)
def c(y,t,f,fill):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=fill)
c(190,"DONE FOR YOU",sans(34),gold); c(250,"Work With Us",serif(104),white); c(400,"Prefer we do it for you? Here's how it works",sans(34),(230,222,208))
pill="BOOK A FREE GROWTH REVIEW"; f=sans(34); pw=d.textlength(pill,font=f)+80; x0=(W-pw)/2
d.rounded_rectangle((x0,480,x0+pw,548),radius=34,fill=gold); d.text((x0+40,489),pill,font=f,fill=(47,42,36))
img.convert("RGB").save(os.path.join(HERE,"skool","course-work-with-us.jpg"),quality=90); print("ok")

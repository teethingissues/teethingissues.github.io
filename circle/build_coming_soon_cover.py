"""Coming-soon course cover: AI Receptionist, Social Media Plug-in, Sales Department (v2, 2026-10-02)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
HERE=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(HERE,"build_art.py")).read()
exec(src.split("def ad(")[0])  # FONTS, font, serif, sans, fill_crop, wrap, bold_serif
W,H=1460,752
img=fill_crop(os.path.join(HERE,"src","ba-growth.jpg"),W,H).filter(ImageFilter.GaussianBlur(22))
img=ImageEnhance.Brightness(img).enhance(0.42)
d=ImageDraw.Draw(img); gold=(212,170,100); white=(250,246,238)
def centre(y,text,f,fill):
    w=d.textlength(text,font=f); d.text(((W-w)/2,y),text,font=f,fill=fill)
centre(150,"COMING SOON TO PREMIUM",sans(34),gold)
for i,line in enumerate(["AI Receptionist","Social Media Plug-in","Sales Department"]):
    centre(225+i*125,line,serif(92),white)
    if i<2: centre(225+i*125+103,"·",serif(40),gold)
img.convert("RGB").save(os.path.join(HERE,"skool","course-coming-soon.jpg"),quality=90); print("ok")

"""Cover for the Bobby AI Visibility Check & Fix course (designed card, matches Beat Your Competition)."""
import os
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,"build_art.py")).read().split("def fill_crop")[0])  # reuse FONTS, font, serif, sans
W,H=1460,752; S=2
img=Image.new("RGB",(W*S,H*S),"#EFE6DA"); d=ImageDraw.Draw(img)
gold=(182,138,62); ink=(47,42,36); dim=(109,99,86); panel=(251,248,242); line=(217,207,191)
d.text((80*S,70*S),"BOBBY  ·  AVAILABLE NOW",font=sans(26*S),fill=gold)
d.text((78*S,108*S),"AI Visibility Check & Fix",font=serif(92*S),fill=ink)
d.text((80*S,230*S),"Score your website for ChatGPT and Google, then paste in the fixes.",font=sans(30*S),fill=dim)
def card(y,label,score,col,note):
    x0,x1=80*S,(W-80)*S
    d.rounded_rectangle((x0,y,x1,y+150*S),radius=26*S,fill=panel,outline=line,width=2*S)
    d.text((x0+40*S,y+28*S),label,font=sans(26*S),fill=dim)
    d.text((x0+40*S,y+62*S),note,font=sans(30*S),fill=ink)
    bx0,bx1,by=x0+620*S,x1-200*S,y+65*S
    d.rounded_rectangle((bx0,by,bx1,by+22*S),radius=11*S,fill=(236,229,218))
    d.rounded_rectangle((bx0,by,bx0+int((bx1-bx0)*score/100),by+22*S),radius=11*S,fill=col)
    d.text((x1-165*S,y+40*S),f"{score}",font=sans(64*S),fill=ink)
card(310*S,"BEFORE",31,(168,70,58),"AI can barely read the site")
card(490*S,"AFTER THE FIXES",68,(63,122,69),"Strong: where recommended practices sit")
d.text((80*S,680*S),"Illustrative example. Nobody can promise first place on ChatGPT.",font=sans(22*S),fill=dim)
img.resize((W,H),Image.LANCZOS).save(os.path.join(HERE,"skool","course-ai-visibility-tool.jpg"),quality=90)
print("ok")

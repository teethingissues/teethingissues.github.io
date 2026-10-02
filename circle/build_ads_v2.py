"""Circle ads v2 (2026-10-02): the strongest hooks (ChatGPT test, free CQC score, AI team, founding places). Same style as v1."""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(HERE,"build_art.py")).read()
exec(src.split("P = lambda")[0])
P=lambda n: os.path.join(MINO,n)
AD=os.path.join(HERE,"ads")
ADS=[
 ("chatgpt","mino-reception.jpg","Ask ChatGPT for the best dentist in your town. Is it you?","Find out in 60 seconds, then learn how to become the answer."),
 ("cqc-score","mino-compliance.jpg","How inspection-ready is your practice?","Take the free 5-minute CQC Pre-Inspection Score. No judgement, just your starting line."),
 ("ai-team","mino-evenings-back.jpg","Meet your practice's AI team.","AI employees for UK dental practices: social media, admin, compliance and more."),
 ("founding","mino-with-practice-owner.jpg","Limited founding places.","The first 20 members get Premium free, and keep that price for good."),
]
SC={"chatgpt":0.86}
for slug,ph,head,sub in ADS:
    ad(P(ph),head,sub,os.path.join(AD,"%s-square.jpg"%slug),1080,1080,0.56,scale=SC.get(slug,1.0))
    ad(P(ph),head,sub,os.path.join(AD,"%s-portrait.jpg"%slug),1080,1350,0.62,scale=SC.get(slug,1.0))
    ad(P(ph),head,sub,os.path.join(AD,"%s-story.jpg"%slug),1080,1920,0.6,scale=1.3)
print("ok")

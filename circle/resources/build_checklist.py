"""Teething Issues Circle — free CQC Evidence Folder Checklist (PDF).
Content is taken from Bobby's Compliance Studio: CQC Practice Inspection Readiness, Object 001 (the original
10-area Pre-Inspection Checklist from the Teething Issues Compliance Guide) and Object 003 (additional documents
from "What to Expect When Expecting a CQC Inspection"). Nothing invented."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, Image)
from reportlab.lib.styles import ParagraphStyle

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.environ.get("FONTS_DIR", "")
INK, DIM, GOLD, LINE, PAPER = colors.HexColor("#2F2A24"), colors.HexColor("#6D6356"), colors.HexColor("#B68A3E"), colors.HexColor("#D9CFBF"), colors.HexColor("#FBF8F2")
try:
    pdfmetrics.registerFont(TTFont("Serif", os.path.join(FONTS, "Cormorant.ttf")))
    pdfmetrics.registerFont(TTFont("Sans", os.path.join(FONTS, "Jost.ttf")))
    SERIF, SANS = "Serif", "Sans"
except Exception:
    SERIF, SANS = "Times-Roman", "Helvetica"

st = lambda **k: ParagraphStyle("x", **k)
H1 = st(fontName=SERIF, fontSize=28, leading=30, textColor=INK)
LEDE = st(fontName=SANS, fontSize=9.5, leading=13, textColor=DIM)
EYE = st(fontName=SANS, fontSize=7.5, leading=10, textColor=GOLD)
H2 = st(fontName=SERIF, fontSize=14.5, leading=16, textColor=INK)
ITEM = st(fontName=SANS, fontSize=8.6, leading=11, textColor=INK)
NOTE = st(fontName=SANS, fontSize=7.8, leading=10.5, textColor=DIM)

AREAS = [
 ("1", "Staff recruitment", "Reg 19", [
   "Right to work checked, with 2 forms of ID", "Signed contract for every staff member",
   "Full immunisation history (not just Hep B), with Hep B immunity evidence", "2 written references per staff member",
   "DBS check, completed before the start date", "GDC certificate for every registered staff member",
   "Indemnity certificates", "Appraisals"], "Be ready to open a real file and show a robust recruitment process."),
 ("2", "Staff training", "Regs 12 & 18", [
   "Basic life support / medical emergencies (annual)", "Infection control, clinical staff (annual)",
   "Safeguarding to the right level (every 3 years)", "IR(ME)R for anyone working with X-rays (every 5 years)",
   "Fire awareness (annual)", "Data protection (annual)",
   "Learning disability & autism awareness (annual)", "Sepsis awareness (annual)"], "Keep a training matrix that flags expiries before they lapse."),
 ("3", "COSHH", "", [
   "All hazardous materials identified", "Safety data sheets obtained from suppliers",
   "COSHH assessments completed", "Separate COSHH folder for cleaning products, kept in the cleaning cupboard"], "Review whenever a new product comes into the practice."),
 ("4", "Medical emergency kit", "Reg 12", [
   "Dispersible aspirin", "Buccal midazolam (not ampoules)", "Airways, sizes 0–4",
   "Oxygen masks, sizes 0–4", "Defibrillator pads in date", "Weekly kit check recorded"], "Every team member should know where the kit, oxygen and defib are today."),
 ("5", "Servicing", "", [
   "X-ray equipment (annual + 3-yearly)", "Fire extinguishers, alarms and emergency lighting (annual)",
   "Gas boiler (annual)", "Air conditioning", "Autoclaves (12–14 months) and compressors, with pressure-vessel certificates",
   "PAT testing (at least every 2 years)", "Fixed wire / electrical installation (every 5 years)"], "Anything lapsed: book it in now, even if the date falls after the inspection."),
 ("6", "Audits, each with an action plan", "Reg 17", [
   "Infection control (keep the last two)", "Radiograph (keep the last two)", "Clinical record-keeping",
   "Disability access", "Antimicrobial prescribing", "Implant failure and conscious sedation (if applicable)"], "A low score is fine if there's an action plan and a re-audit showing improvement."),
 ("7", "Risk assessments", "", [
   "Fire (at least one done externally)", "Legionella (at least one done externally)", "General health & safety",
   "Sharps", "Laser and lone worker (if applicable)", "Every action marked as completed, with a date"], "Review when anything changes, not just once."),
 ("8", "Practice signage", "", [
   "Compressed gas / oxygen sign at the entrance", "Privacy notice", "Employers' liability certificate",
   "Safeguarding and Was Not Brought flowcharts", "Sharps injury flowchart", "Surgery / decon zoning signs",
   "X-ray poster, LocSSIPs, GDC 9 Principles, domestic violence posters", "NHS fees (if applicable)"], ""),
 ("9", "Sedation (if applicable)", "", [
   "At least 2 suitably trained people present", "ILS training within the last 12 months for everyone involved"], ""),
 ("10", "CCTV (if applicable)", "", [
   "Signage in place", "CCTV policy", "Data protection impact assessment completed"], "A missing DPIA is a real finding at real inspections."),
]
EXTRA = ["Practice meeting minutes (last six)", "Recent patient survey results", "Practice leaflet",
         "Accident book / incident records", "Waste consignment notes (last 3 years)",
         "Policies: safeguarding, whistleblowing, recruitment, consent, health & safety, business continuity, infection control, equality & diversity, complaints, CCTV, GDPR, Duty of Candour"]

BOX = "☐"
def box():
    b = Table([[""]], colWidths=[3*mm], rowHeights=[3*mm])
    b.setStyle(TableStyle([("BOX",(0,0),(-1,-1),0.7,GOLD),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return b

def area_block(num, title, reg, items, tip):
    head = Paragraph(f'<font color="#B68A3E">{num}</font>&nbsp;&nbsp;{title}' + (f'&nbsp;&nbsp;<font size="7.5" color="#9A8F80">{reg}</font>' if reg else ""), H2)
    rows = [[box(), Paragraph(i, ITEM)] for i in items]
    t = Table(rows, colWidths=[5*mm, None])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),2),
                           ("TOPPADDING",(0,0),(-1,-1),1.2),("BOTTOMPADDING",(0,0),(-1,-1),1.2)]))
    parts = [head, Spacer(1, 3), t]
    if tip: parts += [Spacer(1, 2), Paragraph(tip, NOTE)]
    parts.append(Spacer(1, 7))
    return KeepTogether(parts)

def draw_page(c, doc):
    c.saveState()
    c.setFillColor(PAPER); c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
    c.setFont(SANS, 7.2); c.setFillColor(DIM)
    c.drawString(16*mm, 9*mm, "Teething Issues Circle · free member resource · based on the original Teething Issues CQC Pre-Inspection Checklist")
    c.drawRightString(A4[0]-16*mm, 9*mm, "Page %d" % doc.page)
    c.restoreState()

def build(out):
    from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, FrameBreak, NextPageTemplate
    L, R, T, B, G = 16*mm, 16*mm, 14*mm, 16*mm, 8*mm
    W = (A4[0] - L - R - G) / 2
    head_h = 46*mm
    first = PageTemplate(id="first", onPage=draw_page, frames=[
        Frame(L, A4[1]-T-head_h, A4[0]-L-R, head_h, id="head", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
        Frame(L, B, W, A4[1]-T-head_h-B, id="c1", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
        Frame(L+W+G, B, W, A4[1]-T-head_h-B, id="c2", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])
    later = PageTemplate(id="later", onPage=draw_page, frames=[
        Frame(L, B, W, A4[1]-T-B, id="l1", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
        Frame(L+W+G, B, W, A4[1]-T-B, id="l2", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])
    doc = BaseDocTemplate(out, pagesize=A4, pageTemplates=[first, later], title="CQC Evidence Folder Checklist", author="Teething Issues")
    story = [NextPageTemplate("later")]
    logo = os.path.join(HERE, "..", "skool", "circle-icon.jpg")
    hdr = Table([[Paragraph("TEETHING ISSUES CIRCLE · FREE RESOURCE", EYE), Image(logo, 14*mm, 14*mm) if os.path.exists(logo) else ""]], colWidths=[None, 16*mm])
    hdr.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
    story += [hdr, Paragraph("CQC Evidence Folder Checklist", H1), Spacer(1, 4),
              Paragraph("The 10 areas inspectors check, and what to have ready in each. Tick an item only when it's present, current and in date. "
                        "This is a preparation checklist for practices in England, not a guaranteed inspection script: real inspections vary.", LEDE),
              FrameBreak()]
    for a in AREAS:
        story.append(area_block(*a))
    et = Table([[box(), Paragraph(e, ITEM)] for e in EXTRA], colWidths=[5*mm, None])
    et.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),1.2),("BOTTOMPADDING",(0,0),(-1,-1),1.2)]))
    story.append(KeepTogether([Paragraph('<font color="#B68A3E">+</font>&nbsp;&nbsp;Also have ready', H2), Spacer(1, 3), et, Spacer(1, 8)]))
    story.append(KeepTogether([Paragraph("Three rules that save inspections", H2), Spacer(1, 3),
             Paragraph("1. Lapsed? Book it now, even if the date falls after the inspection, and keep the booking as evidence.", ITEM), Spacer(1,2),
             Paragraph("2. Every audit needs an action plan, and a re-audit 3–6 months later that shows what improved.", ITEM), Spacer(1,2),
             Paragraph("3. Spot a gap on the day? Own it, log it and explain the fix. Evidence you already had can still be considered after the visit.", ITEM)]))
    doc.build(story)

if __name__ == "__main__":
    build(os.path.join(HERE, "cqc-evidence-folder-checklist.pdf"))
    print("built")

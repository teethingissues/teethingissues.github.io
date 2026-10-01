"""Builds the Teething Issues Circle (Skool) artwork + ad images from the Mino brand photos.
Run: python3 build_art.py   (outputs into ./skool and ./ads)"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
MINO = os.path.join(SITE, "mino")
FONTS = os.environ.get("FONTS_DIR", os.path.join(HERE, "fonts"))
PAPER, INK, DIM, GOLD = (251, 248, 242), (47, 42, 36), (109, 99, 86), (182, 138, 62)

def font(name, size): return ImageFont.truetype(os.path.join(FONTS, name), size)
def serif(s): return font("Cormorant.ttf", s)
def sans(s): return font("Jost.ttf", s)

def fill_crop(path, w, h, focus=0.35, hfocus=0.5):
    im = Image.open(path).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(hfocus, focus))

def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = word
    lines.append(cur); return lines

def bold_serif(d, xy, text, f, fill):
    # Cormorant variable font renders light; a 1px stroke gives the semibold look of the site
    d.text(xy, text, font=f, fill=fill, stroke_width=max(1, f.size // 60), stroke_fill=fill)

FOOT = "TEETHING ISSUES CIRCLE  ·  ON SKOOL  ·  LINK IN BIO"

def ad(photo, headline, sub, out, w, h, photo_frac, focus=0.3, scale=1.0):
    img = Image.new("RGB", (w, h), PAPER)
    ph = int(h * photo_frac)
    img.paste(fill_crop(photo, w, ph, focus), (0, 0))
    d = ImageDraw.Draw(img)
    pad = int(w * 0.068); y = ph + int(h * 0.055)
    hf = serif(int(w * 0.075 * scale)); sf = sans(int(w * 0.027 * scale)); ff = sans(int(w * 0.022 * min(scale, 1.2)))
    for line in wrap(d, headline, hf, w - 2 * pad):
        bold_serif(d, (pad, y), line, hf, INK); y += int(hf.size * 1.05)
    y += int(w * 0.012)
    for line in wrap(d, sub, sf, w - 2 * pad):
        d.text((pad, y), line, font=sf, fill=DIM); y += int(sf.size * 1.4)
    fy = h - int(h * 0.06) - ff.size
    d.text((pad, fy), FOOT, font=ff, fill=GOLD, stroke_width=0)
    img.save(out, quality=90)

def wide_cover(photo, eyebrow, title, sub, out, w=1460, h=752, focus=0.3, hfocus=0.5):
    img = Image.new("RGB", (w, h), PAPER)
    pw = int(w * 0.46)
    img.paste(fill_crop(photo, pw, h, focus, hfocus), (0, 0))
    d = ImageDraw.Draw(img)
    x = pw + int(w * 0.05); maxw = w - x - int(w * 0.05)
    ef, tf, sf = sans(int(h * 0.036)), serif(int(h * 0.12)), sans(int(h * 0.04))
    lines = wrap(d, title, tf, maxw); sublines = wrap(d, sub, sf, maxw) if sub else []
    block = ef.size * 2 + len(lines) * int(tf.size * 1.02) + (len(sublines) * int(sf.size * 1.45) + 20 if sub else 0)
    y = (h - block) // 2
    d.text((x, y), eyebrow.upper(), font=ef, fill=GOLD); y += ef.size * 2
    for line in lines:
        bold_serif(d, (x, y), line, tf, INK); y += int(tf.size * 1.02)
    y += 20
    for line in sublines:
        d.text((x, y), line, font=sf, fill=DIM); y += int(sf.size * 1.45)
    img.save(out, quality=90)

def icon(out, size=512):
    logo = Image.open(os.path.join(SITE, "assets", "logo.jpg")).convert("RGB")
    # the logo is a round textured badge; shrink it inside a cream circle so the wordmark isn't clipped by Skool's round mask
    bg = Image.new("RGB", (size, size), PAPER)
    inner = int(size * 0.80)
    logo = ImageOps.fit(logo, (inner, inner), Image.LANCZOS)
    mask = Image.new("L", (inner, inner), 0); ImageDraw.Draw(mask).ellipse((0, 0, inner - 1, inner - 1), fill=255)
    off = (size - inner) // 2; bg.paste(logo, (off, off), mask); bg.save(out, quality=92)

P = lambda n: os.path.join(MINO, n)
SK, AD = os.path.join(HERE, "skool"), os.path.join(HERE, "ads")

# --- Skool: icon, cover banner, 5 classroom covers
icon(os.path.join(SK, "circle-icon.jpg"))
def banner_overlay(photo, eyebrow, title, sub, out, w=1084, h=576):
    img = fill_crop(photo, w, h, 0.5); d = ImageDraw.Draw(img)
    x = int(w * 0.715); maxw = w - x - int(w * 0.03)
    ef, tf, sf = sans(int(h * 0.028)), serif(int(h * 0.074)), sans(int(h * 0.03))
    lines = wrap(d, title, tf, maxw); sublines = wrap(d, sub, sf, maxw)
    y = int(h * 0.27)
    d.text((x, y), eyebrow.upper(), font=ef, fill=GOLD); y += int(ef.size * 2)
    for line in lines: bold_serif(d, (x, y), line, tf, INK); y += int(tf.size * 1.02)
    y += 14
    for line in sublines: d.text((x, y), line, font=sf, fill=DIM); y += int(sf.size * 1.45)
    img.save(out, quality=90)

SRC = os.path.join(HERE, "src")
banner_overlay(os.path.join(SRC, "banner-team.jpg"), "Teething Issues Circle", "Run a calmer, compliant, growing practice.",
               "CQC, team and growth for UK dental practices.", os.path.join(SK, "circle-cover-banner.jpg"))
COURSES = [
    ("start-here", "../circle/src/start-here-reception.jpg", "Course 1", "Start Here", "Welcome, how the Circle works, and introduce yourself."),
    ("cqc-foundations", "mino-compliance.jpg", "Course 2", "CQC Compliance Foundations", "Checklists, your evidence folder and mock inspection prep."),
    ("team-delegation", "mino-training.jpg", "Course 3", "Team & Delegation", "Hiring, onboarding and systems that run without you."),
    ("growth", "mino-with-practice-owner.jpg", "Course 4", "Growth & Patient Numbers", "Reactivation, reviews and referrals that work."),
    ("ai-in-practice", "mino-evenings-back.jpg", "Course 5", "Bringing AI Into Your Practice", "What AI can take off your plate, step by step."),
]
HFOCUS = {"start-here": 0.22}
for slug, ph, eb, title, sub in COURSES:
    wide_cover(P(ph), eb, title, sub, os.path.join(SK, "course-%s.jpg" % slug), hfocus=HFOCUS.get(slug, 0.5))

# --- Ads: 4 ads x 3 sizes
ADS = [
    ("together", "mino-with-practice-owner.jpg", "You don't have to figure it out alone.", "A private community for UK dental practice owners and managers."),
    ("inspection", "mino-compliance.jpg", "Inspection-ready, together.", "Real CQC checklists, evidence folder templates and mock inspection prep."),
    ("ask", "mino-training.jpg", "Ask the questions you can't ask anyone else.", "A monthly live Q&A with our founder, a CQC Registered Manager who started as a dental nurse."),
    ("ai", "mino-evenings-back.jpg", "Bring AI into your practice, properly.", "Practical walkthroughs of what AI can take off your plate, from people already using it."),
]
for slug, ph, head, sub in ADS:
    ad(P(ph), head, sub, os.path.join(AD, "%s-square.jpg" % slug), 1080, 1080, 0.58)
    ad(P(ph), head, sub, os.path.join(AD, "%s-portrait.jpg" % slug), 1080, 1350, 0.62)
    ad(P(ph), head, sub, os.path.join(AD, "%s-story.jpg" % slug), 1080, 1920, 0.6, scale=1.3)
print("built", len(os.listdir(SK)), "skool images,", len(os.listdir(AD)), "ad images")

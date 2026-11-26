"""Model-303's two tabs, laid out for the MPC's 1280x628 plugin area (screen pixels, y from the top of the plugin area).
The synth section only: no keys, pattern or sequencer controls. Controls stay left of x ~1025, where the Q-Link
sidebar comes in."""
import make_skin as m
from make_skin import INK, DIM, Tab

K = m.add_knob
NAME = ("ACID", "303")       # the wordmark, either side of its dash


def logo(t, sub):
    # Earth Normal has no dash: the name's two halves set apart, the dash drawn between them at the letters' weight
    size = 46
    f = m.font(size, "Logo")
    x = 60
    t.text(x, 66, NAME[0], size, "Logo", INK, "lm")
    x += f.getlength(NAME[0]) / m.SS + 8
    dash = 22
    for dy, col in ((1, (255, 255, 255, 120)), (0, INK + (255,))):
        t.draw.rectangle((x * m.SS, (64 - 3.5 + dy) * m.SS, (x + dash) * m.SS, (64 + 3.5 + dy) * m.SS), fill=col)
    t.text(x + dash + 8, 66, NAME[1], size, "Logo", INK, "lm")
    t.text(1218, 67, sub, 19, "Bold", DIM, "rm")      # the tagline at the top right, level with the wordmark


def saw_icon(t, x, y, s=9):
    t.draw.line([((x - s) * m.SS, (y + s * 0.6) * m.SS), ((x + s) * m.SS, (y - s * 0.6) * m.SS), ((x + s) * m.SS, (y + s * 0.6) * m.SS)],
                fill=INK, width=int(2.2 * m.SS))


def square_icon(t, x, y, s=9):
    p = [(x - s, y + s * 0.6), (x - s, y - s * 0.6), (x, y - s * 0.6), (x, y + s * 0.6), (x + s, y + s * 0.6), (x + s, y - s * 0.6)]
    t.draw.line([(a * m.SS, b * m.SS) for a, b in p], fill=INK, width=int(2.2 * m.SS))


def end_labels(t, cx, cy, r, lo, hi, ring=None):
    """Words at the ends of a pot's scale (SLOW/FAST, MIN/MAX)."""
    rr = (ring or r) + 28
    x0, y0 = m.polar(cx, cy, rr, -150)
    x1, y1 = m.polar(cx, cy, rr, 150)
    t.text(x0 - 4, y0 + 6, lo, 14, "SemiBold", INK)
    t.text(x1 + 4, y1 + 6, hi, 14, "SemiBold", INK)


# ------------------------------------------------------------------------------------------------ 303

def tb303(params):
    t = Tab("303", ["cutoff", "resonance", "env_mod", "decay", "accent", "tune", "volume", "waveform", "accent_hold", "quality"])
    logo(t, "CIRCUIT-MODELLED ACID BASS SYNTHESIZER")
    row = 238
    t.well(26, 124, 1024, 336)
    for x, key, name in zip([100, 270, 440, 610, 780, 950],
                            ["tune", "cutoff", "resonance", "env_mod", "decay", "accent"],
                            ["TUNE", "CUTOFF", "RESONANCE", "ENV MOD", "DECAY", "ACCENT"]):
        K(t, key, x, row, 46, name)
    # lower row: WAVE | VOLUME | ACCENT; the right-hand column (under the Q-Link sidebar when it slides in): QUALITY
    y = 492
    for x0, x1 in ((26, 290), (300, 690), (700, 1024)):
        t.well(x0, 354, x1, 578)
    t.well(1040, 124, 1252, 336)
    t.well(1040, 354, 1252, 578)
    t.header(150, 384, 170, "WAVE")
    m.add_switch(t, "waveform", 132, y, ["up", "down"])
    saw_icon(t, 170, y - 26)
    square_icon(t, 170, y + 26)
    t.header(500, 384, 280, "VOLUME")
    K(t, "volume", 500, y - 4, 56, ring=56)
    end_labels(t, 500, y - 4, 56, "MIN", "MAX")
    t.header(860, 384, 200, "ACCENT")
    m.add_key(t, "accent_hold", 860, y, "HOLD")
    t.header(1146, 384, 180, "QUALITY")
    m.add_switch(t, "quality", 1126, y, ["up", "mid", "down"], ["HQ", "AUTO", "ECO"], label_dx=30)
    return t


ALL = [tb303]

# -*- coding: utf-8 -*-
"""
Motor cuantitativo: Bonzi vs Van De Zandschulp - Winston-Salem 2026 QF (Dura).
Fuente: Tennis Abstract (matchmx del player-classic + reporte de Elo).
Sin sesgo de ranking ATP: todo se construye desde puntos, juegos y Elo por superficie.
"""
import re, json, math, random, datetime as dt
import numpy as np, pandas as pd

pd.set_option("display.width", 220); pd.set_option("display.max_columns", 40)
HOY = dt.date(2026, 8, 28)
CORTE_52 = HOY - dt.timedelta(weeks=52)

COLS = ["date","tourn","surface","level","result","rank","seed","entry","round","score",
        "bestof","opp","opp_rank","opp_seed","opp_entry","opp_hand","opp_dob","opp_ht","opp_ctry","x19",
        "min","ace","df","svpt","fstIn","fstWon","sndWon","svGms","bpSaved","bpFaced",
        "o_ace","o_df","o_svpt","o_fstIn","o_fstWon","o_sndWon","o_svGms","o_bpSaved","o_bpFaced"]

def load_matchmx(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"var matchmx = (\[.*?\]);", src, re.S)
    rows = json.loads(m.group(1))
    df = pd.DataFrame([r[:len(COLS)] for r in rows], columns=COLS)
    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d").dt.date
    for c in COLS[20:]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["rank"] = pd.to_numeric(df["rank"], errors="coerce")
    df["opp_rank"] = pd.to_numeric(df["opp_rank"], errors="coerce")
    return df

def games_from_score(s):
    """Total de juegos disputados (ignora RET/WO y puntos de super-TB)."""
    if not isinstance(s, str) or not s.strip() or "W/O" in s: return np.nan
    tot = 0
    for st in s.replace("RET", "").split():
        m = re.match(r"^(\d+)-(\d+)", st)
        if not m: continue
        tot += int(m.group(1)) + int(m.group(2))
    return tot if tot else np.nan

def sets_played(s):
    if not isinstance(s, str) or not s.strip() or "W/O" in s: return np.nan
    return sum(1 for st in s.split() if re.match(r"^\d+-\d+", st))

def bloque(df, etiqueta):
    """Agrega a nivel de punto/juego (pooled), no promedio de ratios."""
    d = df.dropna(subset=["svpt", "o_svpt"])
    d = d[d.svpt > 0]
    if d.empty: return None
    spw = (d.fstWon.sum() + d.sndWon.sum()) / d.svpt.sum()
    rpw = (d.o_svpt.sum() - d.o_fstWon.sum() - d.o_sndWon.sum()) / d.o_svpt.sum()
    brk_perd = (d.bpFaced.sum() - d.bpSaved.sum())
    hold = (d.svGms.sum() - brk_perd) / d.svGms.sum()
    brk_hechos = (d.o_bpFaced.sum() - d.o_bpSaved.sum())
    brk = brk_hechos / d.o_svGms.sum()
    dr = rpw / (1 - spw)
    return dict(bloque=etiqueta, M=len(d), V=int((d.result == "W").sum()), D=int((d.result == "L").sum()),
                SPW=round(100*spw,1), RPW=round(100*rpw,1), DR=round(dr,3),
                Hold=round(100*hold,1), Break=round(100*brk,1),
                Ace=round(100*d.ace.sum()/d.svpt.sum(),1), DF=round(100*d.df.sum()/d.svpt.sum(),1),
                BPconv=round(100*brk_hechos/max(d.o_bpFaced.sum(),1),1),
                BPsalv=round(100*d.bpSaved.sum()/max(d.bpFaced.sum(),1),1))

J = {"Bonzi": load_matchmx("classic_Bonzi.html"),
     "BVDZ":  load_matchmx("classic_BVDZ.html")}
for n, d in J.items():
    d["games"] = d.score.map(games_from_score)
    d["sets"]  = d.score.map(sets_played)

print("### 1. BLOQUES DE FORMA (agregado pooled a nivel de punto)\n")
res = {}
for n, d in J.items():
    hard52 = d[(d.date >= CORTE_52) & (d.surface == "Hard") & (d.result.isin(["W","L"]))]
    tot52  = d[(d.date >= CORTE_52) & (d.result.isin(["W","L"]))]
    hard26 = d[(d.date >= dt.date(2026,1,1)) & (d.surface == "Hard") & (d.result.isin(["W","L"]))]
    us_swing = d[(d.date >= dt.date(2026,7,20)) & (d.surface == "Hard") & (d.result.isin(["W","L"]))]
    filas = [bloque(hard52,"Dura 52sem"), bloque(hard26,"Dura 2026"),
             bloque(us_swing,"Gira US (desde 20-jul)"), bloque(tot52,"Todas sup. 52sem")]
    res[n] = pd.DataFrame([f for f in filas if f])
    print(f"--- {n} ---"); print(res[n].to_string(index=False)); print()

print("### 2. HEAD TO HEAD\n")
h2h = J["Bonzi"][J["Bonzi"].opp.str.contains("Zandschulp", na=False)]
print(h2h[["date","tourn","surface","round","result","score","rank","opp_rank","min","games"]].to_string(index=False))
print()

print("### 3. CARGA / DESGASTE - Winston-Salem 2026 y 14 dias previos\n")
for n, d in J.items():
    ws = d[(d.tourn.str.contains("Winston-Salem", na=False)) & (d.date >= dt.date(2026,8,1)) & (d.result.isin(["W","L"]))]
    prev14 = d[(d.date >= HOY - dt.timedelta(days=14)) & (d.result.isin(["W","L"]))]
    prev28 = d[(d.date >= HOY - dt.timedelta(days=28)) & (d.result.isin(["W","L"]))]
    print(f"--- {n} ---")
    print(ws[["date","round","result","score","min","sets","games"]].to_string(index=False))
    print(f"  Torneo actual : {len(ws)} partidos | {int(ws['min'].sum())} min | {int(ws.sets.sum())} sets | {int(ws.games.sum())} juegos")
    print(f"  Ultimos 14 d  : {len(prev14)} partidos | {int(prev14['min'].sum())} min")
    print(f"  Ultimos 28 d  : {len(prev28)} partidos | {int(prev28['min'].sum())} min\n")

print("### 4. DISTRIBUCION DE JUEGOS (Dura, 52 semanas, best-of-3)\n")
for n, d in J.items():
    g = d[(d.date >= CORTE_52) & (d.surface == "Hard") & (d.bestof == "3") & d.games.notna()].games
    print(f"{n:6s} n={len(g):3d}  media={g.mean():5.2f}  mediana={g.median():5.1f}  "
          f"P(>21.5)={100*(g>21.5).mean():5.1f}%  P(>22.5)={100*(g>22.5).mean():5.1f}%  "
          f"P(3 sets)={100*(d[(d.date>=CORTE_52)&(d.surface=='Hard')&(d.bestof=='3')].sets==3).mean():5.1f}%")
print()

# ---------------- 5. ELO por superficie ----------------
elo_src = open("elo.html", encoding="utf-8", errors="replace").read()
def elo_row(name):
    m = re.search(r"<tr>(?:(?!</tr>).)*?" + name.replace(" ", "&nbsp;") + r"</a>.*?</tr>", elo_src, re.S)
    v = [re.sub(r"<[^>]*>", "", x).replace("&nbsp;", " ").strip()
         for x in re.findall(r"<td[^>]*>(.*?)</td>", m.group(0), re.S)]
    return v
b, z = elo_row("Benjamin&nbsp;Bonzi"), elo_row("Botic&nbsp;Van&nbsp;De&nbsp;Zandschulp")
lab = ["EloRk","Player","Age","Elo","_","hEloRk","hElo","cEloRk","cElo","gEloRk","gElo","_","PeakElo","PeakMes","_","ATPRk","LogDiff"]
elo = pd.DataFrame([b, z], index=["Bonzi","BVDZ"], columns=lab).drop(columns="_")
print("### 5. ELO (Tennis Abstract)\n"); print(elo.to_string()); print()

hB, hZ = float(b[6]), float(z[6])
gB, gZ = float(b[3]), float(z[3])
p_h = 1/(1+10**((hZ-hB)/400)); p_g = 1/(1+10**((gZ-gB)/400))
print(f"hElo Bonzi {hB} vs BVDZ {hZ}  -> diff {hZ-hB:+.1f} a favor de BVDZ")
print(f"P(Bonzi gana) segun hElo   = {100*p_h:.1f}%  (cuota justa {1/p_h:.2f})")
print(f"P(Bonzi gana) segun Elo gral= {100*p_g:.1f}%  (cuota justa {1/p_g:.2f})\n")

# ---------------- 6. Simulacion punto a punto ----------------
AVG_SPW_HARD, AVG_RPW_HARD = 0.645, 0.355
def spw_ajustado(spw_prop, rpw_rival):
    return min(max(spw_prop - (rpw_rival - AVG_RPW_HARD), 0.35), 0.85)

sB = res["Bonzi"].set_index("bloque").loc["Dura 52sem"]
sZ = res["BVDZ"].set_index("bloque").loc["Dura 52sem"]
pB = spw_ajustado(sB.SPW/100, sZ.RPW/100)
pZ = spw_ajustado(sZ.SPW/100, sB.RPW/100)
print(f"### 6. SIMULACION (100k best-of-3, TB a 6-6)\n")
print(f"SPW ajustado -> Bonzi {100*pB:.1f}% | BVDZ {100*pZ:.1f}%\n")

rng = random.Random(20260828)
def juego(p):
    a = b_ = 0
    while True:
        if rng.random() < p: a += 1
        else: b_ += 1
        if a >= 4 and a - b_ >= 2: return 1
        if b_ >= 4 and b_ - a >= 2: return 0
def tiebreak(p, q, saca_a):
    a = b_ = 0; n = 0; turno = saca_a
    while True:
        p_now = p if turno else (1 - q)
        if rng.random() < p_now: a += 1
        else: b_ += 1
        n += 1
        if n == 1 or (n - 1) % 2 == 0: turno = not turno
        if a >= 7 and a - b_ >= 2: return 1
        if b_ >= 7 and b_ - a >= 2: return 0
def set_(p, q, saca_a):
    ja = jb = 0; turno = saca_a
    while True:
        gana = juego(p) if turno else (1 - juego(q))
        if gana: ja += 1
        else: jb += 1
        turno = not turno
        if ja == 6 and jb <= 4: return 1, ja + jb, turno
        if jb == 6 and ja <= 4: return 0, ja + jb, turno
        if ja == 7: return 1, ja + jb, turno
        if jb == 7: return 0, ja + jb, turno
        if ja == 6 and jb == 6:
            w = tiebreak(p, q, turno); return w, 13, turno

N = 100000
victorias = 0; juegos = []; spreads = []; tres_sets = 0
for _ in range(N):
    sa = sb = 0; tot = 0; ga = gb = 0; saca_a = rng.random() < 0.5
    while sa < 2 and sb < 2:
        w, g, saca_a = set_(pB, pZ, saca_a)
        tot += g
        if w: sa += 1
        else: sb += 1
        # reparto aproximado de juegos del set al ganador del set
        if w: ga += (g + 2) // 2 + 1; gb += g - ((g + 2) // 2 + 1)
        else: gb += (g + 2) // 2 + 1; ga += g - ((g + 2) // 2 + 1)
    victorias += sa == 2; juegos.append(tot); spreads.append(ga - gb)
    tres_sets += (sa + sb == 3)
j = np.array(juegos); sp = np.array(spreads)
pw = victorias / N
print(f"P(Bonzi gana) modelo de puntos = {100*pw:.1f}%   (cuota justa {1/pw:.2f})")
print(f"P(BVDZ gana)                   = {100*(1-pw):.1f}%   (cuota justa {1/(1-pw):.2f})")
print(f"Juegos totales: media {j.mean():.2f} | mediana {np.median(j):.0f} | 3 sets {100*tres_sets/N:.1f}%")
for L in (20.5, 21.5, 22.5, 23.5):
    print(f"   P(Over {L}) = {100*(j>L).mean():5.1f}%  (cuota justa {1/max((j>L).mean(),1e-9):.2f})   "
          f"P(Under {L}) = {100*(j<L).mean():5.1f}%  (cuota justa {1/max((j<L).mean(),1e-9):.2f})")
print()
for hcap in (-4.5, -3.5, -2.5, 2.5, 3.5, 4.5):
    p = (sp + hcap > 0).mean()
    print(f"   Hcap juegos Bonzi {hcap:+.1f}: P={100*p:5.1f}% (cuota justa {1/max(p,1e-9):.2f}) | "
          f"BVDZ {-hcap:+.1f}: P={100*(1-p):5.1f}% (cuota justa {1/max(1-p,1e-9):.2f})")

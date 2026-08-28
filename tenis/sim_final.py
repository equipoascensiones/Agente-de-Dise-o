# -*- coding: utf-8 -*-
"""Simulacion final con metricas AJUSTADAS POR NIVEL (solo ATP tour, dura, 52 semanas)."""
import numpy as np, random

AVG_RPW = 0.355
# Dura 52 semanas, SOLO nivel ATP (des-sesgado de Challengers)
P = {"Bonzi": dict(spw=0.647, rpw=0.354, hold=0.813, brk=0.194),
     "BVDZ":  dict(spw=0.658, rpw=0.363, hold=0.847, brk=0.187)}

def ajusta(a, b): return min(max(P[a]["spw"] - (P[b]["rpw"] - AVG_RPW), .40), .82)
pB, pZ = ajusta("Bonzi","BVDZ"), ajusta("BVDZ","Bonzi")

rng = random.Random(7)
def juego(p):
    a=b=0
    while True:
        if rng.random()<p: a+=1
        else: b+=1
        if a>=4 and a-b>=2: return 1
        if b>=4 and b-a>=2: return 0
def tb(p,q,t):
    a=b=n=0
    while True:
        if rng.random() < (p if t else 1-q): a+=1
        else: b+=1
        n+=1
        if n==1 or (n-1)%2==0: t=not t
        if a>=7 and a-b>=2: return 1
        if b>=7 and b-a>=2: return 0
def set_(p,q,t):
    ja=jb=0
    while True:
        g = juego(p) if t else 1-juego(q)
        if g: ja+=1
        else: jb+=1
        t=not t
        if ja==6 and jb<=4: return 1,ja,jb,t
        if jb==6 and ja<=4: return 0,ja,jb,t
        if ja==7: return 1,ja,jb,t
        if jb==7: return 0,ja,jb,t
        if ja==6 and jb==6:
            w=tb(p,q,t); 
            return w,(7 if w else 6),(6 if w else 7),t

def corre(pB,pZ,N=200000):
    win=0; tot=[]; spr=[]; t3=0
    for _ in range(N):
        sa=sb=0; ga=gb=0; t=rng.random()<.5
        while sa<2 and sb<2:
            w,x,y,t = set_(pB,pZ,t)
            ga+=x; gb+=y
            sa+= w; sb+= 1-w
        win+= sa==2; tot.append(ga+gb); spr.append(ga-gb); t3+= (sa+sb)==3
    return win/N, np.array(tot), np.array(spr), t3/N

print(f"SPW ajustado (nivel ATP): Bonzi {100*pB:.1f}%  BVDZ {100*pZ:.1f}%\n")
pw, j, sp, t3 = corre(pB,pZ)
print("== ESCENARIO BASE (sin ajuste de desgaste) ==")
print(f"P(Bonzi) {100*pw:.1f}% (justa {1/pw:.2f}) | P(BVDZ) {100*(1-pw):.1f}% (justa {1/(1-pw):.2f})")
print(f"Juegos: media {j.mean():.2f} mediana {np.median(j):.0f} | 3 sets {100*t3:.1f}%")
for L in (20.5,21.5,22.5,23.5):
    print(f"  Over {L}: {100*(j>L).mean():5.1f}% (justa {1/(j>L).mean():.2f})")
print()

# Escenario con penalizacion de desgaste a Bonzi (-158 min de carga en el torneo,
# -376 min en 14 dias): -1.5 pts de SPW y -1.0 pt de RPW.
pB2 = pB - 0.015
print("== ESCENARIO CON DESGASTE (Bonzi -1.5 pts SPW) ==")
pw2, j2, sp2, t32 = corre(pB2, pZ)
print(f"P(Bonzi) {100*pw2:.1f}% (justa {1/pw2:.2f}) | P(BVDZ) {100*(1-pw2):.1f}% (justa {1/(1-pw2):.2f})")
print(f"Juegos: media {j2.mean():.2f} | 3 sets {100*t32:.1f}%")
for L in (21.5,22.5):
    print(f"  Over {L}: {100*(j2>L).mean():5.1f}% (justa {1/(j2>L).mean():.2f})")
print()

# --- Consenso de probabilidad de victoria ---
p_elo = 1/(1+10**((1739.4-1671.0)/400))
comp = {"hElo (superficie)": p_elo, "Modelo puntos base": pw, "Modelo puntos c/desgaste": pw2}
pes  = {"hElo (superficie)": .45, "Modelo puntos base": .30, "Modelo puntos c/desgaste": .25}
cons = sum(comp[k]*pes[k] for k in comp)
print("== CONSENSO ML ==")
for k,v in comp.items(): print(f"  {k:26s} P(Bonzi)={100*v:5.1f}%  peso {pes[k]:.2f}")
print(f"  --> CONSENSO P(Bonzi)={100*cons:.1f}% (justa {1/cons:.2f}) | "
      f"P(BVDZ)={100*(1-cons):.1f}% (justa {1/(1-cons):.2f})")
print(f"  Valor si BVDZ paga > {1/(1-cons):.2f} | valor si Bonzi paga > {1/cons:.2f}\n")

# --- Consenso de totales: shrink del modelo iid hacia la base empirica ---
EMP = {"media": 23.67, "o215": .596, "o225": .500}   # pool ATP-tour dura bo3 52s
for L,key,mod in ((21.5,"o215",(j>21.5).mean()), (22.5,"o225",(j>22.5).mean())):
    blend = .5*mod + .5*EMP[key]
    print(f"== TOTALES {L} ==  modelo {100*mod:.1f}% | empirico {100*EMP[key]:.1f}% "
          f"| CONSENSO {100*blend:.1f}% -> justa Over {1/blend:.2f} / Under {1/(1-blend):.2f}")
print(f"\nMedia de juegos consenso: {(0.5*j.mean()+0.5*EMP['media']):.2f}")

print("\n== HANDICAP DE JUEGOS (escenario con desgaste) ==")
for h in (-5.5,-4.5,-3.5,-2.5,-1.5,1.5,2.5,3.5,4.5,5.5):
    p = (sp2 + h > 0).mean()
    print(f"  Bonzi {h:+.1f}: {100*p:5.1f}% (justa {1/max(p,1e-9):.2f})   |   "
          f"BVDZ {-h:+.1f}: {100*(1-p):5.1f}% (justa {1/max(1-p,1e-9):.2f})")

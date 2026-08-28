# -*- coding: utf-8 -*-
"""Desglose por nivel de torneo (ATP vs Challenger) + juegos empiricos + torneo actual."""
import re, json, datetime as dt, numpy as np, pandas as pd
exec(open("analiza.py").read().split("print(\"### 1.")[0])   # reutiliza loaders

TOUR = {"A","M","G","F","D"}   # ATP250/500, Masters, Slam, Finals, Davis
print("### 1b. DURA - ULTIMAS 52 SEMANAS, SEPARADO POR NIVEL\n")
for n, d in J.items():
    h = d[(d.date >= CORTE_52) & (d.surface == "Hard") & (d.result.isin(["W","L"]))]
    filas = [bloque(h[h.level.isin(TOUR)], "Dura 52s - ATP tour"),
             bloque(h[~h.level.isin(TOUR)], "Dura 52s - Challenger/Q"),
             bloque(h, "Dura 52s - TODO")]
    print(f"--- {n} ---")
    print(pd.DataFrame([f for f in filas if f]).to_string(index=False)); print()

print("### 4b. JUEGOS EMPIRICOS - Dura, bo3, 52 semanas, SOLO nivel ATP\n")
for n, d in J.items():
    sub = d[(d.date >= CORTE_52) & (d.surface == "Hard") & (d.bestof == "3")
            & (d.level.isin(TOUR)) & d.games.notna()]
    g = sub.games
    print(f"{n:6s} n={len(g):3d} media={g.mean():5.2f} mediana={g.median():5.1f} "
          f"P(>20.5)={100*(g>20.5).mean():5.1f}% P(>21.5)={100*(g>21.5).mean():5.1f}% "
          f"P(>22.5)={100*(g>22.5).mean():5.1f}% 3sets={100*(sub.sets==3).mean():5.1f}%")
todos = pd.concat([d[(d.date >= CORTE_52) & (d.surface=="Hard") & (d.bestof=="3")
                     & (d.level.isin(TOUR)) & d.games.notna()] for d in J.values()])
print(f"\nPool combinado n={len(todos)} media={todos.games.mean():.2f} "
      f"P(>21.5)={100*(todos.games>21.5).mean():.1f}% P(>22.5)={100*(todos.games>22.5).mean():.1f}%")

print("\n### 3b. RENDIMIENTO DENTRO DE WINSTON-SALEM 2026\n")
for n, d in J.items():
    ws = d[(d.tourn.str.contains("Winston-Salem", na=False)) & (d.date >= dt.date(2026,8,1))
           & (d.result.isin(["W","L"]))]
    print(f"{n:6s}", bloque(ws, "WS 2026"))

print("\n### 3c. HISTORIAL EN WINSTON-SALEM (carrera)\n")
for n, d in J.items():
    ws = d[(d.tourn.str.contains("Winston-Salem", na=False)) & (d.result.isin(["W","L"]))]
    print(f"--- {n}: {int((ws.result=='W').sum())}-{int((ws.result=='L').sum())} ---")
    print(ws[["date","round","result","opp","score"]].to_string(index=False)); print()

print("### 7. RIESGO DE CALENDARIO: partidos jugados la semana previa a un Grand Slam\n")
for n, d in J.items():
    prev = d[(d.date >= dt.date(2021,1,1)) & (d.result.isin(["W","L"]))]
    print(f"{n}: eventos ATP 250 en agosto (semana pre-US Open):")
    ago = prev[(pd.to_datetime(prev.date).dt.month == 8) & (pd.to_datetime(prev.date).dt.day >= 15)]
    print(ago.groupby([pd.to_datetime(ago.date).dt.year, "tourn"]).agg(
        M=("result","size"), V=("result", lambda s:(s=="W").sum())).to_string()); print()

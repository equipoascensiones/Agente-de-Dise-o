"""
Parser Tennis Abstract -> DataFrames.
La pagina player.cgi inyecta todas sus tablas desde /jsfrags/<Player>.js.
El proxy de red de este entorno resetea el trafico HTTPS del navegador, asi que
descargamos el frag con curl y renderizamos el DOM localmente (file://) con
Playwright/Chromium headless antes de extraer las tablas.
"""
import asyncio, os, re, io, sys, html, json
import pandas as pd
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PLAYERS = {"Bonzi": "BenjaminBonzi.js", "BVDZ": "BoticVanDeZandschulp.js"}
WANT = ["recent-results", "last52-splits", "career-splits", "recent-events",
        "head-to-heads", "tour-years", "pbp-stats", "serve-speed"]

def frag_html(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"var player_frag\s*=\s*`(.*?)`;", src, re.S)
    if not m:
        raise SystemExit(f"no player_frag in {path}")
    return m.group(1)

def build_shell(body, out):
    open(out, "w", encoding="utf-8").write(
        "<!doctype html><meta charset='utf-8'><body><div id='root'></div>"
        "<script id='payload' type='text/plain'>" + body.replace("</script", "<\\/script") +
        "</script><script>document.getElementById('root').innerHTML="
        "document.getElementById('payload').textContent;</script></body>")

async def render(files):
    tables = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True,
                                    executable_path="/opt/pw-browsers/chromium",
                                    args=["--no-sandbox"])
        pg = await (await b.new_context()).new_page()
        for name, f in files.items():
            await pg.goto("file://" + f, wait_until="load", timeout=60000)
            await pg.wait_for_selector("#recent-results", timeout=60000)
            tables[name] = await pg.evaluate(
                """(ids)=>Object.fromEntries(ids.map(i=>{const e=document.getElementById(i);
                    return [i, e?e.outerHTML:null];}).filter(([_,v])=>v))""", WANT)
        await b.close()
    return tables

def main():
    shells = {}
    for name, js in PLAYERS.items():
        out = os.path.join(HERE, f"_dom_{name}.html")
        build_shell(frag_html(os.path.join(HERE, js)), out)
        shells[name] = out
    tables = asyncio.run(render(shells))
    for name, tabs in tables.items():
        for tid, h in tabs.items():
            try:
                df = pd.read_html(io.StringIO(h))[0]
            except Exception as e:
                print(f"skip {name}/{tid}: {e}", file=sys.stderr); continue
            df.to_csv(os.path.join(HERE, f"{name}__{tid}.csv"), index=False)
            print(f"saved {name}__{tid}.csv {df.shape}")

main()

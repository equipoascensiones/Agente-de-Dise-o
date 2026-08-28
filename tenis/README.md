# Pipeline cuantitativo de tenis (Tennis Abstract)

Extrae y modela datos de Tennis Abstract sin apoyarse en el ranking ATP/WTA:
todo se construye desde puntos, juegos y Elo por superficie.

## Por qué hace falta renderizar el DOM

`player.cgi` no trae las tablas en el HTML: las inyecta desde
`/jsfrags/<Slug>.js`. `parse_ta.py` descarga ese fragmento, lo monta en una
página local y lo renderiza con **Playwright + Chromium headless** antes de
volcar cada tabla a un DataFrame de pandas.

> En entornos donde el proxy de red corta el tráfico HTTPS del navegador, la
> descarga se hace con `curl` (`fetch_ta.sh`) y el render se hace sobre
> `file://`. El resultado es el mismo DOM.

Para las métricas finas se usa `var matchmx` de `player-classic.cgi`: la matriz
cruda de partidos (minutos, aces, dobles faltas, puntos de saque, primeros
dentro/ganados, segundos ganados, juegos al saque, break points salvados y
enfrentados — propios y del rival). Con eso se calculan Hold%, Break%, SPW,
RPW y DR **agregando a nivel de punto/juego**, no promediando ratios.

## Uso

```bash
pip install playwright pandas lxml
./fetch_ta.sh BenjaminBonzi BoticVanDeZandschulp
python3 parse_ta.py     # renderiza el DOM y exporta las tablas a CSV
python3 analiza.py      # bloques de forma, H2H, desgaste, Elo, simulación
python3 analiza2.py     # desglose ATP tour vs Challenger, juegos empíricos, sede
python3 sim_final.py    # simulación punto a punto ajustada por nivel + consenso
```

## Sesgos que corrige el pipeline

- **Nivel de torneo.** Mezclar Challengers con ATP infla Hold% y DR. `analiza2.py`
  separa `level` en tour (A/M/G/F/D) vs Challenger/qualy. Es el ajuste que más
  mueve la aguja en jugadores que bajan a Challenger entre torneos ATP.
- **Superficie.** Se filtra siempre por la superficie del torneo y se usa el Elo
  específico de superficie (hElo/cElo/gElo), no el Elo general ni el ranking.
- **Ventana temporal.** 52 semanas móviles desde la fecha de análisis.
- **Sobre-competitividad del modelo iid.** Un modelo punto a punto independiente
  sobreestima los partidos cerrados (y por tanto los totales de juegos). Los
  totales se publican como mezcla 50/50 entre el modelo y la base empírica.

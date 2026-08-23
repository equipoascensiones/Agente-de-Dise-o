# Análisis MLB — 23 de agosto de 2026

Análisis sabermétrico detallado de los 15 partidos de la jornada. Un archivo por partido,
con abridores, ofensivas, splits de platoon y bullpen desglosados por equipo.

| # | Partido | Hora | Abridores (V / L) |
|---|---|---|---|
| 01 | [Tampa Bay Rays vs Baltimore Orioles](01-tampa-bay-rays-vs-baltimore-orioles.md) | 17:35 UTC | Nick Martinez / Shane Baz |
| 02 | [St. Louis Cardinals vs Philadelphia Phillies](02-st-louis-cardinals-vs-philadelphia-phillies.md) | 17:35 UTC | Kyle Leahy / Cristopher Sánchez |
| 03 | [Toronto Blue Jays vs New York Yankees](03-toronto-blue-jays-vs-new-york-yankees.md) | 17:35 UTC | José Soriano / Carlos Rodón |
| 04 | [Washington Nationals vs Miami Marlins](04-washington-nationals-vs-miami-marlins.md) | 17:40 UTC | Jackson Kent / Janson Junk |
| 05 | [Detroit Tigers vs Kansas City Royals](05-detroit-tigers-vs-kansas-city-royals.md) | 18:10 UTC | Jacob Waguespack / Daniel Lynch IV |
| 06 | [New York Mets vs Chicago White Sox](06-new-york-mets-vs-chicago-white-sox.md) | 18:10 UTC | Nolan McLean / Sean Newcomb |
| 07 | [Athletics vs Houston Astros](07-athletics-vs-houston-astros.md) | 18:10 UTC | Brady Basso / Cristian Javier |
| 08 | [Los Angeles Angels vs Texas Rangers](08-los-angeles-angels-vs-texas-rangers.md) | 18:35 UTC | Yusei Kikuchi / Cal Quantrill |
| 09 | [Cleveland Guardians vs Colorado Rockies](09-cleveland-guardians-vs-colorado-rockies.md) | 19:10 UTC | Foster Griffin / Tomoyuki Sugano |
| 10 | [San Francisco Giants vs Boston Red Sox](10-san-francisco-giants-vs-boston-red-sox.md) | 19:10 UTC | Matt Wilkinson / Jake Bennett |
| 11 | [Pittsburgh Pirates vs Los Angeles Dodgers](11-pittsburgh-pirates-vs-los-angeles-dodgers.md) | 20:10 UTC | Lake Bachar / Blake Snell |
| 12 | [Chicago Cubs vs Seattle Mariners](12-chicago-cubs-vs-seattle-mariners.md) | 20:10 UTC | Shota Imanaga / Bryce Miller |
| 13 | [Minnesota Twins vs San Diego Padres](13-minnesota-twins-vs-san-diego-padres.md) | 20:10 UTC | Bailey Ober / Walker Buehler |
| 14 | [Cincinnati Reds vs Arizona Diamondbacks](14-cincinnati-reds-vs-arizona-diamondbacks.md) | 20:15 UTC | Andrew Abbott / Mitch Bratt |
| 15 | [Atlanta Braves vs Milwaukee Brewers](15-atlanta-braves-vs-milwaukee-brewers.md) | 23:10 UTC | Tyler Mahle / Shane Drohan |

## Métricas incluidas por partido

**Abridores:** FIP · xFIP · K% · BB% · WHIP · K-BB% · ERA · SIERA · Barrel% permitido ·
HardHit% · HR/9 · BABIP · LOB% · WAR · mano (derecho/zurdo)

**Ofensiva:** wOBA · wRC+ · Barrel% · HardHit% · ISO · OPS · K% · BB% ·
**platoon split** contra la mano exacta del abridor rival de hoy

**Bullpen:** FIP · xFIP · ERA · WHIP · SIERA · K% · BB% de temporada ·
FIP de los últimos 30 días · **IP y FIP colectivo de los últimos 3 días** (medida de cansancio)

---

## Glosario de umbrales

| Métrica | Qué mide | Umbral de referencia |
|---|---|---|
| **FIP** | Aísla al lanzador de la defensa: solo ponches, boletos y jonrones | < 3.50 indica dominio |
| **xFIP** | FIP con la tasa de jonrones normalizada a la liga | Si xFIP >> FIP, hay suerte de por medio |
| **K%** | Porcentaje de bateadores ponchados | > 25% es nivel superior |
| **BB%** | Porcentaje de bases por bolas otorgadas | < 7% para evitar aprietos |
| **WHIP** | Corredores permitidos por entrada | < 1.10 es excelente |
| **wOBA** | Pondera cada evento ofensivo por su impacto en carreras | > .340 es ofensiva pesada |
| **wRC+** | Creación de carreras ajustada por parque y época | 100 = promedio; > 115 muy fuerte |
| **Barrel%** | Batazos con ángulo y velocidad de salida óptimos | Media de liga ~7.5% |
| **Platoon split** | Rendimiento del lineup según la mano del abridor rival | Comparado con su línea global |
| **Bullpen 3 días** | IP del relevo en los últimos 3 días + su FIP colectivo | Media de liga: 9.0 IP |

**Referencias de liga (2026):** FIP de bullpen 4.14 · wOBA 0.316 · wRC+ base 100 · IP de bullpen en 3 días 9.0

*Fuente: FanGraphs, temporada 2026. Carga de bullpen y splits calculados sobre el rango 20–22 de agosto.
Los lanzadores cambiados a mitad de temporada figuran con sus totales combinados.*

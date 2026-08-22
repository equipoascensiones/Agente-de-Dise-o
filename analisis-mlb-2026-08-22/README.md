# Análisis MLB — 22 de agosto de 2026

Análisis sabermétrico detallado de los 15 partidos de la jornada. Un archivo por partido,
con abridores, ofensivas, splits de platoon y bullpen desglosados por equipo.

| # | Partido | Hora | Abridores (V / L) |
|---|---|---|---|
| 01 | [Toronto Blue Jays vs New York Yankees](01-toronto-blue-jays-vs-new-york-yankees.md) | 17:35 UTC | Dylan Cease / Ryan Weathers |
| 02 | [Atlanta Braves vs Milwaukee Brewers](02-atlanta-braves-vs-milwaukee-brewers.md) | 18:10 UTC | Martín Pérez / Logan Henderson |
| 03 | [Washington Nationals vs Miami Marlins](03-washington-nationals-vs-miami-marlins.md) | 20:10 UTC | Jake Irvin / Eury Pérez |
| 04 | [St. Louis Cardinals vs Philadelphia Phillies](04-st-louis-cardinals-vs-philadelphia-phillies.md) | 22:05 UTC | Quinn Mathews / Andrew Painter |
| 05 | [Tampa Bay Rays vs Baltimore Orioles](05-tampa-bay-rays-vs-baltimore-orioles.md) | 23:05 UTC | Shane McClanahan / Brandon Young |
| 06 | [Los Angeles Angels vs Texas Rangers](06-los-angeles-angels-vs-texas-rangers.md) | 23:05 UTC | Ryan Johnson / Cody Bradford |
| 07 | [New York Mets vs Chicago White Sox](07-new-york-mets-vs-chicago-white-sox.md) | 23:10 UTC | Christian Scott / Luis Castillo |
| 08 | [Athletics vs Houston Astros](08-athletics-vs-houston-astros.md) | 23:10 UTC | Jacob Lopez / Hunter Brown |
| 09 | [San Francisco Giants vs Boston Red Sox](09-san-francisco-giants-vs-boston-red-sox.md) | 23:15 UTC | Blade Tidwell / Patrick Sandoval |
| 10 | [Detroit Tigers vs Kansas City Royals](10-detroit-tigers-vs-kansas-city-royals.md) | 23:15 UTC | Drew Anderson / Michael Wacha |
| 11 | [Pittsburgh Pirates vs Los Angeles Dodgers](11-pittsburgh-pirates-vs-los-angeles-dodgers.md) | 23:15 UTC | Jared Jones / Tarik Skubal |
| 12 | [Chicago Cubs vs Seattle Mariners](12-chicago-cubs-vs-seattle-mariners.md) | 23:15 UTC | David Peterson / TBD |
| 13 | [Cincinnati Reds vs Arizona Diamondbacks](13-cincinnati-reds-vs-arizona-diamondbacks.md) | 00:10 UTC | Rhett Lowder / Michael Soroka |
| 14 | [Cleveland Guardians vs Colorado Rockies](14-cleveland-guardians-vs-colorado-rockies.md) | 00:10 UTC | Tanner Bibee / Gabriel Hughes |
| 15 | [Minnesota Twins vs San Diego Padres](15-minnesota-twins-vs-san-diego-padres.md) | 00:40 UTC | Dean Kremer / Casey Mize |

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
| **Bullpen 3 días** | IP del relevo en los últimos 3 días + su FIP colectivo | Media de liga: 9.6 IP |

**Referencias de liga (2026):** FIP de bullpen 4.14 · wOBA 0.316 · wRC+ base 100 · IP de bullpen en 3 días 9.6

*Fuente: FanGraphs, temporada 2026. Carga de bullpen y splits calculados sobre el rango 19–21 de agosto.
Los lanzadores cambiados a mitad de temporada figuran con sus totales combinados.*

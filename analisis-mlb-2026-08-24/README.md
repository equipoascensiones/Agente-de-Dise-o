# Análisis MLB — 24 de agosto de 2026

Análisis sabermétrico detallado de los 15 partidos de la jornada. Un archivo por partido,
con abridores, ofensivas, splits de platoon y bullpen desglosados por equipo.

| # | Partido | Hora | Abridores (V / L) |
|---|---|---|---|
| 01 | [Tampa Bay Rays vs Detroit Tigers](01-tampa-bay-rays-vs-detroit-tigers.md) | 22:40 UTC | Drew Rasmussen / Framber Valdez |
| 02 | [Boston Red Sox vs Miami Marlins](02-boston-red-sox-vs-miami-marlins.md) | 22:40 UTC | Ranger Suarez / Sandy Alcantara |
| 03 | [Colorado Rockies vs Washington Nationals](03-colorado-rockies-vs-washington-nationals.md) | 22:45 UTC | Ryan Feltner / Cade Cavalli |
| 04 | [Texas Rangers vs Chicago White Sox](04-texas-rangers-vs-chicago-white-sox.md) | 23:40 UTC | Kumar Rocker / José Urquidy |
| 05 | [Cleveland Guardians vs Los Angeles Angels](05-cleveland-guardians-vs-los-angeles-angels.md) | 01:35 UTC | Parker Messick / George Klassen |
| 06 | [Chicago Cubs vs Arizona Diamondbacks](06-chicago-cubs-vs-arizona-diamondbacks.md) | 01:40 UTC | Kevin Gausman / Merrill Kelly |
| 07 | [Minnesota Twins vs Athletics](07-minnesota-twins-vs-athletics.md) | 01:40 UTC | Zebby Matthews / Jeffrey Springs |
| 08 | [Pittsburgh Pirates vs San Diego Padres](08-pittsburgh-pirates-vs-san-diego-padres.md) | 01:40 UTC | Braxton Ashcraft / Robbie Ray |
| 09 | [Philadelphia Phillies vs Seattle Mariners](09-philadelphia-phillies-vs-seattle-mariners.md) | 01:40 UTC | Zack Wheeler / Logan Gilbert |
| 10 | [Cincinnati Reds vs San Francisco Giants](10-cincinnati-reds-vs-san-francisco-giants.md) | 01:45 UTC | Chase Burns / Carson Whisenhunt |

## Métricas incluidas por partido

**Abridores:** FIP · xFIP · K% · BB% · WHIP · K-BB% · ERA · SIERA · Barrel% permitido ·
HardHit% · HR/9 · BABIP · LOB% · WAR · mano (derecho/zurdo)

**Abridor según la mano del bateador:** AVG / OBP / SLG / **OPS** permitidos, K%, BB%, jonrones,
WHIP, K/9 y BB/9 **contra bateadores zurdos y contra derechos por separado** — en 2026 y en
carrera completa, para distinguir el patrón real del ruido de una temporada

**Historial contra el rival:** juegos, PA, AVG / OBP / SLG / **OPS** permitidos, ponches, boletos
y jonrones **de toda su carrera contra ese equipo**, más el desglose contra los ocho bateadores
que más veces ha enfrentado

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
| **Bullpen 3 días** | IP del relevo en los últimos 3 días + su FIP colectivo | Media de liga: 6.9 IP |

**Referencias de liga (2026):** FIP de bullpen 4.14 · wOBA 0.316 · wRC+ base 100 · IP de bullpen en 3 días 6.9

**Fuentes:** FanGraphs (métricas avanzadas de temporada) y MLB Stats API (splits por mano del
bateador e historial de enfrentamientos). Los splits del abridor por mano y el historial contra el
rival son de **carrera completa**, no solo de 2026.

*Carga de bullpen y splits de ofensiva calculados sobre el rango 21–23 de agosto; los resultados
del 23 aún no estaban publicados, así que la ventana refleja el 21 y 22.
Los lanzadores cambiados a mitad de temporada figuran con sus totales combinados.*

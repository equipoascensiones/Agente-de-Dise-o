#!/usr/bin/env bash
# Descarga las fuentes de Tennis Abstract necesarias para el pipeline.
# Uso: ./fetch_ta.sh <SlugJugador1> [SlugJugador2 ...]
#   ej: ./fetch_ta.sh BenjaminBonzi BoticVanDeZandschulp
set -euo pipefail
BASE="https://www.tennisabstract.com"

# Reporte de Elo por superficie (HTML estatico, la tabla viene inline).
curl -sS --max-time 90 -o elo.html "$BASE/reports/atp_elo_ratings.html"

for slug in "$@"; do
  # Fragmento JS con todas las tablas que player.cgi inyecta en el DOM.
  curl -sS --max-time 90 -o "${slug}.js"        "$BASE/jsfrags/${slug}.js"
  # Pagina classic: trae 'var matchmx' = matriz completa de partidos con stats crudos.
  curl -sS --max-time 90 -o "classic_${slug}.html" "$BASE/cgi-bin/player-classic.cgi?p=${slug}"
done

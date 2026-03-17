#!/usr/bin/env bash
set -e

source .venv-wsl/bin/activate
python -c "import AegeanTools; print('AegeanTools OK')"

INPUT_FITS="$1"
OUTPUT_CSV="$2"

aegean "$INPUT_FITS" --table "$OUTPUT_CSV"
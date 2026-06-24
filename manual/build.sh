#!/usr/bin/env bash
# Build the TypixNode bilingual PDF manual and publish it to the repo root.
#   brew install weasyprint   (or: pipx install weasyprint)
set -euo pipefail
cd "$(dirname "$0")"

python3 build_manual.py
weasyprint manual.html TypixNode_Manual.pdf
cp TypixNode_Manual.pdf ../TypixNode_Manual.pdf
echo "OK -> TypixNode_Manual.pdf (also copied to repo root)"

#!/bin/bash
set -e
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m cmd.rgig --demo

echo "\nRGIG V4 CLI is ready!"
echo "To activate: source .venv/bin/activate"
echo "To run: python -m cmd.rgig --batch"
echo "To use Tab UI: open tab-ui/index.html in your browser." 
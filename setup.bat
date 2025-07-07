@echo off
python -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python -m cmd.rgig --demo

echo RGIG V4 CLI is ready!
echo To activate: call .venv\Scripts\activate
echo To run: python -m cmd.rgig --batch
echo To use Tab UI: open tab-ui/index.html in your browser. 
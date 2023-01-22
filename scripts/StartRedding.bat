@echo off
cd ..
if NOT exist .venv\ (
 python -m venv .venv
 .venv\scripts\activate.bat
 pip install -r requirements.txt
 if NOT exist .venv\Lib\nltk_data\ (
 python -m nltk.downloader -d .venv\Lib\nltk_data popular
)
 python src/main.py -s
) else (
 .venv\scripts\activate.bat
 python src/main.py -s
)

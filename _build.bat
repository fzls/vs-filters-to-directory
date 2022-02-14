python -m venv .venv
call .venv\Scripts\activate

pip install -i https://pypi.doubanio.com/simple pyinstaller wheel
pip install -i https://pypi.doubanio.com/simple -r requirements.txt

pyinstaller --name vs-filters.exe -F main.py

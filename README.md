# Извелечении информации из текста

## Работа с requirements
```
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```

## Запуск web-приложения
```
python3 manage.py runserver
python3 manage.py migrate
```

## Jupyter Notebook
Для более кофортной разработки модулей лучше использовать Jupyter Notebook, из-за более информативной визуализация
```
cd ~/GitHub/analyzedata
export PYTHONPATH="/home/dmitry/GitHub/analyzedata/packages"
jupyter notebook
echo $PYTHONPATH
```

## Virtualenv
python3 -m venv env
source env/bin/activate

## VSCode Python
```
Ctrl+Shift+P
Select Interpreter
```
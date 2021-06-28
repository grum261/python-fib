# Ряд Фибоначчи

## Запуск:
```bash
git clone https://github.com/grum261/python-fib
cd python-fib
docker-compose up
```

## Без докера:
```bash
git clone https://github.com/grum261/python-fib
cd python-fib
sudo apt install pipenv
pipenv install
./manage runserver
```

## Запросы:
Получение списка задач:
```bash
curl -X GET -H "Accept: application/json" http://127.0.0.1:8000/fibonacci
```

Расчет ряда Фибоначчи до n:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"n": 10}' http://127.0.0.1:8000/fibonacci
```

Получение информации о задаче по uuid:
```bash
curl -X GET -H "Accept: application/json" http://127.0.0.1:8000/fibonacci/task/1516b57f-af40-4256-9d58-09d5edc20d59
```
# ДЗ Тема: Основи Web. Побудова простого HTTP сервера.

Створіть віртуальне оточення то встановіть необхідні бібліотеки

```bash
python3 -m venv venv
```
```bash
pip install -r requirements.txt
```

```bash
docker build -t flask-app .
```

Запуск:

```bash 
docker run -d -p 3000:3000 -v $(pwd)/storage:/app/storage flask-app
```

Вебсайт буде доступний за адресою
```bash
http://localhost:3000/
```
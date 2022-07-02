# Бот проверки цены криптовалюты с GoinGecko написанный на Python

### Как запустить?

1. Установить Python: https://www.python.org/downloads/
2. Скачать проект из github и открыть в IDE (например, VSCode)
3. Указать API-КЛЮЧ бота, полученный из BotFather в файл .env
4. Установить требуемые библиотеки ```pip install -r requirements.txt```
6. Запускать командой ```python main.py```

### Как запустить через Docker ?

1. Скачать проект из github и перейти в папку
2. Собрать образ из Dockerfile командой ```docker build -t crypto_bot .```
3. Запустить образ командой ```docker run --rm --name crypto_bot crypto_bot```

### Дополнительно (Docker)
Посмотреть все запущенные контейнеры ```docker ps```

Остановить контейнер ```docker stop crypto_bot```

Удалить контейнер ```docker image rm crypto_bot```

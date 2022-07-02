FROM python:3

COPY . ./crypto_bot
WORKDIR ./crypto_bot

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
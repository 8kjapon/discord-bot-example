FROM python:3.12.8

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /discord-bot
COPY . /discord-bot/

RUN pip install --no-cache-dir -r requirements.txt
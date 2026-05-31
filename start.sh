#!/bin/bash
# Arranca la web y el bot en background
cd "$(dirname "$0")"

echo "Iniciando GangaViaje web (puerto 5002)..."
nohup python3 app.py >> web.log 2>&1 &
echo "Web PID: $!"

echo "Iniciando GangaViaje bot..."
nohup python3 bot.py >> bot.log 2>&1 &
echo "Bot PID: $!"

echo "Listo. Logs: web.log / bot.log"

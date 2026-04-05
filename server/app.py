from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
import json
import os
import cv2
import numpy as np

app = Flask(__name__)

# Criar pasta
if not os.path.exists("dados"):
    os.makedirs("dados")

# Criar banco
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id TEXT PRIMARY KEY,
            sensor_id TEXT,
            temperatura REAL,
            status_logico TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()


def processar(temp):
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    if temp > 15:
        cv2.putText(img, "CRITICO", (5,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        return "Crítico"
    elif temp > 10:
        cv2.putText(img, "ALERTA", (5,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)
        return "Alerta"
    else:
        cv2.putText(img, "NORMAL", (5,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        return "Normal"

@app.route('/sensor', methods=['POST'])
def receber():
    data = request.json

    uuid = data['id']
    sensor_id = data['sensor_id']
    temp = data['temperatura']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM leituras WHERE id = ?", (uuid,))
    if c.fetchone():
        conn.close()
        return jsonify({"status": "duplicado"})

    status = processar(temp)
    timestamp = datetime.now().isoformat()

    c.execute('''
        INSERT INTO leituras (id, sensor_id, temperatura, status_logico, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (uuid, sensor_id, temp, status, timestamp))

    conn.commit()
    conn.close()

    with open(f"dados/{uuid}.json", "w") as f:
        json.dump({
            "id": uuid,
            "sensor_id": sensor_id,
            "temperatura": temp,
            "status": status,
            "timestamp": timestamp
        }, f, indent=4)

    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
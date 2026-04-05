import tkinter as tk
import requests
import uuid
import random

# TROCAR PELO IP DO SERVIDOR
URL = "http://192.168.0.107:5000/sensor"

historico = []

def enviar():
    temp = round(random.uniform(-10, 40), 2)
    uid = str(uuid.uuid4())

    data = {
        "id": uid,
        "sensor_id": "sensor_01",
        "temperatura": temp
    }

    try:
        r = requests.post(URL, json=data)
        status = r.json()["status"]

        label.config(text=f"Status: {status}")
        historico.append(f"{temp}°C -> {status}")
        atualizar()

    except:
        label.config(text="Erro de conexão")

def atualizar():
    lista.delete(0, tk.END)
    for item in historico[-10:]:
        lista.insert(tk.END, item)

root = tk.Tk()
root.title("Sensor Cliente")

tk.Button(root, text="Enviar Leitura", command=enviar).pack(pady=10)
label = tk.Label(root, text="Status:")
label.pack()

lista = tk.Listbox(root, width=40)
lista.pack(pady=10)

root.mainloop()
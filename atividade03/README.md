<<<<<<< HEAD
# Sistema Cliente/Servidor em Camadas

## 📌 Descrição

Este projeto implementa um sistema distribuído em três camadas para
simulação de sensores de temperatura.

## 🏗️ Arquitetura

-   Cliente (Tkinter)
-   Servidor (Flask + OpenCV)
-   Banco de Dados (SQLite)

## 🔄 Fluxo de Funcionamento

1.  Cliente gera temperatura + UUID\
2.  Envia JSON via HTTP\
3.  Servidor valida UUID\
4.  Aplica lógica (Normal, Alerta, Crítico)\
5.  Salva no SQLite\
6.  Salva JSON em disco\
7.  Retorna status ao cliente

## ⚙️ Pré-requisitos

-   Python 3
-   Dois computadores na mesma rede

## 🚀 Execução

### 🖥️ Servidor

``` bash
cd server
pip install flask opencv-python numpy
python app.py
```

### 🌐 Descobrir IP

``` bash
ipconfig
```

### 💻 Cliente

Editar URL no client.py:

``` python
URL = "http://IP_DO_SERVIDOR:5000/sensor"
```

Instalar e rodar:

``` bash
cd client
pip install requests
python client.py
```

## 📁 Saídas

-   database.db
-   pasta dados/ com arquivos JSON


=======
# Atividade03SD
Atividade 03 da disciplina de Sistemas Distribuidos
>>>>>>> b43dec6bc8080a52ce374cc4c1b9e93da47c136a

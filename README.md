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

Video de teste: https://github-production-user-asset-6210df.s3.amazonaws.com/120272721/573961516-98168f4c-2644-4e36-8233-2b4e08374425.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260405%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260405T235015Z&X-Amz-Expires=300&X-Amz-Signature=074541a1e720c1aafc81c5f89c7d9f91bb7258ed3cef46c07514b77e27c536f4&X-Amz-SignedHeaders=host

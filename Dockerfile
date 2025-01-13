FROM python:3.10.9-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Copiar os arquivos necessários para o container
COPY requirements.txt runtime.txt /app/
COPY src /app/src

# Instalar dependências do Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Expor a porta padrão do Uvicorn
EXPOSE 8020

# Comando para iniciar o serviço FastAPI
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8020"]

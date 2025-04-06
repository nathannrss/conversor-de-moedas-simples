# imagem leve do python
FROM python:3.12-slim

# definir o diretorio de trabalho no container
WORKDIR /app

# copiar as dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia o script principal main.py
COPY main.py .

# rodar o programa no terminal
CMD ["python", "main.py"]

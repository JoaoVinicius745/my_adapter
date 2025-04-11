# Base Python
FROM python:3.13
# Diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta onde o FastAPI/Uvicorn irá rodar
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "output.ragflow:app", "--host", "0.0.0.0", "--port", "8000"]

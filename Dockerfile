# Use a imagem oficial do Python como base
FROM python:3.10-slim

# Configure o diretório de trabalho
WORKDIR /app

# Copie o script do servidor para o contêiner
COPY simple.py .

# Exponha a porta 80 para o servidor
EXPOSE 80

# Comando para rodar o servidor
CMD ["python", "simple.py"]

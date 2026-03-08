 # 1. Escolhemos a imagem base do Python
FROM python:3.11-slim

# 2. Definimos onde o código vai morar dentro do container
WORKDIR /app

# 3. Copiamos a pasta 'src' para dentro da pasta 'app' no container
COPY src/ ./src/

# 4. Comando para rodar o projeto (ainda vamos criar o main.py!)
CMD ["python", "src/main.py"]
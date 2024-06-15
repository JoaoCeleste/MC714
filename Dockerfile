# Usar uma imagem base do Python
FROM python:3.9-slim

# Instalar pacotes necessários
RUN apt-get update && apt-get install -y \
    build-essential \
    openmpi-bin \
    libopenmpi-dev

# Instalar mpi4py
RUN pip install mpi4py

# Criar um diretório de trabalho
WORKDIR /usr/src/app

# Copiar o código-fonte para o contêiner
COPY . .

# Comando padrão para executar o contêiner
CMD ["mpirun", "--allow-run-as-root", "-np", "3", "python", "script.py"]

FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    openmpi-bin \
    openmpi-common \
    libopenmpi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install mpi4py

# Criar um usuário não-root
RUN useradd -m mpiuser
USER mpiuser

WORKDIR /app

COPY . /app

CMD ["mpirun", "-np", "4", "python", "leader_election.py"]

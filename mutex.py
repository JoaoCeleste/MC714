from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def request_critical_section(rank):
    print(f"Processo {rank} solicitando seção crítica")
    for i in range(size):
        if i != rank:
            comm.send(rank, dest=i, tag=0)
    acks = 0
    while acks < size - 1:
        data = comm.recv(tag=0)
        acks += 1
        print(f"Processo {rank} recebeu ACK de {data}")

def release_critical_section(rank):
    print(f"Processo {rank} liberando seção crítica")
    for i in range(size):
        if i != rank:
            comm.send(rank, dest=i, tag=1)

if __name__ == "__main__":
    time.sleep(rank)
    request_critical_section(rank)
    print(f"Processo {rank} está na seção crítica")
    time.sleep(2)
    release_critical_section(rank)

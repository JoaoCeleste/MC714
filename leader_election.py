from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def leader_election():
    print(f"Processo {rank} iniciou a eleição")
    leader = rank
    for i in range(size):
        if i != rank:
            comm.send(rank, dest=i, tag=0)
    for i in range(size - 1):
        candidate = comm.recv(tag=0)
        if candidate > leader:
            leader = candidate
    return leader

if __name__ == "__main__":
    random.seed(rank)
    leader = leader_election()
    print(f"Processo {rank} elegeu o líder {leader}")

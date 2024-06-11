from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ELECTION = 1
LEADER = 2

def main():
    if rank == 0:
        # Processo 0 inicia a eleição com um líder aleatório
        leader = random.randint(0, size - 1)
        print(f"Process {rank} starting leader election with initial leader {leader}")
        # Processo 0 envia a mensagem de eleição para todos os processos
        for i in range(size):
            if i != rank:
                comm.isend((ELECTION, leader), dest=i, tag=ELECTION)
    
    leader = None
    while True:
        # Recebe mensagens de outros processos
        status = MPI.Status()
        msg = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        tag = status.Get_tag()
        
        if tag == ELECTION:
            # Recebe a mensagem de eleição e retransmite como mensagem de liderança
            _, proposed_leader = msg
            print(f"Process {rank} received ELECTION with proposed leader {proposed_leader}")
            leader = proposed_leader
            for i in range(size):
                if i != rank:
                    comm.isend((LEADER, leader), dest=i, tag=LEADER)
        elif tag == LEADER:
            # Recebe a mensagem de liderança e reconhece o líder
            _, leader = msg
            print(f"Process {rank} acknowledges leader {leader}")
            break
    
    # Garante que todos os processos cheguem ao ponto de saída ao mesmo tempo
    comm.barrier()
    print(f"Process {rank} exiting with leader {leader}")

if __name__ == "__main__":
    main()

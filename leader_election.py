from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ELECTION = 1
LEADER = 2

def main():
    if rank == 0:
        # Process 0 starts the leader election with a random leader
        leader = random.randint(0, size - 1)
        print(f"Process {rank} starting leader election with initial leader {leader}")
        # Process 0 sends election message to all other processes
        for i in range(size):
            if i != rank:
                comm.isend((ELECTION, leader), dest=i, tag=ELECTION)
    
    leader = None
    while True:
        # Receive messages from other processes
        status = MPI.Status()
        msg = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        tag = status.Get_tag()
        
        if tag == ELECTION:
            # Receive election message and forward as leader message
            _, proposed_leader = msg
            print(f"Process {rank} received ELECTION with proposed leader {proposed_leader}")
            leader = proposed_leader
            for i in range(size):
                if i != rank:
                    comm.isend((LEADER, leader), dest=i, tag=LEADER)
        elif tag == LEADER:
            # Receive leader message and acknowledge the leader
            _, leader = msg
            print(f"Process {rank} acknowledges leader {leader}")
            break
    
    # Ensure all processes reach the exit point at the same time
    comm.barrier()
    print(f"Process {rank} exiting with leader {leader}")

if __name__ == "__main__":
    main()

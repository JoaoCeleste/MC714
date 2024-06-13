from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

REQUEST = 1
GRANT = 2
RELEASE = 3

# Function to request entry to the critical section
def request_entry():
    print(f"Process {rank} requesting entry to critical section")
    for i in range(size):
        if i != rank:
            comm.send((REQUEST, rank), dest=i)

# Function to handle incoming messages
def handle_message():
    status = MPI.Status()
    while True:
        msg = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        tag = status.Get_tag()
        src = status.Get_source()
        
        if tag == REQUEST:
            comm.send((GRANT, rank), dest=src)
        elif tag == GRANT:
            print(f"Process {rank} received GRANT from Process {src}")
        elif tag == RELEASE:
            print(f"Process {rank} received RELEASE from Process {src}")

# Main function
if __name__ == "__main__":
    if rank == 0:
        request_entry()
        handle_message()
        print(f"Process {rank} entering critical section")
        # Simulate critical section
        handle_message()
        for i in range(size):
            if i != rank:
                comm.send((RELEASE, rank), dest=i)
        print(f"Process {rank} leaving critical section")
    else:
        handle_message()

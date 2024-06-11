from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def critical_section():
    print(f"Process {rank} entering critical section")
    time.sleep(2)  # Simulate critical section
    print(f"Process {rank} leaving critical section")

def handle_message():
    status = MPI.Status()
    msg = comm.recv(source=MPI.ANY_SOURCE, status=status)
    source = status.Get_source()
    
    if msg == "REQUEST":
        print(f"Process {rank} received REQUEST from Process {source}")
        comm.send("GRANT", dest=source)
    elif msg == "GRANT":
        print(f"Process {rank} received GRANT from Process {source}")
    elif msg == "RELEASE":
        print(f"Process {rank} received RELEASE from Process {source}")
    elif msg == "TERMINATE":
        print(f"Process {rank} received TERMINATE from Process {source}")
        return False  # Indicate to stop receiving messages
    return True  # Indicate to continue receiving messages

def main():
    if rank == 0:
        # Process 0 requests critical section access
        comm.send("REQUEST", dest=1)
        handle_message()  # Wait for GRANT
        
        critical_section()
        
        comm.send("RELEASE", dest=1)
        comm.send("TERMINATE", dest=1)  # Signal termination
    elif rank == 1:
        # Process 1 handles the messages
        running = True
        while running:
            running = handle_message()

if __name__ == "__main__":
    main()

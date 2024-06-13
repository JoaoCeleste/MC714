from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Initialize the Lamport clock for each process
lamport_clock = 0

def send_message(destination):
    global lamport_clock
    lamport_clock += 1  # Increment clock before sending
    comm.send(lamport_clock, dest=destination)
    print(f"Process {rank} sending message to Process {destination} with clock {lamport_clock}")

def receive_message():
    global lamport_clock
    message = comm.recv(source=MPI.ANY_SOURCE)
    lamport_clock = max(lamport_clock, message) + 1  # Update clock after receiving
    print(f"Process {rank} received message: Message from {message}")

if __name__ == "__main__":
    if rank == 0:
        send_message(1)
        receive_message()
    elif rank == 1:
        receive_message()
        send_message(0)

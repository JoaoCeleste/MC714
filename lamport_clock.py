from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

lamport_clock = 0

def send_message(dest):
    global lamport_clock
    lamport_clock += 1
    message = (lamport_clock, f"Message from {rank}")
    comm.send(message, dest=dest)
    print(f"Process {rank} sending message to Process {dest} with clock {lamport_clock}")

def receive_message():
    global lamport_clock
    message = comm.recv()
    lamport_clock = max(lamport_clock, message[0]) + 1
    print(f"Process {rank} received message: {message[1]} with clock {message[0]}")

if rank == 0:
    send_message(1)
    receive_message()
elif rank == 1:
    receive_message()
    send_message(0)

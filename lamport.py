from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

clock = 0

def send_message(clock, rank, dest):
    comm.send(clock, dest=dest, tag=0)
    print(f"Processo {rank} enviou mensagem com timestamp {clock} para o processo {dest}")

def receive_message(clock, rank, src):
    recv_clock = comm.recv(source=src, tag=0)
    clock = max(clock, recv_clock) + 1
    print(f"Processo {rank} recebeu mensagem com timestamp {recv_clock} do processo {src} e atualizou seu relógio para {clock}")
    return clock

if size < 3:
    print("É necessário pelo menos 3 processos para executar este programa")
    sys.exit(0)
else:
    comm.Barrier()  # Sincronizar todos os processos antes de iniciar
    # Simular eventos e troca de mensagens
    if rank == 0:
        clock += 1
        send_message(clock, rank, 1)
        clock += 1
        send_message(clock, rank, 2)
        clock = receive_message(clock, rank, 1)
    elif rank == 1:
        clock = receive_message(clock, rank, 0)
        clock += 1
        send_message(clock, rank, 2)
        clock = receive_message(clock, rank, 2)
    elif rank == 2:
        clock = receive_message(clock, rank, 0)
        clock = receive_message(clock, rank, 1)
        clock += 1
        send_message(clock, rank, 1)

    comm.Barrier()  # Sincronizar todos os processos antes de finalizar
    print(f"Processo {rank} terminou com sucesso")

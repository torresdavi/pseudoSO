from Modules.Memory.memory import Memory
from Modules.Process.process import Process
from Modules.Process.manager import process_manager
from Modules.Queue.queue import Queue
from Modules.Reader.reader import read_file


print("Início")
print("Leitura dos processos")
processes = read_file()
print("Processos lidos.")
print("Alocando a memória.")
memory = Memory()
print("Memória alocada.")
print("Criando fila.")
queue = Queue()
print("Fila criada.")

queue.initial_time(processes, memory)

process_manager(queue, memory)
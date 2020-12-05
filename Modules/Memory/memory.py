from Modules.Process.process import Process;

class Memory:
    def __init__(self):
        self.tamanho = [0]*1024 # Tamanho da memória é 1024
        self.offset_user = 64 # a partir do 64 é processo de usuário
        self.offset_nucleo = 0 # de 0 até o 64 é processo de núcleo


    def __validate_process_type(self, priority):
        # flag para caso seja um processo de núcleo, retornará true
        if (priority == 0):
            return true
        else
            return false

    def alocate_memory(self, PID, length)
           
from Modules.Process.process import Process;

class Memory:
    def __init__(self):
        self.memory_block = [None]*1024 # Tamanho da memória é 1024x
        self.offset_user = 64 # a partir do 64 é processo de usuário
        self.offset_kernel = 0 # de 0 até o 64 é processo de núcleo
        self.id = 0 # id do processo
        
    def __validate_process_kernel(self, priority):
        # flag para caso seja um processo de núcleo, retornará true
        if (priority == 0):
            return True
        else:
            return False

    def __validate_process_length(self, process):
        if (self.__validate_process_kernel(process_priority) and process.process_length < 64):
            return True
        elif (not self.__validate_process_kernel(process_priority) and 64 < process.process_length <= 1024):
            return True
        else:
            return False


    def alocate_memory(self, process):
        
        process.PID = self.id 
        if (self.__validate_process_kernel(process.priority) and process.process_length <= 64):
            for i in range(self.offset_kernel, (self.offset_kernel + process.process_length)):
                self.memory_block[i] = process.PID
            self.offset_kernel += process.process_length                #Atualizando o offset do núcleo
        else:
            for i in range(self.offset_user , (self.offset_user + process.process_length)):
                self.memory_block[i] = process.PID
            self.offset_user += process.process_length                  #Atualizando o offset do usuário
        self.id += 1

    #def dealocate_memory (self, process):
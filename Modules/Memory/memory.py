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
        
        if (process.instruction == 1 ):
            process.PID = self.id 
            self.id += 1
        if (self.__validate_process_kernel(process.priority) and process.process_length <= 64):
            if ((self.memory_block[0] != None) and ((self.offset_kernel + process.process_length ) > 64 )):  #Verifica se ha processo alocado na memoria (kernel)
                print("Nao ha espaço para alocacao na memoria para o processo.")
            else:
                for i in range(self.offset_kernel, (self.offset_kernel + process.process_length)):
                    self.memory_block[i] = process.PID
            
            process.own_offset = self.offset_kernel                       #Passando o offset pra sabermos a localização do processo na memória
            self.offset_kernel += process.process_length                #Atualizando o offset do núcleo
        else:
            #validar se o processo usuario tem no máximo 960mb
            for i in range(self.offset_user , (self.offset_user + process.process_length)):
                self.memory_block[i] = process.PID
            process.own_offset = self.offset_user                #Atualizando o offset do usuário
            self.offset_user += process.process_length
        return (process)

    def dealocate_memory (self, process):
        
        # Percorre do offset até o final do processo e retira o processo da memória
        for i in range(process.own_offset, (process.own_offset + (process.process_length))):
            self.memory_block[i] = None
            
        self.offset_kernel = process.own_offset

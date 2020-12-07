#from Modules.Memory.memory import Memory;

class Queue:
    def __init__(self):
        self.kernel_queue = [] #fila de tempo real
        self.user1_queue = [] #fila de processos prioridade 1
        self.user2_queue = [] #fila de processos prioridade 2
        self.user3_queue = [] #fila de processos prioridade 3


    def insert_process(self, process, memory): #insercao de processo nas filas de prioridade
        if ((len(self.kernel_queue) + len(self.user1_queue) + len(self.user2_queue) + len(self.user3_queue)) <= 1000):
            if(process.priority == 0):
                if(process.instruction == 1):
                    memory.alocate_memory(process)
                self.kernel_queue.append(process)

            elif (process.priority == 1):
                if(process.instruction == 1):
                    memory.alocate_memory(process)
                self.user1_queue.append(process)
            elif (process.priority == 2):
                if(process.instruction == 1):
                    memory.alocate_memory(process)
                self.user2_queue.append(process)
            elif (process.priority == 3):
                if(process.instruction == 1):
                    memory.alocate_memory(process)
                self.user3_queue.append(process)
        
        else:
            print("A fila está cheia.")

    def update_priority(self):    #funcao definida para atualizacao constante da fila de prioridades
        self.user1_queue.extend(self.user2_queue)
        self.user2_queue = []
        self.user2_queue.extend(self.user3_queue)
        self.user3_queue = []

        
    def remove_process(self):    #remocao dos processos das filas de prioridade
        if (self.kernel_queue):   
            pop_queue = self.kernel_queue.pop()
        elif(self.user1_queue):
            pop_queue = self.user1_queue.pop()
        elif(self.user2_queue):
            pop_queue = self.user2_queue.pop()
        elif(self.user3_queue):
            pop_queue = self.user3_queue.pop()
        else:
            return 0
        self.update_priority()
        return pop_queue

    def initial_time(self, processes, memory): #funcao que ordena os processos por tempo de processador para execucao
        processes.sort(key=lambda x: x.time_init, reverse=True)
        for process in processes:
            self.insert_process(process,memory)
        


            
    
    
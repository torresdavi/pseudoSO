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
                if(memory.alocate_memory(process)):
                    self.kernel_queue.append(process)
                    print("\nKernel: ")
                    print(self.kernel_queue)
            elif (process.priority == 1):
                if (memory.alocate_memory(process)):
                    self.user1_queue.append(process)
                    print("\nUser1: ")
                    print(self.user1_queue)
            elif (process.priority == 2):
                if (memory.alocate_memory(process)):
                    self.user2_queue.append(process)
                    print("\nUser2:")
                    print(self.user2_queue)  
            elif (process.priority == 3):
                if (memory.alocate_memory(process)):
                    self.user3_queue.append(process)
                    print("\n User3:")
                    print(self.user3_queue)
        
        else:
            print("A fila está cheia.")

    def update_priority(self):
        self.user1_queue.extend(self.user2_queue)
        self.user2_queue = []
        self.user2_queue.extend(self.user3_queue)
        self.user3_queue = []

        
    def remove_process(self):    #remocao dos processos das filas de prioridade
        if (self.kernel_queue is not None):   
            pop_queue = self.kernel_queue.pop()
        elif(self.user1_queue is not None):
            pop_queue = self.user1_queue.pop()
        elif(self.user2_queue is not None):
            pop_queue = self.user2_queue.pop()
        elif(self.user3_queue is not None):
            pop_queue = self.user3_queue.pop()
        self.update_priority()
        
        return pop_queue
        
    
    
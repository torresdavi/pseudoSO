#from Modules.Memory.memory import Memory;

class Queue:
    def __init__(self):
        # self.kernel_queue = [] #fila de tempo real
        self.main_queue = [[], []] #fila de processos


    def insert_process(self, process, memory):
        if (len(self.main_queue) <= 1000):
                if (memory.alocate_memory(process)):
                    self.main_queue.append([process.priority], [process.PID])

                print(self.main_queue)
        else:
            print("A fila está cheia.")
        # Olhar dps
    
    #def remove_process(self):
        
    
    #def update_priority(self):
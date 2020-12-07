import time
import threading


def execute_process_kernel(process, CPU, memory):
    CPU.acquire()
    print("P" + str(process.PID) + " STARTED")
    for instruction in range(1, process.time_process + 1):
        print("P" + str(process.PID) + " instruction" + str(process.instruction))
        time.sleep(1)
        process.instruction += 1
    print("P" + str(process.PID) + " return SIGINT")
    memory.dealocate_memory(process)
    CPU.release()


def execute_process_user(process, CPU, memory):
    CPU.acquire()
    # se ultrapassar 1 quantum ele chama o próximo processo (desaloca o processo atual do processador e chama o próximo)
    if (process.instruction == 1):
        print("P" + str(process.PID) + " STARTED")
        print("P" + str(process.PID) + " instruction" + str(process.instruction))
    elif (process.instruction == process.time_process):
        print("P" + str(process.PID) + " instruction" + str(process.instruction))
        print("P" + str(process.PID) + " return SIGINT")
        memory.dealocate_memory(process)
    else:
        print("P" + str(process.PID) + " instruction" + str(process.instruction))

    process.instruction += 1
    time.sleep(1)
    CPU.release()


def process_manager(queue, memory):  # gerenciador de processos
    CPU = threading.Lock()
    while (True):
        if not CPU.locked():
            process = queue.remove_process()
            if(process == 0):  # verificacao de processos para usuario ou kernel
                break
            if(process.priority == 0):
                thread = threading.Thread(target=execute_process_kernel, args=(
                    process, CPU, memory, ))  # starta a thread para processos de nucleo
                thread.start()
            else:
                thread = threading.Thread(target=execute_process_user, args=(
                    process, CPU, memory, ))  # starta a thread para processos de usuario
                thread.start()
                if (process.instruction != process.time_process):
                    queue.insert_process(process, memory)

from Modules.Process.process import Process;

def read_file():
    # Lista de processos
    processes_array = []

    # with open("Arquivos/files.txt", "r") as file:
    #     file.
    #print(file)

    # Leitura do arquivo de processos, armazenamento em array e instanciamento da classe Process
    # Armazenamos os processos em um array de processos
    with open("Arquivos/processes.txt", "r") as processes:
        for row in processes:
            process_attributes = row.split(", ")
            if (row == 0 and process_attributes[-1] == '\n'):
                process = Process(process_attributes)
                process.pop(-1)
            else:
                process = Process(process_attributes)
            processes_array.append(process)
            
return (processes_array)

class Process:

        # Construtor pra instanciar o processo com os valores recebidos/lidos
    def __init__(self, process_array):
        self.time_init = int(process_array[0])
        self.priority = int(process_array[1])
        self.time_process = int(process_array[2])
        self.process_length = int(process_array[3])
        self.printer_request = int(process_array[4])
        self.scanner_request = int(process_array[5])
        self.modem_request = int(process_array[6])
        self.disk_request = int(process_array[7]) 

    
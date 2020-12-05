class Memory:
    def __init__(self):
        self.tamanho = [0]*1024 # Tamanho da memória é 1024
        self.offset_user = 64 # a partir do 64 é processo de usuário
        self.offset_nucleo = 0 # de 0 até o 64 é processo de núcleo



    
    def __valida_tipo_processo(self,  ):
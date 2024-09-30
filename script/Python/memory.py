import random

# Simulação de RAM (memória física) e Swap (memória virtual)
class MemoryManager:
    def __init__(self, ram_size, swap_size):
        self.ram_size = ram_size
        self.swap_size = swap_size
        self.ram = []
        self.swap = []
        self.page_table = {}

    def add_process(self, process_name):
        if len(self.ram) < self.ram_size:
            print(f'Carregando {process_name} na RAM.')
            self.ram.append(process_name)
            self.page_table[process_name] = 'RAM'
        else:
            print(f'RAM cheia! {process_name} movido para o Swap (Memória Virtual).')
            self.swap.append(process_name)
            self.page_table[process_name] = 'Swap'

    def access_process(self, process_name):
        if process_name in self.ram:
            print(f'{process_name} já está na RAM.')
        elif process_name in self.swap:
            print(f'Falha de Página! {process_name} está no Swap.')
            self.swap.remove(process_name)
            if len(self.ram) < self.ram_size:
                print(f'Carregando {process_name} para a RAM.')
                self.ram.append(process_name)
                self.page_table[process_name] = 'RAM'
            else:
                page_to_remove = random.choice(self.ram)
                print(f'Removendo {page_to_remove} da RAM e movendo para o Swap.')
                self.ram.remove(page_to_remove)
                self.swap.append(page_to_remove)
                self.page_table[page_to_remove] = 'Swap'
                print(f'Carregando {process_name} para a RAM.')
                self.ram.append(process_name)
                self.page_table[process_name] = 'RAM'
        else:
            print(f'{process_name} não está em nenhum lugar.')

    def display_memory(self):
        print(f'\nRAM: {self.ram}')
        print(f'Swap: {self.swap}')
        print(f'Tabela de Páginas: {self.page_table}')

ram_size = 3  # Capacidade máxima da RAM
swap_size = 5  # Capacidade máxima do Swap

manager = MemoryManager(ram_size, swap_size)

manager.add_process('Sistema Operacional')
manager.add_process('Navegador Web')
manager.add_process('Editor de Texto')
manager.add_process('Banco de Dados')

manager.access_process('Navegador Web')  # Já está na RAM
manager.access_process('Banco de Dados')  # Falha de Página (Swap -> RAM)
manager.access_process('Editor de Texto')  # Já está na RAM

manager.display_memory()

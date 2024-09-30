import psutil
import os

def memory_usage():
    # Função que retorna o uso de memória em MB do processo atual
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 2)  # Convertendo para MB

def consume_memory(size_in_gb):
    big_list = []

    # Simula o consumo de memória (cada número inteiro ocupa 28 bytes em média no Python)
    target_size = size_in_gb * (1024 ** 3)  # Converte GB para bytes

    print(f"Consumindo {size_in_gb} GB de memória...")

    while memory_usage() < size_in_gb * 1024:  # Continua até atingir o tamanho desejado em MB
        big_list.extend(range(10**6))  # Adiciona mais itens

    print(f"Memória consumida: {memory_usage():.2f} MB")

# Consumir 4 GB de memória como exemplo
consume_memory(4)

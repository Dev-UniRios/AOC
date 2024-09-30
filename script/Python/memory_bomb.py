import psutil
import os

def memory_usage():
    # Função que retorna o uso de memória em MB do processo atual
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 2)  # Convertendo para MB

def consume_memory(target_size_gb):
    big_list = []
    
    # Converte o tamanho desejado para MB
    target_size_mb = target_size_gb * 1024

    print(f"Objetivo: Consumir {target_size_gb} GB ({target_size_mb} MB) de memória...")

    while memory_usage() < target_size_mb:
        big_list.extend(range(10**6))  # Adiciona 1 milhão de inteiros (cada inteiro ~28 bytes)

        # A cada iteração, mostra o consumo de memória até atingir o valor desejado
        print(f"Memória consumida até agora: {memory_usage():.2f} MB")

    print(f"Memória final consumida: {memory_usage():.2f} MB")

# 🧨 CUIDADO!!🧨
# Consumir 4 GB de memória como exemplo, mas pode causar travamento do sistema.
consume_memory(4)

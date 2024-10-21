import concurrent.futures
import time

# Função que aplica uma operação em cada dado
def processar(valor):
    return valor * 2

# Dados para processamento MIMD
dados = [1, 2, 3, 4, 5]
start_time = time.time()

# Aplicando diferentes instruções em diferentes dados usando multithreading
with concurrent.futures.ThreadPoolExecutor() as executor:
    resultados = list(executor.map(processar, dados))

print(f"Resultado MIMD: {resultados}")
print(f"Tempo de execução MIMD: {time.time() - start_time:.4f} segundos")

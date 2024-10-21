from multiprocessing.pool import Pool
import time

# Função que simula um processamento pesado
def processar_dados(dado):
    time.sleep(1)  # Simulando processamento
    return dado * 2

if __name__ == '__main__':
    dados = [1, 2, 3, 4, 5]
    start_time = time.time()

    # Criando um pool de processos para processar os dados em paralelo
    with Pool(5) as pool:
        resultados = pool.map(processar_dados, dados)

    print(f"Resultados: {resultados}")
    print(f"Tempo de execução distribuído: {time.time() - start_time:.4f} segundos")

import numpy as np
import time

# Dados para processamento SIMD
vetor = np.array([1, 2, 3, 4, 5])
start_time = time.time()

# Aplicando uma única instrução em múltiplos dados
resultado = vetor * 2

print(f"Resultado SIMD: {resultado}")
print(f"Tempo de execução SIMD: {time.time() - start_time:.4f} segundos")

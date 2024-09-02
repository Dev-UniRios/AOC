import time

# Simulador de Arquiteturas RISC e CISC com Núcleo Único, Multinúcleo e Hyper-Threading

class SimuladorCPU:
    def __init__(self):
        self.registradores = [0] * 8  # Registradores R0 a R7
        self.resultados = []  # Lista para armazenar os resultados de tempo

    def executar_instrucoes_RISC(self):
        start_time = time.time()  # Inicia a medição do tempo
        print("Executando instruções em arquitetura RISC (núcleo único)...")
        
        # Repetir as instruções para simular carga de trabalho
        for _ in range(100000):  # Aumente ou diminua o número para ajustar a carga
            self.registradores[0] = 10  # Load valor em R0
            self.registradores[1] = 20  # Load valor em R1
            self.registradores[2] = self.registradores[0] + self.registradores[1]  # ADD R0, R1 -> R2
            self.registradores[3] = self.registradores[2] - 5  # SUB R2, 5 -> R3

        end_time = time.time()  # Finaliza a medição do tempo
        tempo_execucao = end_time - start_time
        print(f"Tempo de execução para RISC: {tempo_execucao:.6f} segundos")
        self.resultados.append(("RISC", tempo_execucao))
        input("Pressione Enter para continuar...")

    def executar_instrucoes_CISC(self):
        start_time = time.time()  # Inicia a medição do tempo
        print("Executando instruções em arquitetura CISC (núcleo único)...")
        
        # Repetir as instruções para simular carga de trabalho
        for _ in range(100000):  # Aumente ou diminua o número para ajustar a carga
            self.registradores[0] = 10  # Load valor em R0
            self.registradores[1] = 20  # Load valor em R1
            self.registradores[3] = (self.registradores[0] + self.registradores[1]) - 5  # ADD R0, R1, SUB 5 -> R3

        end_time = time.time()  # Finaliza a medição do tempo
        tempo_execucao = end_time - start_time
        print(f"Tempo de execução para CISC: {tempo_execucao:.6f} segundos")
        self.resultados.append(("CISC", tempo_execucao))
        input("Pressione Enter para continuar...")

    def executar_multinucleo(self):
        start_time = time.time()  # Inicia a medição do tempo
        print("Simulando processador multinúcleo...")
        
        for _ in range(50000):  # Metade da carga em cada núcleo
            # Núcleo 1
            self.registradores[0] = 10  # Load valor em R0
            self.registradores[2] = self.registradores[0] + self.registradores[1]  # ADD R0, R1 -> R2

            # Núcleo 2
            self.registradores[1] = 20  # Load valor em R1
            self.registradores[3] = self.registradores[1] - 5  # SUB R1, 5 -> R3

        end_time = time.time()  # Finaliza a medição do tempo
        tempo_execucao = end_time - start_time
        print(f"Tempo de execução para multinúcleo: {tempo_execucao:.6f} segundos")
        self.resultados.append(("Multinúcleo", tempo_execucao))
        input("Pressione Enter para continuar...")

    def executar_hyper_threading(self):
        start_time = time.time()  # Inicia a medição do tempo
        print("Simulando processador com hyper-threading...")
        
        for _ in range(50000):  # Metade da carga para cada thread
            # Thread 1
            self.registradores[0] = 10  # Load valor em R0
            self.registradores[2] = self.registradores[0] + self.registradores[1]  # ADD R0, R1 -> R2

            # Thread 2
            self.registradores[1] = 20  # Load valor em R1
            self.registradores[3] = self.registradores[1] - 5  # SUB R1, 5 -> R3

        end_time = time.time()  # Finaliza a medição do tempo
        tempo_execucao = end_time - start_time
        print(f"Tempo de execução para hyper-threading: {tempo_execucao:.6f} segundos")
        self.resultados.append(("Hyper-Threading", tempo_execucao))
        input("Pressione Enter para continuar...")

    def comparar_RISC_CISC(self):
        print("Comparando RISC vs CISC...")
        self.executar_instrucoes_RISC()
        print("\n")
        self.executar_instrucoes_CISC()
        print("\n")

    def comparar_tipos_processadores(self):
        print("Comparando diferentes tipos de processadores...")
        self.executar_multinucleo()
        print("\n")
        self.executar_hyper_threading()
        print("\n")

    def gerar_relatorio(self):
        # Ordenar os resultados com base no tempo de execução
        self.resultados.sort(key=lambda x: x[1])
        print("Relatório de desempenho (do mais rápido para o mais lento):")
        for i, (nome, tempo) in enumerate(self.resultados, start=1):
            print(f"{i}. {nome} - Tempo de execução: {tempo:.6f} segundos")

# Inicializar e executar o simulador
simulador = SimuladorCPU()
simulador.comparar_RISC_CISC()
simulador.comparar_tipos_processadores()
simulador.gerar_relatorio()

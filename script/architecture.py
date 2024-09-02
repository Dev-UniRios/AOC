import time

# Simulador de Arquiteturas RISC e CISC com Núcleo Único, Multinúcleo e Hyper-Threading

class SimuladorCPU:
    def __init__(self):
        self.registradores = [0] * 8
        self.resultados = []

    def executar_instrucoes_RISC(self):
        start_time = time.time()
        print("Executando instruções em arquitetura RISC (núcleo único)...")
        
        for _ in range(100000):
            self.registradores[0] = 10
            self.registradores[1] = 20
            self.registradores[2] = self.registradores[0] + self.registradores[1]
            self.registradores[3] = self.registradores[2] - 5

        end_time = time.time()
        tempo_execucao = end_time - start_time
        print(f"Tempo de execução para RISC: {tempo_execucao:.6f} segundos")
        self.resultados.append(("RISC", tempo_execucao))
        input("Pressione Enter para continuar...")

    def executar_instrucoes_CISC(self):
        start_time = time.time()
        print("Executando instruções em arquitetura CISC (núcleo único)...")
        
        for _ in range(100000):
            self.registradores[0] = 10
            self.registradores[1] = 20
            self.registradores[3] = (self.registradores[0] + self.registradores[1]) - 5

        end_time = time.time()
        tempo_execucao = end_time - start_time
        print(f"Tempo de execução para CISC: {tempo_execucao:.6f} segundos")
        self.resultados.append(("CISC", tempo_execucao))
        input("Pressione Enter para continuar...")

    def executar_multinucleo(self):
        start_time = time.time()
        print("Simulando processador multinúcleo...")
        
        for _ in range(50000):
            self.registradores[0] = 10
            self.registradores[2] = self.registradores[0] + self.registradores[1]

            self.registradores[1] = 20
            self.registradores[3] = self.registradores[1] - 5

        end_time = time.time()
        tempo_execucao = end_time - start_time
        print(f"Tempo de execução para multinúcleo: {tempo_execucao:.6f} segundos")
        self.resultados.append(("Multinúcleo", tempo_execucao))
        input("Pressione Enter para continuar...")

    def executar_hyper_threading(self):
        start_time = time.time()
        print("Simulando processador com hyper-threading...")
        
        for _ in range(50000):
            self.registradores[0] = 10
            self.registradores[2] = self.registradores[0] + self.registradores[1]

            self.registradores[1] = 20
            self.registradores[3] = self.registradores[1] - 5

        end_time = time.time()
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
        self.resultados.sort(key=lambda x: x[1])
        print("Relatório de desempenho (do mais rápido para o mais lento):")
        for i, (nome, tempo) in enumerate(self.resultados, start=1):
            print(f"{i}. {nome} - Tempo de execução: {tempo:.6f} segundos")

simulador = SimuladorCPU()
simulador.comparar_RISC_CISC()
simulador.comparar_tipos_processadores()
simulador.gerar_relatorio()

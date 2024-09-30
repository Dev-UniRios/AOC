import time
import random

# Dispositivos conhecidos
dispositivos_io = {
    "teclado": {"tipo": "entrada", "prioridade": 1},
    "mouse": {"tipo": "entrada", "prioridade": 2},
    "monitor": {"tipo": "saida", "prioridade": 1},
    "impressora": {"tipo": "saida", "prioridade": 2},
    "webcam": {"tipo": "entrada", "prioridade": 3},
    "microfone": {"tipo": "entrada", "prioridade": 4}
}

# Controlador Roni
class ControladorRoni:
    def __init__(self):
        self.lista_dispositivos = []

    def adicionar_dispositivo(self, dispositivo):
        if dispositivo in dispositivos_io:
            self.lista_dispositivos.append(dispositivo)
            print(f"\nControlador Roni: {dispositivo.upper()} detectado. Verificando prioridade...")
            time.sleep(1)
            self.verificar_prioridade(dispositivo)
        else:
            print(f"\nControlador Roni: {dispositivo.upper()} não reconhecido! Não será adicionado ao sistema.")

    def verificar_prioridade(self, dispositivo):
        info = dispositivos_io[dispositivo]
        print(f"Tipo de dispositivo: {info['tipo'].capitalize()}")
        print(f"Prioridade de processamento: {info['prioridade']}")

        if info["prioridade"] == 1:
            print(f"Controlador Roni: {dispositivo.upper()} tem alta prioridade! Processando imediatamente.")
            self.processar_dispositivo(dispositivo)
        else:
            print(f"Controlador Roni: {dispositivo.upper()} tem prioridade menor. Aguardando a fila de processamento.")
            self.lista_dispositivos.sort(key=lambda x: dispositivos_io[x]["prioridade"])

    def processar_dispositivo(self, dispositivo):
        print(f"Controlador Roni: {dispositivo.upper()} está agora sendo processado pelo sistema...\n")
        time.sleep(2)  # Simula o tempo de processamento
        print(f"Controlador Roni: {dispositivo.upper()} foi processado com sucesso!\n")

# Função que simula a inserção de novos dispositivos
def plugar_dispositivos():
    controlador = ControladorRoni()

    dispositivos_novos = ["teclado", "monitor", "impressora", "webcam", "microfone", "mouse"]
    random.shuffle(dispositivos_novos)

    for dispositivo in dispositivos_novos:
        controlador.adicionar_dispositivo(dispositivo)
        time.sleep(1)

    print("\nResumo: Lista de dispositivos no sistema por ordem de prioridade:")
    for dispositivo in controlador.lista_dispositivos:
        print(f" - {dispositivo.capitalize()} (Prioridade {dispositivos_io[dispositivo]['prioridade']})")

# Executar a simulação
plugar_dispositivos()

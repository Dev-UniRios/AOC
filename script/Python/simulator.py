class WhatsappSimulator:
    def __init__(self):
        self.caixas_de_mensagens = ["Opa!", "Tudo certo e nada errado?", "Vamos ao cinema?"]
        self.pipeline = [''] * 4
        self.contador_mensagens = 0

    def capturar_mensagem(self):
        # Fetch: Captura a mensagem que será enviada
        if self.contador_mensagens < len(self.caixas_de_mensagens):
            self.pipeline[0] = self.caixas_de_mensagens[self.contador_mensagens]
            print(f"Capturando mensagem: {self.pipeline[0]}")
            self.contador_mensagens += 1
        else:
            self.pipeline[0] = 'ESPERA'
            print("Nenhuma nova mensagem para capturar, esperando...")

    def codificar_mensagem(self):
        # Decode: Codifica a mensagem em um formato que possa ser enviado pela rede
        mensagem = self.pipeline[0]
        if mensagem != 'ESPERA':
            self.pipeline[1] = f"Codificando: {mensagem}"
            print(self.pipeline[1])
        else:
            self.pipeline[1] = 'ESPERA'
            print("Nada para codificar, esperando...")

    def enviar_mensagem(self):
        # Execute: Envia a mensagem codificada para o destinatário
        codificacao = self.pipeline[1]
        if codificacao != 'ESPERA':
            self.pipeline[2] = codificacao.replace("Codificando", "Enviando")
            print(self.pipeline[2])
        else:
            self.pipeline[2] = 'ESPERA'
            print("Nada para enviar, esperando...")

    def notificar_recebimento(self):
        # Write-back: Notifica que a mensagem foi enviada com sucesso
        envio = self.pipeline[2]
        if envio != 'ESPERA':
            self.pipeline[3] = envio.replace("Enviando", "Mensagem enviada com sucesso!")
            print(self.pipeline[3])
        else:
            self.pipeline[3] = 'ESPERA'
            print("Nada para notificar, esperando...")

    def rodar_whatsapp(self):
        # Simulador do WhatsApp, gerenciando o fluxo pelo pipeline
        while self.contador_mensagens < len(self.caixas_de_mensagens) or any(estacao != 'ESPERA' for estacao in self.pipeline):
            print(f'Estágio das Estações: {self.pipeline}')
            self.notificar_recebimento()
            self.enviar_mensagem()
            self.codificar_mensagem()
            self.capturar_mensagem()

            print('-' * 40)

            input("Pressione Enter para continuar para o próximo ciclo...")

simulador_whatsapp = WhatsappSimulator()
simulador_whatsapp.rodar_whatsapp()

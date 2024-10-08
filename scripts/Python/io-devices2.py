import subprocess
import time

def parse_ioreg_output(output):
    # Filtra a saída para exibir apenas informações de barramentos USB e PCI
    lines = output.split('\n')
    filtered_info = []
    current_device = {}
    
    for line in lines:
        # Detecta dispositivos USB e PCI
        if "IOUSBHostDevice" in line or "IOPCIDevice" in line:
            if current_device:
                filtered_info.append(current_device)
            current_device = {"type": "", "location": ""}
            
            if "IOUSBHostDevice" in line:
                current_device["type"] = "USB Device"
            elif "IOPCIDevice" in line:
                current_device["type"] = "PCI Device"
            
            # Captura o caminho do dispositivo no sistema (source location)
            location = line.split("@")[1].strip() if "@" in line else "Desconhecido"
            current_device["location"] = location
        # Captura detalhes de dispositivos conectados
        elif "|" in line and current_device:
            connected_device = line.strip().split(" ")[-1]  # Nome do dispositivo conectado
            current_device["connected"] = connected_device

    if current_device:
        filtered_info.append(current_device)
    
    return filtered_info

def get_bus_and_controllers_info():
    try:
        # Executa o comando ioreg para listar barramentos e dispositivos conectados
        result = subprocess.run(['ioreg', '-l'], stdout=subprocess.PIPE)
        bus_info = result.stdout.decode('utf-8')
        filtered_info = parse_ioreg_output(bus_info)
        return filtered_info
    except Exception as e:
        print(f"Erro ao obter informações sobre barramentos e controladores: {e}")
        return None

def display_info(info):
    print("\n--- Resumo dos Barramentos e Controladores ---")
    if info:
        for device in info:
            print(f"Tipo de dispositivo: {device['type']}")
            print(f"Local de origem: {device['location']}")
            if 'connected' in device:
                print(f"Dispositivo conectado: {device['connected']}")
            print("---")
    else:
        print("Nenhuma informação disponível.")
    print("--------------------------------------------\n")

def monitor_buses_and_controllers():
    print("Monitorando barramentos e controladores...\n")
    previous_info = get_bus_and_controllers_info()
    
    while True:
        current_info = get_bus_and_controllers_info()
        if current_info != previous_info:
            print("Mudança detectada nos barramentos ou dispositivos conectados:")
            display_info(current_info)
            previous_info = current_info
        time.sleep(5)  # Verifica a cada 5 segundos

if __name__ == "__main__":
    monitor_buses_and_controllers()

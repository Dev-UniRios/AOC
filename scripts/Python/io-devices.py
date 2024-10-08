import subprocess
import time

def get_usb_devices():
    try:
        # Executa o comando system_profiler para listar dispositivos USB
        result = subprocess.run(['system_profiler', 'SPUSBDataType'], stdout=subprocess.PIPE)
        usb_info = result.stdout.decode('utf-8')
        return usb_info
    except Exception as e:
        print(f"Erro ao obter dispositivos USB: {e}")
        return None
    except KeyboardInterrupt as f:
        print(f"Programa interrompido pelo usuário: {f}")
        return None

def monitor_usb_devices():
    print("Monitorando dispositivos USB conectados...\n")
    previous_devices = get_usb_devices()
    
    while True:
        current_devices = get_usb_devices()
        if current_devices != previous_devices:
            print("Mudança detectada nos dispositivos USB:")
            print(current_devices)
            previous_devices = current_devices
        time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente

if __name__ == "__main__":
    monitor_usb_devices()

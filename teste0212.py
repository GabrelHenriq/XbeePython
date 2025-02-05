from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import time

# Inicialize o dispositivo XBee (Coordenador) na porta COM6
xbee = XBeeDevice("COM6", 9600)  # Coordenador conectado na COM6

# Abrir a conexão com o XBee
xbee.open()

# Definir o endereço do dispositivo remoto (em 64 bits) - exemplo de endereço
remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A20041AEB242"))

# Função para enviar dados ao dispositivo remoto
def send_data_to_remote_device():
    message = "Hello from Coordinator!"
    # Enviar os dados de forma assíncrona
    xbee.send_data(remote, message)
    print(f"Mensagem enviada para o dispositivo remoto: {message}")

# Enviar dados para o dispositivo remoto
send_data_to_remote_device()

# Aguarde por um tempo antes de fechar (para garantir que a mensagem seja enviada)
time.sleep(1)

# Fechar a conexão
xbee.close()

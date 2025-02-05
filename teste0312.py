from digi.xbee.devices import ZigBeeDevice, RemoteZigBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import time

# Inicialize o dispositivo ZigBee (Coordenador) na porta COM6
zigbee = ZigBeeDevice("COM6", 9600)  # Coordenador conectado na COM6

# Abrir a conexão com o dispositivo ZigBee
zigbee.open()

# Definir o endereço do dispositivo remoto (em 64 bits) - exemplo de endereço
remote_device = RemoteZigBeeDevice(zigbee, XBee64BitAddress.from_hex_string("0013A20041AEB242"))

# Função de callback para processar os dados recebidos
def data_received_callback(xbee_message):
    # Obter o remetente e os dados recebidos
    sender = xbee_message.remote_device.get_64bit_addr()
    data = xbee_message.data.decode('utf-8')  # Decodifica os dados recebidos
    print(f"Dados recebidos de {sender}: {data}")

# Definir o callback para dados recebidos
zigbee.add_data_received_callback(data_received_callback)

# Função para enviar dados ao dispositivo remoto
def send_data_to_remote_device():
    message = "Hello from Coordinator!"
    zigbee.send_data(remote_device, message)
    print(f"Mensagem enviada para o dispositivo remoto: {message}")

# Enviar dados para o dispositivo remoto
send_data_to_remote_device()

# Manter o coordenador ativo para processar respostas
try:
    print("Esperando por respostas do dispositivo remoto...")
    while True:
        time.sleep(1)  # Aguarda 1 segundo antes de continuar o loop
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")

# Fechar a conexão
zigbee.close()

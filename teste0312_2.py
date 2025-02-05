from digi.xbee.devices import ZigBeeDevice
from digi.xbee.models.address import XBee64BitAddress

# Inicialize o dispositivo ZigBee (Remoto) na porta COM5
zigbee = ZigBeeDevice("COM5", 9600)  # Dispositivo remoto conectado na COM5

# Abrir a conexão com o dispositivo ZigBee
zigbee.open()

# Função de callback para quando os dados forem recebidos
def data_received_callback(data):
    print(f"Dados recebidos do coordenador: {data.data.decode('utf-8')}")  # Decodifica os dados para string
    
    # Responder com uma mensagem
    response = "Hello from Remote Device!"
    # Responder ao coordenador
    zigbee.send_data(data.remote_device, response)
    print(f"Resposta enviada para o coordenador: {response}")

# Definir o callback para dados recebidos
zigbee.add_data_received_callback(data_received_callback)

# Manter o dispositivo remoto ativo para receber dados
try:
    print("Esperando por dados do coordenador...")
    while True:
        pass
except KeyboardInterrupt:
    print("Dispositivo interrompido pelo usuário.")

# Fechar a conexão
zigbee.close()

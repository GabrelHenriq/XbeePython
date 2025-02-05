from digi.xbee.devices import XBeeDevice
from digi.xbee.models.address import XBee64BitAddress

# Inicialize o dispositivo XBee (Remoto) na porta COM5
xbee = XBeeDevice("COM5", 9600)  # Dispositivo remoto conectado na COM5

# Abrir a conexão com o XBee
xbee.open()

# Função de callback para quando os dados forem recebidos
def data_received_callback(data):
    print(f"Dados recebidos do coordenador: {data}")
    
    # Responder com uma mensagem
    response = "Hello from Remote Device!"
    # Responder ao coordenador com a mesma mensagem
    xbee.send_data(data.remote_device, response)
    print(f"Resposta enviada para o coordenador: {response}")

# Definir o callback para dados recebidos
xbee.add_data_received_callback(data_received_callback)

# Manter o dispositivo remoto ativo para receber dados
try:
    print("Esperando por dados do coordenador...")
    while True:
        pass
except KeyboardInterrupt:
    pass

# Fechar a conexão
xbee.close()

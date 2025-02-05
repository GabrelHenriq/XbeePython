from digi.xbee.devices import ZigBeeDevice

# Inicialização do dispositivo ZigBee (Coordenador)
coordinator = ZigBeeDevice("COM5", 9600)  # Porta correta: COM5

try:
    # Abrir a conexão com o dispositivo ZigBee
    coordinator.open()

    # Testar o comando AT para o ID da rede
    network_id = coordinator.get_parameter("ID")  # "ID" para identificar a rede
    print(f"ID da rede ZigBee: {network_id}")

    # Testar o comando AT para o nome do nó na rede
    node_name = coordinator.get_parameter("NI")  # "NI" para o nome do nó
    print(f"Nome do nó na rede: {node_name}")

    # Testar o comando AT para o endereço de hardware do dispositivo
    hardware_address = coordinator.get_parameter("SH")  # "SH" para o endereço de hardware
    print(f"Endereço de hardware (SH): {hardware_address}")

    # Testar o comando AT para o endereço de rede do dispositivo
    network_address = coordinator.get_parameter("SL")  # "SL" para o endereço de rede
    print(f"Endereço de rede (SL): {network_address}")

    # Testar o comando AT para o valor do RSSI (Received Signal Strength Indicator)
    rssi = coordinator.get_parameter("DB")  # "DB" para o valor do RSSI
    print(f"RSSI: {rssi}")

    # Testar o comando AT para a tabela de roteamento (RT)
    route_table = coordinator.get_parameter("RT")  # "RT" para a tabela de roteamento
    print(f"Tabela de Roteamento (RT): {route_table}")

finally:
    if coordinator is not None and coordinator.is_open():
        coordinator.close()

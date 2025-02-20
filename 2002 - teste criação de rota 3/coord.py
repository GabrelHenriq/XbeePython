from digi.xbee.devices import ZigBeeDevice

def setup_coordinator():
    try:
        # Configurar o dispositivo ZigBee Coordenador na porta serial correta
        coordinator = ZigBeeDevice("COM6", 9600)  # Coordenador na porta COM6
        coordinator.open()

        print("Configurando o Coordenador...")

        # Definindo Coordenador (CE=1)
        coordinator.set_parameter("CE", b'\x01')
        coordinator.write_changes()

        # Configuração do endereço de destino (Roteador)
        coordinator.set_parameter("DH", b'\x13\xA2\x00')  # Parte alta do endereço do Roteador
        coordinator.set_parameter("DL", b'\x41\xAE\xB2\x42')  # Parte baixa do endereço do Roteador
        coordinator.write_changes()

        # Exibir informações do coordenador
        print("ID da Rede:", coordinator.get_parameter("ID"))
        print("Nome do Nó:", coordinator.get_parameter("NI"))

        # Broadcast para atualizar a rede
        print("Enviando broadcast para atualizar rede...")
        coordinator.send_data_broadcast("Atualizando rota na rede...")

        return coordinator

    except Exception as e:
        print(f"Erro ao configurar o coordenador: {e}")
        return None

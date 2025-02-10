from digi.xbee.devices import ZigBeeDevice

def setup_coordinator():
    try:
        # Configurar o dispositivo ZigBee Coordenador na porta serial correta
        coordinator = ZigBeeDevice("COM6", 9600)  # Coordenador na porta COM6
        coordinator.open()

        print("Configurando o Coordenador...")
        coordinator.set_parameter("CE", b'\x01')  # Coordenador habilitado
        coordinator.write_changes()

        # Verificar o ID da rede
        id_network = coordinator.get_parameter("ID")
        print(f"ID da Rede: {id_network}")

        # Verificar o Nome do Dispositivo
        node_name = coordinator.get_parameter("NI")
        print(f"Nome do Nó: {node_name}")

        return coordinator

    except Exception as e:
        print(f"Erro ao configurar o coordenador: {e}")
        return None

if __name__ == "__main__":
    coordinator = setup_coordinator()
    if coordinator:
        print("Coordenador configurado com sucesso!")

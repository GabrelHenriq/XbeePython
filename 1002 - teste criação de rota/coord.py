from digi.xbee.devices import ZigBeeDevice

def setup_coordinator():
    # Configurar o dispositivo ZigBee Coordenador na porta serial correta
    coordinator = ZigBeeDevice("COM6", 9600)  # Coordenador na porta COM6
    coordinator.open()

    print("Configurando o Coordenador...")
    coordinator.set_parameter("CE", b'\x01')  # Coordenador habilitado
    coordinator.write_changes()

    return coordinator

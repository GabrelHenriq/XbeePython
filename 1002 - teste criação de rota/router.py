from digi.xbee.devices import ZigBeeDevice

def setup_router():
    try:
        # Configurar o dispositivo ZigBee Roteador na porta serial correta
        router = ZigBeeDevice("COM5", 9600)  # Roteador na porta COM5
        router.open()

        # Configuração do roteador
        print("Configurando o Roteador...")

        # Desativar modo de coordenador (para o roteador)
        router.set_parameter("CE", b'\x00')  # Desativar coordenador (CE=0)
        router.set_parameter("NJ", b'\xFF')  # Permitir associação por tempo indeterminado
        router.write_changes()
        return router

    except Exception as e:
        print(f"Erro ao configurar o roteador: {e}")
        return None

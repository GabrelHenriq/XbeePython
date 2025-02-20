from digi.xbee.devices import ZigBeeDevice

def setup_router():
    try:
        # Configurar o dispositivo ZigBee Roteador na porta serial correta
        router = ZigBeeDevice("COM5", 9600)  # Roteador na porta COM5
        router.open()

        print("Roteador configurado e conectado com sucesso!")
        print("Configurando o Roteador...")

        # Desativar modo de coordenador (CE=0)
        router.set_parameter("CE", b'\x00')
        router.write_changes()

        # Configuração do endereço de destino (Coordenador)
        router.set_parameter("DH", b'\x13\xA2\x00')  # Parte alta do endereço do Coordenador
        router.set_parameter("DL", b'\x41\xAE\xB3\xD3')  # Parte baixa do endereço do Coordenador
        router.write_changes()

        # Verificar se o roteador está aberto
        if router.is_open():
            print("Roteador aberto com sucesso e pronto para uso.")
        else:
            print("Falha ao abrir a conexão com o roteador.")
            return None

        return router

    except Exception as e:
        print(f"Erro ao configurar o roteador: {e}")
        return None

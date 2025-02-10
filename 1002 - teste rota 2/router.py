from digi.xbee.devices import ZigBeeDevice

def setup_router():
    try:
        # Configurar o dispositivo ZigBee Roteador na porta serial correta
        router = ZigBeeDevice("COM5", 9600)  # Roteador na porta COM5
        router.open()

        print("Roteador configurado e conectado com sucesso!")

        # Configuração do roteador
        print("Configurando o Roteador...")

        # Definir o nome do nó (para identificação)
        router.set_parameter("NI", b'Router')  # Nome do nó
        router.set_parameter("ID", b'\x1234')  # ID da rede
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

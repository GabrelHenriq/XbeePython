from digi.xbee.devices import ZigBeeDevice, XBee64BitAddress

# Inicialização do dispositivo ZigBee (Coordenador)
coordinator = ZigBeeDevice("COM5", 9600)  # Porta correta: COM5

try:
    # Abrir a conexão com o dispositivo ZigBee
    coordinator.open()

    # Obter a tabela de roteamento
    print("Obtendo a tabela de roteamento...")
    try:
        route_table_raw = coordinator.get_parameter("RT")  # Obtém o parâmetro RT (Routing Table)

        # Exibir o valor retornado para debug
        print(f"Dados retornados pelo comando RT: {route_table_raw}")

        # Verificar se há dados na tabela
        if not route_table_raw:
            print("Nenhuma entrada encontrada na tabela de roteamento.")
        else:
            # Garantir que o número de bytes é múltiplo de 2
            if len(route_table_raw) % 2 != 0:
                print("Dados inválidos na tabela de roteamento.")
            else:
                # Processar os dados da tabela
                print("Tabela de Roteamento com Qualidade de Link:")
                print("------------------------------------------------------------")
                print("{:<16} {:<16} {:<10}".format("Endereço Destino", "Próximo Salto", "RSSI"))
                print("------------------------------------------------------------")

                for i in range(0, len(route_table_raw), 2):
                    destination = format(route_table_raw[i], "02X")
                    next_hop = format(route_table_raw[i + 1], "02X")
                    print(f"{destination:<16} {next_hop:<16}")

    except KeyError:
        print("O comando RT não é suportado pelo dispositivo.")
finally:
    # Fechar a conexão com o dispositivo
    if coordinator is not None and coordinator.is_open():
        coordinator.close()

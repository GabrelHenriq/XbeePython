from digi.xbee.devices import ZigBeeDevice
from digi.xbee.models.routing import RouteRecord

# Configurar o dispositivo ZigBee (coordenador ou roteador) na porta COM
zigbee = ZigBeeDevice("COM6", 9600)  # Substitua "COM6" pela porta correta

try:
    # Abrir a conexão com o dispositivo
    zigbee.open()

    # Verificar se o dispositivo suporta tabela de roteamento
    if not zigbee.supports_routing():
        print("Este dispositivo não suporta tabela de roteamento.")
    else:
        print("Obtendo a tabela de roteamento...")

        # Obter a tabela de roteamento
        route_table = zigbee.get_route_table()

        # Verificar se há entradas na tabela
        if not route_table:
            print("Nenhuma entrada na tabela de roteamento.")
        else:
            # Exibir as entradas da tabela
            print(f"Tabela de roteamento do dispositivo ZigBee ({zigbee.get_64bit_addr()}):")
            print("-------------------------------------------------------------")
            print("{:<16} {:<16} {:<10}".format("Endereço Destino", "Próximo Salto", "Status"))
            print("-------------------------------------------------------------")

            for route in route_table:
                # Cada rota é uma instância da classe RouteRecord
                destination = route.destination_address
                next_hop = route.next_hop_address
                status = route.status.name  # Status como string (ex.: ACTIVE, DISCOVERY)
                print(f"{destination:<16} {next_hop:<16} {status:<10}")
finally:
    # Fechar a conexão com o dispositivo
    if zigbee is not None and zigbee.is_open():
        zigbee.close()

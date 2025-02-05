from digi.xbee.devices import ZigBeeDevice

# Inicialização do dispositivo ZigBee (Roteador)
router = ZigBeeDevice("COM4", 9600)  # Substitua "COM7" pela porta correta do roteador

try:
    # Abrir a conexão com o dispositivo ZigBee
    router.open()

    # O roteador pode realizar ações específicas, como reportar status ou retransmitir mensagens
    print("Roteador inicializado e aguardando comandos...")
    input("Pressione Enter para finalizar o programa.")

finally:
    # Fechar a conexão com o dispositivo
    if router is not None and router.is_open():
        router.close()

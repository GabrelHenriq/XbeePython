from coord import setup_coordinator
from router import setup_router
import time  # ADICIONADO para a espera do listener

def main():
    print("Iniciando a configuração do Coordenador e Roteador...")

    # Configurar Coordenador
    coordinator = setup_coordinator()
    if coordinator:
        print("Coordenador configurado com sucesso!")
    else:
        print("Falha ao configurar o coordenador.")
        return

    # Configurar Roteador
    router = setup_router()
    if router:
        print("Roteador configurado com sucesso!")
    else:
        print("Falha ao configurar o roteador.")
        return

    # Se ambos estão configurados corretamente
    print("Configuração concluída com sucesso.")

    print("\nConfigurando a tabela de roteamento...")
    routing_table_coordinator = coordinator.get_parameter("RT")
    routing_table_router = router.get_parameter("RT")

    table = router.get_routes() 

    print(table)
    
    print(f"Tabela de Roteamento do Coordenador: {routing_table_coordinator}")
    print(f"Tabela de Roteamento do Roteador: {routing_table_router}")

    print("\nEnviando mensagem de teste...")
    try:
        coordinator.send_data_broadcast("Teste de comunicação entre XBee!")
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

    # ADICIONADO: Tempo para o listener do Roteador receber mensagens
    print("\nAguardando resposta do Roteador...")
    time.sleep(10)

    # Fechar as conexões
    if coordinator.is_open():
        coordinator.close()

    if router.is_open():
        router.close()

if __name__ == "__main__":
    main()

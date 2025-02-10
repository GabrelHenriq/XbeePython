from coord import setup_coordinator
from router import setup_router

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
    
    print(f"Tabela de Roteamento do Coordenador: {routing_table_coordinator}")
    print(f"Tabela de Roteamento do Roteador: {routing_table_router}")

        # Fechar as conexões
    if coordinator.is_open():
        coordinator.close()

    if router.is_open():
        router.close()

if __name__ == "__main__":
    main()

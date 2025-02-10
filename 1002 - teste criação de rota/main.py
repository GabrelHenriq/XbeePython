from coord import setup_coordinator
from router import setup_router

# Função principal para executar o código
def main():
    # Configurando o coordenador
    coordinator = setup_coordinator()
    if not coordinator:
        print("Falha ao configurar o coordenador. Encerrando o script.")
        return

    # Configurando o roteador
    router = setup_router()
    if not router:
        print("Falha ao configurar o roteador. Encerrando o script.")
        return

    # Testar se o coordenador e o roteador estão configurados corretamente
    print("\nConfigurando a tabela de roteamento...")
    routing_table_coordinator = coordinator.get_parameter("RT")
    routing_table_router = router.get_parameter("RT")
    
    print(f"Tabela de Roteamento do Coordenador: {routing_table_coordinator}")
    print(f"Tabela de Roteamento do Roteador: {routing_table_router}")

    # Finalizando a execução
    print("\nProcesso concluído.")
    
    # Fechar as conexões
    if coordinator.is_open():
        coordinator.close()

    if router.is_open():
        router.close()

if __name__ == "__main__":
    main()

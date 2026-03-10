import os
from src.controllers.gasto_controller import GastoController
from src.repositories.gasto_repository import GastoRepository

def iniciar_sistema():
    mes_env = int(os.getenv("MES_CONSULTA", 3))
    ano_env = int(os.getenv("ANO_CONSULTA", 2026))

    controller = GastoController()
    resultado = controller.obter_relatorio_mensal(mes=mes_env, ano=ano_env)
    
    print(f"--- 📊 Relatório de Gastos ---")
    print(resultado)

if __name__ == "__main__":
    iniciar_sistema()

    from src.repositories.gasto_repository import GastoRepository

repo = GastoRepository()
lista = repo.listar_todos()

print("--- Teste de Leitura de Gastos ---")
print(lista)
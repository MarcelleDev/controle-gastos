import os
from controllers.gasto_controller import GastoController

def iniciar_sistema():
    # Buscando o 'bilhete' do sistema. Se não existir, usa 3 por padrão.
    mes_env = int(os.getenv("MES_CONSULTA", 3))
    ano_env = int(os.getenv("ANO_CONSULTA", 2026))

    controller = GastoController()
    resultado = controller.obter_relatorio_mensal(mes=mes_env, ano=ano_env)
    
    print(f"--- 📊 Relatório de Gastos ---")
    print(resultado)

if __name__ == "__main__":
    iniciar_sistema()
from repositories.gasto_repository import GastoRepository
from services.gasto_service import GastoService

class GastoController:
    def __init__(self):
        self.repository = GastoRepository()
        self.service = GastoService()

    def obter_relatorio_mensal(self, mes, ano):
        # 1. Busca os dados brutos no repositório
        todos_os_gastos = self.repository.buscar_todos()
        
        # 2. Envia para o serviço calcular o total do mês solicitado
        total = self.service.calcular_total_mes(todos_os_gastos, mes, ano)
        
        return f"Total de gastos em {mes}/{ano}: R$ {total:.2f}"
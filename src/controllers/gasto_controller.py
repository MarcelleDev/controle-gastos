from src.repositories.gasto_repository import GastoRepository
from src.services.gasto_service import GastoService

class GastoController:
    def __init__(self):
        self.repository = GastoRepository() 
        
        self.service = GastoService() 

    def obter_relatorio_mensal(self, mes, ano):
        todos_os_gastos = self.repository.listar_todos()
        
        total = self.service.calcular_total_mes(todos_os_gastos, mes, ano)
        
        return f"Total de gastos em {mes}/{ano}: R$ {total:.2f}"
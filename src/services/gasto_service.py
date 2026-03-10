from datetime import datetime

class GastoService:
    def calcular_total_mes(self, gastos, mes_desejado, ano_desejado):
        total = 0.0
        for gasto in gastos:        
            data_objeto = datetime.strptime(gasto['data'], "%Y-%m-%d")
            
            if data_objeto.month == mes_desejado and data_objeto.year == ano_desejado:
                total += gasto['valor']
        
        return total
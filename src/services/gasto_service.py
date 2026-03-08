class GastoService:
    def calcular_total_mes(self, lista_de_gastos, mes_desejado, ano_desejado):
        total = 0
        for gasto in lista_de_gastos:
            # Verificamos se o mês e o ano coincidem
            if gasto.data.month == mes_desejado and gasto.data.year == ano_desejado:
                total += gasto.valor
        return total
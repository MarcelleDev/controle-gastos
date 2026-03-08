from models.gasto import Gasto
from datetime import date

class GastoRepository:
    def buscar_todos(self):
        return [
            Gasto(descricao="Internet", valor=150.0, data=date(2026, 3, 1)),
            Gasto(descricao="Luz", valor=200.0, data=date(2026, 3, 5)),
            Gasto(descricao="Mercado", valor=500.0, data=date(2026, 2, 20)),
        ]
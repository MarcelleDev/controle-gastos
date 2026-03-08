from dataclasses import dataclass
from datetime import date 

@dataclass
class Gasto:   
    descricao: str
    valor: float
    data: date
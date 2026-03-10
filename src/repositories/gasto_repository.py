import json
import os

class GastoRepository:
    def __init__(self):
      
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
      
        self.caminho_arquivo = os.path.join(diretorio_script, '..', 'data', 'gastos.json')
        
        
        self.caminho_arquivo = os.path.normpath(self.caminho_arquivo)

    def listar_todos(self):
        try:
            
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                return dados
        except FileNotFoundError:
            
            print(f"Erro: Arquivo não encontrado.")
            return []
        except json.JSONDecodeError:
            
            print("Erro: Formato JSON inválido.")
            return []
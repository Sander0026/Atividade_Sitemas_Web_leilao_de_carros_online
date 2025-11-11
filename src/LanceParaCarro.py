import json
from filas.FilaLance import FilaLance

def LanceParaCarro(evento):
    """
    Adiciona um lance à fila de lances.

        evento (dict): Um dicionário contendo as informações do lance.
                       Espera-se que tenha as chaves 'carro_id', 'valor' e 'comprador'.
    """
    print(f"Recebido lance: {evento}")
    FilaLance.put(evento)
    print("Lance adicionado à fila.")


'''# Exemplo de uso:
if __name__ == "__main__":
    lance_exemplo = {
        'carro_id': '123ABC',
        'valor': 15000,
        'comprador': 'João Silva'
    }
    LanceParaCarro(lance_exemplo)
'''
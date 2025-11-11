import json
from filas.FilaLance import FilaLance

def LanceParaCarro(evento):
 
    print(f"Recebido lance: {evento}")
    FilaLance.put(evento)
    print("Lance adicionado à fila.")



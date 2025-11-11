import json
from filas.FilaLance import FilaLance
import time

def MaiorLance(fila):
   
    maiores_lances = {}
    while True:
        if not fila.empty():
            lance = fila.get()
            print(f"Processando lance: {lance}")
            carro_id = lance.get('carro_id')
            valor_lance = lance.get('valor')

            if carro_id and valor_lance is not None:
                if carro_id not in maiores_lances or valor_lance > maiores_lances[carro_id]['valor']:
                    maiores_lances[carro_id] = lance
                    print(f"Novo maior lance para o carro {carro_id}: {maiores_lances[carro_id]}")
        time.sleep(1)


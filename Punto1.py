"""
Created on Sun Aug 20 12:59:05 2023

@author: juanj
"""

import numpy as np
import pandas as pd

matriz_transicion = np.array([
    [0, 0.5935, 0, 0, 0.4065, 0],
    [0, 0, 0.5046, 0, 0.4954, 0],
    [0, 0, 0, 0.4073, 0.5927, 0],
    [0, 0, 0, 0, 0.6393, 0.3607],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
])


num_empresas = 2000
num_meses = 20

estado_empresas = np.zeros((num_empresas, num_meses), dtype=int)

estado_empresas[:, 0] = 1

for mes in range(1, num_meses):
    for empresa in range(num_empresas):
       
        nuevo_estado = np.random.choice(range(1, 7), p=matriz_transicion[estado_empresas[empresa, mes - 1] - 1])
        estado_empresas[empresa, mes] = nuevo_estado

df = pd.DataFrame(estado_empresas)

df.insert(0, "Empresa", range(1, num_empresas + 1))

df.columns = ["Empresa"] + [f"Mes {mes}" for mes in range(1, num_meses + 1)]

df.to_csv("ssimulacion_empresas.csv", index=False)

empresas_en_estado_6 = np.sum(estado_empresas[:, -1] == 6)
empresas_en_estado_5 = np.sum(estado_empresas[:, -1] == 5)

probabilidad_llegar_estado_6 = empresas_en_estado_6 / num_empresas

probabilidad_llegar_estado_5 = empresas_en_estado_5 / num_empresas

print("Datos simulados exportados a 'simulacion_empresas.csv'")
print("Empresas en el estado 6 al final de los 20 meses:", empresas_en_estado_6)
print("Probabilidad de llegar al estado 6:", probabilidad_llegar_estado_6)
print("Empresas en el estado 5 al final de los 20 meses:", empresas_en_estado_5)
print("Probabilidad de llegar al estado 5:", probabilidad_llegar_estado_5)

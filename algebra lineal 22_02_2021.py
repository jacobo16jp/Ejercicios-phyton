import numpy as np
matriz = np.array ([[2,1,3],[-4,5,6],[-1,0,2]])
matriz_trasp=matriz.T
matriz_inv = np.linalg.inv(matriz)
print(matriz_inv)

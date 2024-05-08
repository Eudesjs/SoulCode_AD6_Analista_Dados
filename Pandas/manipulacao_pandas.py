import pandas as pd
import numpy as np

'''
Uma Series é uma estrutura de dados unidimensional em Pandas que é utilizada para armazenar uma sequência de valores, 
similar a um array unidimensional em NumPy. Cada valor em uma Series é associado a um índice, que pode ser personalizado
ou padrão. As Series são frequentemente utilizadas para representar uma única variável ou característica em um conjunto 
de dados e são uma das estruturas de dados fundamentais em Pandas. Elas oferecem funcionalidades poderosas para manipulação
e análise de dados, como indexação, filtragem e operações matemáticas.
'''
notas = pd.Series([10,5,7,5,9,10])
print(notas)
print(notas.values)
print(notas.index)

notas2 = pd.Series([10,5,7,5,9,10],index=['Eudes','Michele','Luna','Leda','Isnar','Diego'])
print(notas2)
print(notas.describe())
print(notas.mean())
print(notas**2)
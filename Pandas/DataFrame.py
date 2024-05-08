import pandas as pd
'''
Pandas é uma biblioteca popular de manipulação e análise de dados de código aberto para Python. 
Ela fornece estruturas de dados como DataFrames e Series que permitem aos usuários manipular e 
analisar facilmente dados tabulares. O Pandas é amplamente utilizado em ciência de dados, aprendizado
de máquina e outros campos para tarefas como limpeza de dados, transformação e exploração.
'''
import numpy as np
'''
NumPy é uma biblioteca fundamental para computação científica em Python. Ela fornece suporte para arrays
multidimensionais, juntamente com diversas funções matemáticas para operações eficientes em arrays. NumPy 
é amplamente utilizado em áreas como processamento de imagens, álgebra linear, estatística, entre outras, 
devido à sua eficiência e facilidade de uso. É comum ver o NumPy sendo utilizado em conjunto com outras 
bibliotecas como Pandas e Matplotlib para análise e visualização de dados.
'''
'''
Um DataFrame é uma estrutura de dados bidimensional em forma de tabela que é utilizada em bibliotecas como 
Pandas para armazenar e manipular dados de forma tabular. Cada coluna de um DataFrame representa uma variável 
ou característica, enquanto cada linha representa uma observação ou instância. Os DataFrames são muito utilizados 
em análise de dados, processamento de dados e modelagem estatística, pois permitem a fácil manipulação e visualização
de dados de forma organizada e eficiente.
'''
df = pd.DataFrame({
    'Aluno':["Eudes", "Michele", "Luna", "Leda", "Isnar"],
    'Faltas': [3,4,2,4,3],
    'Prova': [2,7,8,5.5,9.2],
    'Seminário': [8.5,5,8.2,6,9.5]
    
})

print(df)
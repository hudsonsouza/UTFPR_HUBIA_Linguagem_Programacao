# 01 - TRATAMENTO DO BANCO DE DADOS
import pandas as pd
import matplotlib.pyplot as plt
import os 
# import numpy as np

# Ajustar a configuração do Pandas para mostrar todas as colunas com o comando 'head()'
pd.set_option('display.max_columns', None)  


# 02 - LEITURA DO BANCO DE DADOS
dados1 = pd.read_csv('banco/banco_bombeiros-dados-tratados-3.csv', sep=',')

# IMPRIMIR OS PRIMEIROS 20 REGISTROS
print('\n### DADOS DO BANCO DE DADOS ORIGINAL ###')
print(f'Numero de Colunas..: {dados1.shape[1]}')
print(f'Numero de Linhas...: {dados1.shape[0]}')
print('\nDados do Banco: ') 
print(dados1.head(10))

# Passo 5: Imprimir o nome de todas as variáveis da base de dados
print("\nNomes das variáveis da base de dados:")
print(dados1.columns.tolist())

# Passo 6: Imprimir a descrição da base de dados
print("\nDescrição da base de dados:")
print(dados1.describe())

# Verificar tipos de dados
print("\nTipos de dados das colunas:")
print(dados1.dtypes)

# Contar valores nulos
print('\nContagem de valores nulls em cada coluna:')
null_counts = dados1.isnull().sum()
print(null_counts)


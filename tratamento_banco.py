# 01 - TRATAMENTO DO BANCO DE DADOS
import pandas as pd
import matplotlib.pyplot as plt
import os 
# import numpy as np

# Ajustar a configuração do Pandas para mostrar todas as colunas com o comando 'head()'
pd.set_option('display.max_columns', None)  


# 02 - LEITURA DO BANCO DE DADOS
dados1 = pd.read_csv('banco/banco_bombeiros-dados-brutos-1.csv', sep=';')

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



# Substituir vírgulas por pontos nas colunas  
dados1['peso_antes'] = dados1['peso_antes'].str.replace(',', '.', regex=False)  
dados1['peso_depois'] = dados1['peso_depois'].str.replace(',', '.', regex=False)  
dados1['peso_diferenca'] = dados1['peso_diferenca'].str.replace(',', '.', regex=False)  

# Converter as colunas de 'object' para 'float64'  
dados1['peso_antes'] = pd.to_numeric(dados1['peso_antes'], errors='coerce')  
dados1['peso_depois'] = pd.to_numeric(dados1['peso_depois'], errors='coerce')  
dados1['peso_diferenca'] = pd.to_numeric(dados1['peso_diferenca'], errors='coerce')  

# Verificar os tipos de dados das colunas  
print(dados1[['peso_antes', 'peso_depois', 'peso_diferenca']].dtypes)  

# Verificar tipos de dados
print("\nTipos de dados das colunas:")
print(dados1.dtypes)

# Verificar os tipos de dados das colunas  
print(dados1[['peso_antes', 'peso_depois', 'peso_diferenca']].dtypes)  


# Contar valores nulos
null_counts = dados1.isnull().sum()
print('\nContagem de valores nulls em cada coluna:')
print(null_counts)


# SUBSTITUIR VALORES NULOS PELA MEDIANA  
print('\n\n### SUBSTITUIR VALORES NULOS PELA MEDIANA ###\n\n')  

# VERIFICA SE HÁ VALORES NULOS  
if dados1.isnull().values.any():       
    # Substituir valores nulos pela mediana apenas em colunas numéricas  
    for coluna in dados1.select_dtypes(include=[np.number]).columns:  
        mediana = dados1[coluna].median()  
        dados1[coluna].fillna(mediana, inplace=True)  

    # Verificar se ainda há valores nulos  
    null_counts_after = dados1.isnull().sum()  
    print('Contagem de valores nulls após substituição:')  
    print(null_counts_after)  
else:   
    print('Nenhum valor nulo encontrado na base de dados.')

### CATEGORIZACAO DAS VARIAVEIS

# Processo de Anonimização da coluna 'avaliado'
# Criar a nova coluna 'combatente' com valores sequenciais  
dados1['combatente'] = ['Avaliado' + str(i) for i in range(1, len(dados1) + 1)]  

# Reorganizar as colunas para que 'combatente' fique após 'avaliador'  
# Primeiro, obtenha a lista de colunas  
colunas = dados1.columns.tolist()  

# Encontre o índice da coluna 'avaliador'  
indice_avaliador = colunas.index('avaliado')  

# Insira 'combatente' após 'avaliador'  
colunas.insert(indice_avaliador + 1, colunas.pop(colunas.index('combatente')))  

# Reorganize o DataFrame com a nova ordem de colunas  
dados1 = dados1[colunas]  

# Exibir as primeiras linhas do DataFrame atualizado  
print(dados1.head())  

# Remover colunas desnecessárias
dados1 = dados1.drop(columns=['num','avaliado'])

# Atualizar a lista de colunas  
colunas = dados1.columns.tolist()

# Reorganize o DataFrame com a nova ordem de colunas  
dados1 = dados1[colunas]  

# Exibir as primeiras linhas do DataFrame atualizado  
print(dados1.head())  



### TRATAMENTO DE DADOS: PESO

print('\n\n### TRATAMENTO DE DADOS: PESO ###\n')

# Imprimir as colunas selecionadas  
print(dados1[['peso_antes', 'peso_depois', 'peso_diferenca']].head()) 

# Calcular a diferença entre os pesos
dados1['peso_diferenca'] = dados1['peso_depois'] - dados1['peso_antes'] 

# Imprimir as colunas selecionadas  
print(dados1[['peso_antes', 'peso_depois', 'peso_diferenca']].head()) 



### TRATAMENTO DE DADOS: PRESSÃO ARTERIAL (PA)
print('\n\n### TRATAMENTO DE DADOS: PRESSÃO ARTERIAL (PA) ###\n')

# criando nova coluna sistolica
dados1['pa_diferenca_sist'] = dados1['pa_depois_sist'] - dados1['pa_antes_sist']

# criando nova coluna diastolica
dados1['pa_diferenca_diast'] = dados1['pa_depois_diast'] - dados1['pa_antes_diast']

# Imprimir as colunas selecionadas  
print(dados1[['pa_antes_sist', 'pa_depois_sist', 'pa_diferenca_sist']].head(10)) 

print('\n')

print(dados1[['pa_antes_diast', 'pa_depois_diast', 'pa_diferenca_diast']].head(10)) 




### TRATAMENTO DE DADOS: FREQUENCIA CARDIACA (FC)
print('\n\n### TRATAMENTO DE DADOS: FREQUENCIA CARDIACA (FC) ###\n')

# criando nova coluna sistolica
dados1['fc_diferenca'] = dados1['fc_depois'] - dados1['fc_antes']

# Imprimir as colunas selecionadas  
print(dados1[['fc_antes', 'fc_depois', 'fc_diferenca']].head(10)) 





### TRATAMENTO DE DADOS: SATURAÇÃO DE OXIGÊNIO (O2) 
print('\n\n### TRATAMENTO DE DADOS: SATURAÇÃO DE OXIGÊNIO (O2) ###\n')

# criando nova coluna sistolica
dados1['sat_o2_diferenca'] = dados1['sat_o2_depois'] - dados1['sat_o2_antes']

# Imprimir as colunas selecionadas  
print(dados1[['sat_o2_antes', 'sat_o2_depois', 'sat_o2_diferenca']].head(10)) 





### TRATAMENTO DE DADOS: AR CILINDRO (AC) 
print('\n\n### TRATAMENTO DE DADOS: AR CILINDRO (AC)  ###\n')


# Imprimir as colunas selecionadas  
print(dados1[['ar_cilindro_antes', 'ar_cilindro_depois', 'ar_cilindro_diferenca']].head(10)) 

# Substituir vírgulas por pontos nas colunas  
dados1['ar_cilindro_diferenca'] = dados1['ar_cilindro_diferenca'].str.replace(',', '.', regex=False)  

# Converter as colunas de 'object' para 'float64'  
dados1['ar_cilindro_diferenca'] = pd.to_numeric(dados1['ar_cilindro_diferenca'], errors='coerce')  

# Verificar os tipos de dados das colunas  
print(dados1[['ar_cilindro_antes', 'ar_cilindro_depois', 'ar_cilindro_diferenca']].dtypes)  

# Imprimir as colunas selecionadas  
print(dados1[['ar_cilindro_antes', 'ar_cilindro_depois', 'ar_cilindro_diferenca']].head(10)) 

# calcular a diferença entre ar_cilindro
dados1['ar_cilindro_diferenca'] = dados1['ar_cilindro_depois'] - dados1['ar_cilindro_antes']

# Imprimir as colunas selecionadas  
print(dados1[['ar_cilindro_antes', 'ar_cilindro_depois', 'ar_cilindro_diferenca']].head(10)) 





# Visualização de dados  
plt.figure(figsize=(10, 6), dpi=150)  
plt.hist(dados1['genero'], bins=30, alpha=0.7, color='blue')  
plt.title('Distribuição de Gênero')  
plt.xlabel('Gêneros')  
plt.ylabel('Frequência')  
plt.grid()  
plt.show()  


### MATRIZ DE CORRELACAO

# Verificar os tipos de dados das colunas  
print('\nTipos de dados das colunas:')
print(dados1.dtypes)  

# Especificar as colunas que você deseja incluir na matriz de correlação  
colunas_para_correlacao = ['idade', 
                           'tempo-exposicao-sdi', 
                           'peso_diferenca',
                           'pa_diferenca_sist',
                           'pa_diferenca_diast',
                           'fc_diferenca',
                           'sat_o2_diferenca',
                           'ar_cilindro_diferenca'
                            ]  


# Selecionar apenas as colunas especificadas  
dados_selecionados = dados1[colunas_para_correlacao]  

# Converter as colunas para numérico, se necessário  
dados_selecionados = dados_selecionados.apply(pd.to_numeric, errors='coerce')  

# Calcular a matriz de correlação  
correlacao = dados_selecionados.corr()  

# Plotar a matriz de correlação  
plt.figure(figsize=(12, 8))  
plt.imshow(correlacao, cmap='coolwarm', interpolation='none')  
plt.colorbar()  
plt.xticks(range(len(correlacao.columns)), correlacao.columns, rotation=90)  
plt.yticks(range(len(correlacao.columns)), correlacao.columns)  
plt.title('Matriz de Correlação')  
plt.show()  



### EXPORTAR O BANCO DE DADOS

print('\n\n### EXPORTAR O BANCO DE DADOS ###\n\n')
dados1.to_csv('banco/banco_bombeiros-dados-tratados-2.csv', sep=';', index=False)
print('Banco de dados exportado com sucesso!\n')
print(f'Caminho do arquivo: {os.path.abspath("banco/banco_bombeiros-dados-tratados-2.csv")}')


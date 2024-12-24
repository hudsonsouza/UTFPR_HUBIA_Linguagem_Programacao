import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
# conda install seaborn  
#import seaborn as sns  

#print(sns.__version__)  # Isso deve imprimir a versão do Seaborn instalada


# Ajustar a configuração do Pandas para mostrar todas as colunas com o comando 'head()'
pd.set_option('display.max_columns', None) 


# 1. Carregar a base de dados  
file_path = "banco/banco_bombeiros-dados-tratados-2.csv"  
data = pd.read_csv(file_path)  

# 2. Explorar os dados  
print("Primeiras linhas do DataFrame:")  
print(data.head())  

print("\nInformações sobre o DataFrame:")  
print(data.info())  

print("\nVerificando valores nulos:")  
print(data.isnull().sum())  

print("\nVerificando tipos de dados:")  
print(data.dtypes)

print("\nPrimeiras linhas do DataFrame:")
print(data.head())  

print("\nInformações da Descrição do DataFrame:")
print(data.describe()) 

# 3. Estatísticas descritivas  
print("\nEstatísticas descritivas:")  
descriptive_stats = data.describe()  
print(descriptive_stats)  

# 4. Análise com NumPy  
print("\nAnálise descritiva utilizando NumPy:")  
numeric_data = data.select_dtypes(include=[np.number])  

# Cálculo de estatísticas  
mean_values = np.mean(numeric_data, axis=0)  
median_values = np.median(numeric_data, axis=0)  
std_dev_values = np.std(numeric_data, axis=0)  
min_values = np.min(numeric_data, axis=0)  
max_values = np.max(numeric_data, axis=0)  

# Exibir resultados  
print("Média:\n", mean_values)  
print("Mediana:\n", median_values)  
print("Desvio Padrão:\n", std_dev_values)  
print("Mínimos:\n", min_values)  
print("Máximos:\n", max_values)  

# 5. Identificação de outliers  
# Usando o método do intervalo interquartil (IQR)  
Q1 = np.percentile(numeric_data, 25, axis=0)  
Q3 = np.percentile(numeric_data, 75, axis=0)  
IQR = Q3 - Q1  

# Definindo limites para outliers  
lower_bound = Q1 - 1.5 * IQR  
upper_bound = Q3 + 1.5 * IQR  

outliers = ((numeric_data < lower_bound) | (numeric_data > upper_bound)).sum()  
print("\nNúmero de outliers por coluna:\n", outliers)  

# Verificar os tipos de dados  
print("\nTipos de dados das colunas:")  
print(data.dtypes)  

# Selecionar apenas colunas numéricas  
numeric_data = data.select_dtypes(include=[np.number])  

# Verificar se há colunas numéricas  
if not numeric_data.empty:  
    # Plotar o histograma para cada coluna numérica  
    numeric_data.hist(bins=15, figsize=(15, 10))  
    plt.suptitle('Distribuição das Variáveis Numéricas')  
    plt.show()  
else:  
    print("Não há colunas numéricas para plotar.")  

# Boxplot para identificar outliers  
plt.figure(figsize=(15, 10))  
# sns.boxplot(data=numeric_data)  
plt.title('Boxplot das Variáveis Numéricas')  
plt.xticks(rotation=45)  
plt.show()
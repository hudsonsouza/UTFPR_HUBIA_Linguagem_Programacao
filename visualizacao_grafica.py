# 01 - TRATAMENTO DO BANCO DE DADOS
import pandas as pd  
import matplotlib as mpl  # Importando o módulo principal do Matplotlib  
import matplotlib.pyplot as plt  
import os   
import numpy as np  
import seaborn as sns 

print('\n### VERSAOS DOS MODULOS ###')
print(f'Versão do Matplotlib..: {mpl.__version__}')  
print(f'Versão do Pandas......: {pd.__version__}')  
print(f'Versão do Numpy.......: {np.__version__}') 
print(f'Versão do Seaborn.....: {sns.__version__}') 

# CONFIGURANDO MATPLOTLIB PARA UMA VERSAO MAIS AGRADÁVEL DOS GRÁFICOS
print(f'\nVerificando o Stilo disponivel no Matplotlib: {plt.style.available}')
plt.style.use('seaborn-v0_8-white')  

# Ajustar a configuração do Pandas para mostrar todas as colunas com o comando 'head()'
pd.set_option('display.max_columns', None)  


# 02 - LEITURA DO BANCO DE DADOS
dados4 = pd.read_csv('banco/banco_bombeiros-dados-tratados-3.csv', sep=',')

# IMPRIMIR OS PRIMEIROS 20 REGISTROS
print('\n### DADOS DO BANCO DE DADOS ORIGINAL ###')
print(f'Numero de Colunas..: {dados4.shape[1]}')
print(f'Numero de Linhas...: {dados4.shape[0]}')
print('\nDados do Banco: ') 
print(dados4.head(10))

# Passo 5: Imprimir o nome de todas as variáveis da base de dados
print("\nNomes das variáveis da base de dados:")
print(dados4.columns.tolist())

# Passo 6: Imprimir a descrição da base de dados
print("\nDescrição da base de dados:")
print(dados4.describe())

# Verificar tipos de dados
print("\nTipos de dados das colunas:")
print(dados4.dtypes)

# Contar valores nulos
print('\nContagem de valores nulls em cada coluna:')
null_counts = dados4.isnull().sum()
print(null_counts)


### ANÁLISE E VISUALIZAÇÃO GRÁFICA DO BANCO DE DADOS 


# GRÁFICO MATRIZ DE CORRELAÇÃO
colunas_para_correlacao = ['idade', 
    'tempo_exposicao_sdi', 
    'peso_diferenca',
    'pa_diferenca_sist',
    'pa_diferenca_diast',
    'fc_diferenca',
    'sat_o2_diferenca',
    'ar_cilindro_diferenca'
     ]  
dados_selecionados = dados4[colunas_para_correlacao]  
correlacao = dados_selecionados.corr()  
plt.figure(figsize=(12, 8))  
plt.imshow(correlacao, cmap='coolwarm', interpolation='none')  
plt.colorbar()  
plt.xticks(range(len(correlacao.columns)), correlacao.columns, rotation=90)  
plt.yticks(range(len(correlacao.columns)), correlacao.columns)  
plt.title('Matriz de Correlação')  
plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo
plt.savefig('grafico.png', dpi=300)
plt.show()







# GRAFICO DE DISPERSAO
eixo_x = dados4['idade']
eixo_y = dados4['tempo_exposicao_sdi']
plt.scatter(eixo_x, eixo_y)
plt.xlabel('Idade')
plt.ylabel('Tempo de exposição (SDI)')
plt.title('Relação entre idade e tempo de exposição (SDI)')
plt.show()


# GRAFICO DE BARRAS
contagem = dados4['genero'].replace({'M': 'Masculino', 'F': 'Feminino'}).value_counts()
colors = ['green' if x == 'Masculino' else 'red' for x in contagem.index]
contagem.plot(kind='bar', color=colors)
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.title('Distribuição por Gênero')
plt.ylim(0, 110)  # Ajusta a escala do eixo Y para 110

total = contagem.sum()
for i, v in enumerate(contagem):
    porcentagem = (v / total) * 100
    plt.text(i, v + 3, f'{porcentagem:.1f}%', color='black', ha='center')

plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo
plt.savefig('grafico.png', dpi=300)
plt.show()


# GRAFICO DE LINHA
y1 = dados4['tempo_exposicao_sdi']
y2 = dados4['sat_o2_diferenca']
y3 = dados4['ar_cilindro_diferenca']
plt.plot(y1, label='Tempo de exposição (SDI)')
plt.plot(y2, label='Saturação de O2')
plt.plot(y3, label='Diferença de Ar no Cilindro')
plt.ylabel('Frequência')
plt.xlabel('Tempo de exposição (SDI)')
plt.title('Relação entre idade e tempo de exposição (SDI) / Saturação O2 / Ar no Cilindro')
plt.legend()
plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo
plt.savefig('grafico.png', dpi=300)
plt.show()




### GRAFICO DE LINHA - NORMATIZAÇÃO DOS VALORES 0 - 100%

# Normalização dos dados para porcentagens  
def normalize_to_percentage(data):  
    return ((data - data.min()) / (data.max() - data.min())) * 100  

# Aplicar a normalização  
y1 = normalize_to_percentage(dados4['tempo_exposicao_sdi'])  
y2 = normalize_to_percentage(dados4['sat_o2_diferenca'])  
#y3 = normalize_to_percentage(dados4['ar_cilindro_diferenca'])  

# GRAFICO DE LINHA  
plt.plot(y1, label='Tempo de Exposição (SDI)')  
plt.plot(y2, label='Saturação de O2')  
#plt.plot(y3, label='Diferença de Ar no Cilindro') 
plt.grid() 
plt.ylabel('Frequência (%)')  
plt.xlabel('Combatentes')  
plt.title('Relação entre Tempo de Exposição (SDI) / Saturação O2')  
plt.legend()  
plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo  
plt.savefig('grafico.png', dpi=300)  
plt.show()  



# GRAFICO NORMATIZAÇÃO COM SUBPLOTS DE 3 LINHAS  

# Normalização dos dados para porcentagens  
def normalize_to_percentage(data):  
    return ((data - data.min()) / (data.max() - data.min())) * 100  

# Aplicar a normalização  
y1 = normalize_to_percentage(dados4['tempo_exposicao_sdi'])  
y2 = normalize_to_percentage(dados4['sat_o2_diferenca'])  
y3 = normalize_to_percentage(dados4['ar_cilindro_diferenca'])  

# GRAFICO DE LINHA  
fig, axs = plt.subplots(3, 1, figsize=(10, 15))  
axs[0].plot(y1, label='Tempo de Exposição (SDI)', color='blue')  
#axs[0].set_title('Tempo de Exposição (SDI)')  
axs[1].plot(y2, label='Saturação de O2' , color='green')  
#axs[1].set_title('Saturação de O2')  
axs[2].plot(y3, label='Diferença de Ar no Cilindro', color='red')  
#axs[2].set_title('Diferença de Ar no Cilindro')  

for ax in axs:  
    ax.grid()  
    ax.set_xlabel('Combatentes')  
    ax.set_ylabel('Frequência (%)')  
    ax.legend()  

# Ajustar o espaço entre os subgráficos  
plt.subplots_adjust(hspace=2.0)  # Aumente o valor para mais espaço  

plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo  
plt.savefig('grafico.png', dpi=300)  
plt.show()  



# GRAFICO DE BARRAS NA HORIZONTAL  
plt.figure(figsize=(12, 10))  # Tamanho da figura (largura, altura) 
y = dados4['combatente']  
x = dados4['fc_diferenca']  
plt.barh(y, x, height=0.5)  
plt.xlabel('Diferença de FC', fontsize=12)  # Ajuste o tamanho da fonte do eixo X  
plt.ylabel('Combatentes', fontsize=8)  # Ajuste o tamanho da fonte do eixo Y 
plt.title('Relação entre Combatentes e Diferença de FC')  
# Remover os rótulos do eixo Y  
plt.yticks([])  # Remove os rótulos do eixo Y
plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo  
plt.savefig('grafico.png', dpi=300)  
plt.show()



### HISTOGRAMA

# Histograma de ar_cilindro_diferenca  
plt.figure(figsize=(10, 5))  
sns.histplot(dados4['ar_cilindro_diferenca'], bins=20, kde=True)  
plt.title('Histograma de Diferença de Ar no Cilindro')  
plt.xlabel('Diferença de Ar no Cilindro')  
plt.ylabel('Frequência')  
plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo  
plt.savefig('grafico.png', dpi=300)  
plt.show()


# GRAFICO PIZZA

#Quantiles de tempo_exposicao_sdi
q1 = dados4['tempo_exposicao_sdi'].quantile(0.25)
q2 = dados4['tempo_exposicao_sdi'].quantile(0.50)
q3 = dados4['tempo_exposicao_sdi'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
dados4 = dados4[dados4['tempo_exposicao_sdi'].between(limite_inferior, limite_superior)]

# gRAFICO DE PIZZA DOS QUANTILES
plt.figure(figsize=(10, 5))  
plt.pie([q1, q2, q3], labels=['Quantil 1', 'Quantil 2', 'Quantil 3'], autopct='%1.1f%%')  
plt.title('Quantiles de Tempo de Exposição (SDI)')  
plt.legend()
plt.tight_layout()  # Ajusta o tamanho do gráfico para acomodar a legenda e os rótulos do eixo  
plt.savefig('grafico.png', dpi=300)  
plt.show()

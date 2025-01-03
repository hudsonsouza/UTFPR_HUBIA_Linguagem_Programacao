import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
import os  

# 1. Carregar os dados corretamente  
# Supondo que o arquivo CSV tenha cabeçalhos e os dados estejam no formato correto  
dados2 = np.genfromtxt('banco/banco_bombeiros-dados-tratados-2.csv', delimiter=',', skip_header=0, names=True, dtype=None, encoding=None)  

print('\nNomes das colunas do Banco de Dados Original:')
print(dados2.dtype.names) 

print('\nTipos das colunas do Banco de Dados:')
print(dados2.dtype)

print('\nConteudo das colunas do Banco de Dados:') 
print(dados2[:10]) 


print('\n### CONVERTENDO TIPOS DE DADOS ###\n')


# 2. Criar um novo array estruturado com os tipos desejados  
dados3 = np.empty(dados2.shape, dtype=[  
    ('idade', 'i8'),  
    ('tempo_exposicao_sdi', 'i8'),  
    ('peso_antes', 'f8'),  
    ('peso_depois', 'f8'),  
    ('peso_diferenca', 'f8'),  
    ('pa_antes_sist', 'i8'),  
    ('pa_antes_diast', 'i8'),  
    ('pa_depois_sist', 'i8'),  
    ('pa_depois_diast', 'i8'),  
    ('pa_diferenca_sist', 'i8'),  
    ('pa_diferenca_diast', 'i8'),  
    ('fc_antes', 'i8'),  
    ('fc_depois', 'i8'),  
    ('fc_diferenca', 'i8'),  
    ('sat_o2_antes', 'i8'),  
    ('sat_o2_depois', 'i8'),  
    ('sat_o2_diferenca', 'i8'),  
    ('ar_cilindro_antes', 'i8'),  
    ('ar_cilindro_depois', 'i8'),  
    ('ar_cilindro_diferenca', 'i8')  
])  


# Substituir NaN e valores do tipo 'int' por 0 || 'float' por 0.0
dados3['idade'] = np.nan_to_num(dados2['idade'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int
dados3['tempo_exposicao_sdi'] = np.nan_to_num(dados2['tempo_exposicao_sdi'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['peso_antes'] = np.nan_to_num(dados2['peso_antes'], nan=0.0).astype('f8')  # Substitui NaN por 0.0 e converte para float  
dados3['peso_depois'] = np.nan_to_num(dados2['peso_depois'], nan=0.0).astype('f8')  # Substitui NaN por 0.0 e converte para float  
dados3['peso_diferenca'] = np.nan_to_num(dados2['peso_diferenca'], nan=0.0).astype('f8')  # Substitui NaN por 0.0 e converte para float  
dados3['pa_antes_sist'] = np.nan_to_num(dados2['pa_antes_sist'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['pa_antes_diast'] = np.nan_to_num(dados2['pa_antes_diast'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['pa_depois_sist'] = np.nan_to_num(dados2['pa_depois_sist'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['pa_depois_diast'] = np.nan_to_num(dados2['pa_depois_diast'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['pa_diferenca_sist'] = np.nan_to_num(dados2['pa_diferenca_sist'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['pa_diferenca_diast'] = np.nan_to_num(dados2['pa_diferenca_diast'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['fc_antes'] = np.nan_to_num(dados2['fc_antes'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['fc_depois'] = np.nan_to_num(dados2['fc_depois'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['fc_diferenca'] = np.nan_to_num(dados2['fc_diferenca'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['sat_o2_antes'] = np.nan_to_num(dados2['sat_o2_antes'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['sat_o2_depois'] = np.nan_to_num(dados2['sat_o2_depois'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['sat_o2_diferenca'] = np.nan_to_num(dados2['sat_o2_diferenca'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['ar_cilindro_antes'] = np.nan_to_num(dados2['ar_cilindro_antes'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['ar_cilindro_depois'] = np.nan_to_num(dados2['ar_cilindro_depois'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  
dados3['ar_cilindro_diferenca'] = np.nan_to_num(dados2['ar_cilindro_diferenca'], nan=0).astype('i8')  # Substitui NaN por 0 e converte para int  


# 4. Exibir o novo array com os tipos convertidos  
print('\nTipos das colunas do Banco de Dados:')  
print(dados3.dtype) 

print('\nConteudo das colunas do Banco de Dados:') 
print(dados2[:10]) 

# 5. Análise com NumPy  
print("\nAnálise descritiva utilizando NumPy:")  
def estatisticas_descritivas(data, nome):  
    print(f"{nome} - Média: {np.mean(data):.2f}, Mediana: {np.median(data):.2f}, Desvio Padrão: {np.std(data):.2f}")  

# Calcular estatísticas descritivas  
estatisticas_descritivas(dados3['idade'], "Idade")  
estatisticas_descritivas(dados3['tempo_exposicao_sdi'], "Tempo Exposição SDI")  
estatisticas_descritivas(dados3['peso_diferenca'], "Variação Peso")  
estatisticas_descritivas(dados3['pa_diferenca_sist'], "Variação PA Sistólica")  
estatisticas_descritivas(dados3['pa_diferenca_diast'], "Variação PA Diastólica")  
estatisticas_descritivas(dados3['fc_diferenca'], "Variação Função Cardíaca")  
estatisticas_descritivas(dados3['sat_o2_diferenca'], "Variação Saturação Oxigênio")  
estatisticas_descritivas(dados3['ar_cilindro_diferenca'], "Variação AR no Cilindro")  


# Lista de variáveis numéricas  
numerical_vars = ['idade', 'tempo_exposicao_sdi', 'peso_diferenca', 'pa_diferenca_sist', 'pa_diferenca_diast', 'fc_diferenca', 'sat_o2_diferenca', 'ar_cilindro_diferenca']  


### MOSTRA O GRAFICO NA TELA, E SALVA O GRAFICO NA PASTA APÓS FECHAR A JANELA ###

def plot_and_save_histogram(var):  
    plt.figure(figsize=(10, 5))  
    sns.histplot(dados3[var], bins=20, kde=True)  
    plt.title(f'Histograma de {var}')  
    plt.xlabel(var)  
    plt.ylabel('Frequência')  
    
    # Exibir o gráfico  
    plt.show()  
    
    # Salvar o gráfico após o fechamento da janela  
    plt.savefig(os.path.join(caminho_salvar, f'histograma-{var}.png'))  
    plt.close()  # Fecha a figura para liberar memória  

def plot_and_save_boxplot(var):  
    plt.figure(figsize=(10, 5))  
    sns.boxplot(y=dados3[var])  # Usando dados3 para o boxplot na vertical  
    plt.title(f'Boxplot de {var}')  
    plt.ylabel(var)  
    plt.xlabel('')  # Rótulo do eixo x (opcional, pode ser deixado vazio)  
    
    # Exibir o gráfico  
    plt.show()  
    
    # Salvar o gráfico após o fechamento da janela  
    plt.savefig(os.path.join(caminho_salvar, f'boxplot-{var}.png'))  
    plt.close()  # Fecha a figura para liberar memória  

# Loop para plotar e salvar histogramas  
for var in numerical_vars:  
    plot_and_save_histogram(var)  

# Loop para plotar e salvar boxplots  
for var in numerical_vars:  
    plot_and_save_boxplot(var)  



### NÃO MOSTRA O GRAFICO NA TELA, MAS SALVA AUTOMATICAMENTE NA PASTA ###

# Tipo de Visualização  
sns.set(style="whitegrid")  

# Caminho para salvar os gráficos  
caminho_salvar = "/home/hudson/hudson2024/insync/site/miniconda3/projetos/UTFPR_HUBIA_Linguagem_Programacao/banco/img/"  

# Loop para plotar e salvar histogramas  
for var in numerical_vars:  
    plt.figure(figsize=(10, 5))  # Ajuste o tamanho da figura conforme necessário  
    try:  
        sns.histplot(dados3[var], bins=20, kde=True)  
        plt.title(f'Histograma de {var}')  
        plt.xlabel(var)  
        plt.ylabel('Frequência')  
        
        # Salvar o gráfico  
        plt.savefig(os.path.join(caminho_salvar, f'histograma-{var}.png'))  
        plt.close()  # Fecha a figura para liberar memória  
    except Exception as e:  
        print(f"Erro ao plotar Histograma {var}: {e}")  

# Loop para plotar e salvar boxplots  
for var in numerical_vars:  
    plt.figure(figsize=(10, 5))  # Ajuste o tamanho da figura conforme necessário  
    try:  
        sns.boxplot(y=dados3[var])  # Usando dados3 para o boxplot na vertical  
        plt.title(f'Boxplot de {var}')  
        plt.ylabel(var)  
        plt.xlabel('')  # Rótulo do eixo x (opcional, pode ser deixado vazio)  
        
        # Salvar o gráfico  
        plt.savefig(os.path.join(caminho_salvar, f'boxplot-{var}.png'))  
        plt.close()  # Fecha a figura para liberar memória  
    except Exception as e:  
        print(f"Erro ao plotar Boxplots {var}: {e}") 
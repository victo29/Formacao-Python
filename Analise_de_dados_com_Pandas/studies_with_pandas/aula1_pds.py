import pandas as pd

df = pd.read_csv("D:\Victor\Documents\VSAprendizado\Estudos\Formacao_Python\Analise_de_dados_com_Pandas\studies_with_pandas\datasets\Gapminder.csv",  on_bad_lines='skip', sep=";")


df  = df.rename(columns={'country':'Pais', 'continent':'Continente', 'year':'Ano', 'lifeExp':'Expectativa de vida', 'pop':'pop Total', 'gdpPercap': 'PIB'})

print(df.head(10))

# print("-----------------------")
# print( df.shape )#Retorna o total de linhas e colunas
# print("-----------------------")
# print( df.columns ) #retorna o nome das colunas
# print("-----------------------")
# print( df.dtypes ) # retorna o tipo de dados de cada coluna

# print("-----------------------")


# print( df.tail(15) ) # ULtimas linhas


# print("-----------------------")

# print( df.describe() ) # mostra estatisticas de todos os dados da tabela

# print('-------------------------')

# print(df["Continente"].unique()) # Retorna somente os valores unicos da coluna que foi passada

# print("------------------------")
# Oceania = df.loc[ df['Continente'] == "Oceania" ] # Utilização de filtros na base de dados
# print(Oceania.head)

print('--------------------------')
print(df.groupby('Continente')["Pais"].nunique()) 
""" 
Nesse caso retorna quantos paises distintos se tem em cada continente, utilizaçaão do group by estilo sql
""" 


print(' -------------------------- ')
print(df.groupby("Ano")['Expectativa de vida'].mean())
"""
Retorna a média da Expectativa de vida em cada ano    
"""


print(' -------------------------- ')
print(df['PIB'].mean())
"""
    Média do Pib
    .sum() -> retorna a soma
"""


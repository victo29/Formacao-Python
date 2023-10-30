import pandas as pd
# Planilhas Excel

df1 = pd.read_excel("studies_with_pandas\datasets\Aracaju.xlsx")
df2 = pd.read_excel("studies_with_pandas\datasets\Fortaleza.xlsx")
df3 = pd.read_excel("studies_with_pandas\datasets\cNatal.xlsx")
df4 = pd.read_excel("studies_with_pandas\datasets\Recife.xlsx")
df5 = pd.read_excel("studies_with_pandas\datasets\Salvador.xlsx")
"""
Lendo os arquivos em formato de planilhas do excel
"""

df = pd.concat([df1,df2,df3,df4,df5])
"""
Concatenando todas as tabelas em uma só
"""

print(df.sample(5))
"""
Retorna 5 exemplos de dados dentro da tabela
"""

print("------------------")
print(df.dtypes)


df["LojaID"] = df["LojaID"].astype("object")
"""
Alterando o tipo de dados da coluna LojaID para Object, não seria necessário ter eles como int
pois não seriam utilizados em operações
""" 

print("------------------")

print(df.dtypes)

print("------------------")

print(df.isnull().sum())
"""
Retorna a quantidade de valores nulos encontrados em cada coluna
"""

df['Vendas'].fillna(df["Vendas"].mean(), inplace=True)
"""
Esta linha de codigo está substituindo todos os valores nulos de "Vendar pela média. O "inplace = True" faz com que a alteração
seja feita na memória
"""
print("------------------")

print(df.isnull().sum())

"""
-> df.dropna( inplace=True )

Simplesmente apaga todas as linhas que contém valores nulos
"""


"""
-> df.dropna( subset= ['Vendas'],inplace=True )

Apaga todas as  linhas que contém os dados da coluna 'Vendas' com valores nulos
"""


"""
-> df.dropna( how='all',inplace=True )

Apaga todas as  linhas que contém os dados de todas as colunas com valores nulos
"""

print('-----------------------')
df['Receita'] = df['Vendas'].mul(df['Qtde'])
"""
Cria uma nova coluna com os dados sendo a multiplicação da coluna 'Vendas' com a coluna 'Qtde'
"""

print(df.head())

df["Receita"].max() #Retorna o maior valor da coluna
df["Receita"].min() #Retorna o menotr valor da coluna receita

print("----------------------")
print( df.nlargest(3,"Receita") )
"""
Retorna as três linhas onde apresentam as maiores receitas
"""

print("----------------------")
print( df.nsmallest(3,"Receita") )
"""
Retorna as três linhas onde apresentam as menores receitas
"""

print("----------------------")
print( df.groupby("Cidade")['Receita'].sum() )
"""
Retorna  a soma das receitas de cada cidades
"""


print("----------------------")
print( df.sort_values("Receita", ascending=False).head(10) )
"""
-> df.sort_values("Receita", ascending=False)

Ordena as linhas em ordem decrescente por Receita 
"""

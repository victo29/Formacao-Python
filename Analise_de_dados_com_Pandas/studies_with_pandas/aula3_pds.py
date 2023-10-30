import pandas as pd

df1 = pd.read_excel("studies_with_pandas\datasets\Aracaju.xlsx")
df2 = pd.read_excel("studies_with_pandas\datasets\Fortaleza.xlsx")
df3 = pd.read_excel("studies_with_pandas\datasets\cNatal.xlsx")
df4 = pd.read_excel("studies_with_pandas\datasets\Recife.xlsx")
df5 = pd.read_excel("studies_with_pandas\datasets\Salvador.xlsx")

df = pd.concat([df1,df2,df3,df4,df5])

df['Vendas'].fillna(df["Vendas"].mean(), inplace=True)

# df["Data"] = pd.to_datetime(df["Data"])
"""
Transforma o os elementos presentes na coluna data em formato Date time
"""
df['Receita'] = df['Vendas'].mul(df['Qtde'])

print(df.groupby(df["Data"].dt.year)["Receita"].sum())
"""
Fazendo um agrupamento com base nos anos e somando todos as receitas referente a cada ano
"""

print("----------------------------")

df["Ano_Venda"] = df["Data"].dt.year
"""
Criando uma coluna com o ano de cada venda
 -> dt.day extrai somente o dia
 -> dt.month extrai somente o més
"""

print(df.sample(10))

print("----------------------------")

print(df["Data"].min()) # Data mais antiga

print("----------------------------")

df["Diferencia_dias"] = df["Data"] - df["Data"].min()
"""
Retorna a diferencia de dias da data para a data mínima
"""
print(df.sample(5))


print("----------------------------")

df["Trimestr_venda"] = df["Data"].dt.quarter
"""
Criando uma coluna onde contém o trimeste que foi feita a venda
"""

print(df.sample(5))

print("----------------------------")

vendas_marco_2019 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
"""
Criando uma tabela somente com as vendas do més de março e ano de 2019
"""

print(vendas_marco_2019.sample(10))



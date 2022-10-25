#IMPORTANDO BIBLIOTECA PANDAS
import pandas as pd

#IMPORTANDO BIBLIOTECA MATPLOTLIB.PYPLOT
#PARA VISUALIZAÇÃO DOS GRAFICOS
import matplotlib.pyplot as plt

#LEITURA DOS ARQUIVOS
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#VISUALIZANDO 5 PRIMEIRAS LINHAS
#print(df1.head())
#print(df2.head())

#JUNTANDO TODOS OS ARQUIVOS (concatenando)
df = pd.concat([df1, df2, df3, df4, df5])

#VISUALIZANDO UMA AMOSTRAGEM DO CONJUNTO DE DADOS
#print(df.sample(5))

#VERIFICANDO O TIPO DE DADO DE CADA COLUNA
#print(df.dtypes)

#ALTERANDO O TIPO DE DADO DE UMA COLUNA
df["LojaID"] = df["LojaID"].astype("object")
#print(df.dtypes) 

#TRATANDO VALORES FALTANTES
#VERIFICANDO VALORES NULOS NO NOSSO CONJUNTO DE DADOS
#print(df.isnull().sum())

#SUBSTITUINDO OS VALORES NULOS PELA MEDIA
#INPLACE=TRUE MODIFICA O OBJETO EM MEMORIA MODIFICANDO O ARQUIVO
df["Vendas"].fillna(df["Vendas"].mean(),inplace=True)


#SUBSTITUINDO OS VALORES NULOS POR ZERO
df["Vendas"].fillna(0, inplace=True)

#APAGANDO AS LINHAS COM VALORES NULOS
df.dropna(inplace=True)

#APAGANDO AS LINHAS COM VALORES NULOS COM BASE APENAS EM UMA DAS COLUNAS
df.dropna(subset=["Vendas"],inplace=True)

#REMOVENDO LINHAS QUE ESTEJAM COM VALORES FALTANTES EM TODAS AS COLUNAS
df.dropna(how="all",inplace=True)

#CRIANDO COLUNAS NOVAS
#a tag .mul multiplica os valores das colunas da esquerda pelos valores dentro de .mul()
df["Receita"] = df["Vendas"].mul(df["Qtde"])
#print(df.head())

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
#print(df.head())

#RETORNANDO O MAIOR VALOR
#print(df["Receita"].max())

#RETORNANDO O MENOR VALOR
#print(df["Receita"].min())

#METODOS NLARGEST E NSMALLEST
#RETORNA TOP MAIORES E MENORES VALORES RESPECTIVAMENTE COM SUAS ESPECIFICAÇOES
#nlargest top 5
#print(df.nlargest(5, "Receita"))

#nsmallest top 5
#print(df.nsmallest(5, "Receita"))

#AGRUPAMENTO POR GRUPO
#print(df.groupby("Cidade")["Receita"].sum())

#ORDENANDO O CONJUNTO DE DADOS
#ASCENDING=fALSE TRÁS O RESULTADO DO MAIOR PARA O MENOR
#print(df.sort_values("Receita", ascending=False).head(10))

#TRABALHANDO COM DATAS
#TRANSFORMANDO A COLUNA DE DATA EM TIPO INTEIRO
df["Data"] = df["Data"].astype("int64")
#print(df.dtypes)

#TRANSFORMANDO A COLUNA DE DATA EM TIPO DATA
df["Data"] = pd.to_datetime(df["Data"])
#print(df.dtypes)

#AGRUPAMENTO POR ANO
#print(df.groupby(df["Data"].dt.year)["Receita"].sum())

#CRIANDO UMA NOVA COLUNA COM O ANO
df["Ano_Venda"] = df["Data"].dt.year
#print(df.sample(15))

#EXTRAINDO O MÊS E O DIA
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
#print(df.sample(15))

#RETORNANDO A DATA MAIS ANTIGA
#print(df["Data"].min())

#CALCULANDO A DIFERENÇA DE DIAS
df["diferenca_dias"] = df["Data"] - df["Data"].min()
#print(df.sample(15))

#CRIANDO A COLUNA DE TRIMESTRE
df["trimestre_venda"] = df["Data"].dt.quarter
#print(df.sample(15))

#FILTRANDO
#FILTRANDO AS VENDAS DE 2019 DO MÊS DE MARÇO
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
#print(vendas_marco_19.sample(15))

#VISUALIZAÇÃO DE DADOS
#MÉTODO VALUE_COUNTS (faz uma contangem de quantas linhas tem determinado item)
print(df["LojaID"].value_counts(ascending=False))

#GRÁFICO DE BARRAS
#df["LojaID"].value_counts(ascending=False).plot.bar();
#plt.show()

#GRÁFICO DE BARRAS HORIZONTAIS
#df["LojaID"].value_counts(ascending=True).plot.barh();
#plt.show()

#GRÁFICO DE PIZZA
#df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie();
#plt.show()

#VISUALIZANDO O TOTAL DE VENDAS POR CIDADE
print(df["Cidade"].value_counts())

#ADICIONANDO UM TÍTULO E ALTERANDO O NOME DOS EIXOS
#df["Cidade"].value_counts().plot.bar(title="Total vendas por cidade")
#plt.show()

#ALTERANDO A COR
#df["Cidade"].value_counts().plot.bar(title="Total vendas por cidade", color="grey")
#plt.show()

#ALTERANDO O ESTILO
#plt.style.use("ggplot")
#df.groupby(df["mes_venda"])["Qtde"].sum().plot(title="Total produtos vendidos por mês")
#plt.xlabel("Mês")
#plt.ylabel("Total produtos vendidos")
#plt.legend()
#plt.show()

print(df.groupby(df["mes_venda"])["Qtde"].sum())

#SELECIONANDO APENAS AS VENDAS DE 2019 UTILIZANDO UMA VARIÁVEL
df_2019 = df[df["Ano_Venda"] == 2019]
print(df_2019.sample(5))

#GRÁFICO TOTAL DE PRODUTOS VENDIDOS POR MẼS
#plt.style.use("ggplot")
#df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
#plt.xlabel("Mês")
#plt.ylabel("Total produtos vendidos")
#plt.legend()
#plt.show()

#PLOTANDO UM HISTOGRAMA
#plt.hist(df["Qtde"], color="green")
#plt.show() 

#PLOTANDO GRAFÍCO DE DISPERSÃO (SCATTER PLOT)
#plt.scatter(x=df_2019["dia_venda"], y=df_2019["Receita"]);
#plt.show()

#SALVANDO EM PNG
plt.style.use("ggplot")
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.xlabel("Mês")
plt.ylabel("Total produtos vendidos")
plt.legend()
plt.savefig("grafico-Qtde-vs-mes.png")
plt.show()
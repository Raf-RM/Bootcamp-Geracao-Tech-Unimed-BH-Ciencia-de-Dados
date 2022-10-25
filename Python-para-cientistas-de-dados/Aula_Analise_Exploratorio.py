#IMPORTANDO AS BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#CRIANDO O DATAFRAME
df = pd.read_excel("AdventureWorks.xlsx")
print(df.head())

#QUANTIDADE DE LINHAS
print(df.shape)

#VERIFICANDO OS TIPOS DE DADOS
print(df.dtypes)

#VERIFICANDO RECEITA TOTAL
print(df["Valor Venda"].sum())

#VERIFICANDO O CUSTO TOTAL
#round( ,2) arredonda para "2" casas decimais o valor
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])
print(round(df["custo"].sum(), 2))

#VERIFICANDO O LUCRO (RECEITA menos CUSTO)
df["lucro"] = df["Valor Venda"] - df["custo"]
print(round(df["lucro"].sum(), 2))

#VERIFICANDO TEMPO DE ENVIO 
#criando coluna com total de dias para enviar produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

#VERIFICANDO MEDIA DO TEMPO DE ENVIO PARA CADA MARCA
#ESTRAINDO APENAS OS DIAS
#.dt.days extrai somente o número de dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print(df.head())
print(df["Tempo_envio"].dtype)
#OBTENDO A MEDIA
print(df.groupby("Marca")["Tempo_envio"].mean())

#VALORES FALTANTES
print(df.isnull().sum())

#VERIFICANDO LUCRO POR ANO E MARCA (AGRUPAMENTO POR ANO E MARCA)
print(df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())
#FORMATANDO OS VALORES ANTERIORES E TIRANDO NOTAÇÃO CIENTIFICA
pd.options.display.float_format = '{:20,.2f}'.format
print(df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())

#RESETANDO O INDEX PARA ESCREVER EM FORMATO COLUNAR (DATAFRAME)
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
print(lucro_ano)

#VERIFICANDO TOTAL DE PRODUTOS VENDIDOS
print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

#GRAFICO TOTAL DE PRODUTOS VENDIDOS
#df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
#plt.show()

#GRAFICO LUCRO VS ANO
#df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
#plt.xlabel("Ano")
#plt.ylabel("Receita");
#plt.show()

#VERIFICANDO APENAS AS VENDAS DO ANO DE 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
print(df_2009.sample(5))

#GRAFICO LUCRO POR MES NO ANO DE 2009
#df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mes")
#plt.xlabel("Mês")
#plt.title("Lucro")
#plt.show()

#GRAFICO LUCRO POR MARCA NO ANO DE 2009
#df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
#plt.xlabel("Marca")
#plt.title("Lucro")
#plt.xticks(rotation="horizontal") #rotaciona a legenda do eixo x
#plt.show()

#GRAFICO LUCRO POR CLASSE NO ANO DE 2009
#df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
#plt.xlabel("Classe")
#plt.title("Lucro")
#plt.xticks(rotation="horizontal") #rotaciona a legenda do eixo x
#plt.show()

#ANALISES ESTATISTICAS
print(df["Tempo_envio"].describe())

#GRAFICO DE BOXPLOT
#plt.boxplot(df["Tempo_envio"])
#plt.show()

#HISTOGRAMA TEMPO DE ENVIO
plt.hist(df["Tempo_envio"])
plt.show()

#TEMPO MÍNIMO DE ENVIO
print(df["Tempo_envio"].min())

#TEMPO MÁXIMO DE ENVIO
print(df["Tempo_envio"].max())

#IDENTIFICANDO O OUTLIER (PONTO QUE PARECE ESTAR FORA DO GRAFICO BOXPLOT)
print(df[df["Tempo_envio"] == 20])

#SALVANDO A ANÁLISE EM UM NOVO ARQUIVO (EXCEL OU CSV)
#INDEX=FALSE RETIRA O ÍNDICE DAS LINHAS
df.to_csv("df_vendas_novo.csv", index = False)


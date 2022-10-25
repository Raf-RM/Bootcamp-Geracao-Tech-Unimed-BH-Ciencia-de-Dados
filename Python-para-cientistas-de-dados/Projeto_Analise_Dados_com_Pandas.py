#IMPORTANTO A BIBLIOTECA PANDAS
import pandas as pd

#ERROR_BAD_LINES=FALSE VAI IGNORAR QUALQUER ERROR QUE ELE ENCONTRAR E PULAR AQUELA LINHA
#SEP=";" VAI INDICAR PARA O PANDAS QUE O SEPARADOR É UM ";" E NÃO "," COMO É POR DEFAULT
data_frame = pd.read_csv("Gapminder.csv", error_bad_lines = False, sep = ";")

#VISUALIZANDO AS 5 PRIMEIRAS LINHAS (head() pode receber argumento exmeplo head(10) para retornar as 10 primeiras)
print(data_frame.head())

#ALTERANDO O NOME DAS COLUNAS
data_frame = data_frame.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de Vida", "pop":"Populacao Total", "gdpPercap":"PIB"})
print(data_frame.head(10))

#CONHECENDO O TOTAL DE LINHAS E COLUNAS NO ARQUIVO
print(data_frame.shape)

#RETORNANDO SOMENTE NOME DAS COLUNAS
print(data_frame.columns)

#RETORNANDO O TIPO DE DADO EM CADA COLUNA
print(data_frame.dtypes)

#VISUALIZANDO AS ÚLTIMAS LINHAS DO CONJUNTO DE DADOS (tail também recebe argumento exemplo tail(10) retornando as ultimas 10)
print(data_frame.tail())

#MÉTODO describe() RETORNA INFORMAÇÕES ESTATÍSTICAS DO CONJUNTO DE DADOS
#COUNT -> TOTAL DE LINHAS PARA CADA COLUNA
#MEAN -> MÉDIA PARA CADA COLUNA
#STD -> DESVIO PADRÃO PARA CADA COLUNA
#MIN -> VALOR MÍNIMO PARA CADA COLUNA
#25%, 50%, 75% -> QUARTIS PARA CADA COLUNA (50% EQUIVALENTE A MEDIANA)
#MAX -> VALOR MÁXIMO PARA CADA COLUNA  
print(data_frame.describe())

#VISUALIZANDO OS VALORES UNICOS DE UMA COLUNA (SEM REPETIÇÃO)
print(data_frame["Continente"].unique())

#VISUALIZANDO VALORES ESPECÍFICOS (método loc para localizar) UTILIZANDO LOC COMO FILTRO NA NOSSA BASE DE DADOS
oceania = data_frame.loc[data_frame["Continente"] == "Oceania"]
print(oceania.head())

#FAZENDO AGRUPAMENTO DE DADOS
#No exemplo fizemos uma contagem distinta com .nunique do número de países em cada continente
print(data_frame.groupby("Continente")["Pais"].nunique())

#Outro exemplo calculando a expectativa de vida média para cada ano utilizando groupby e .mean() (.mean() retorna a média)
print(data_frame.groupby("Ano")["Expectativa de Vida"].mean())

#FAZENDO SOMAS DAS LINHAS DE UMA COLUNA
print(data_frame["PIB"].sum())

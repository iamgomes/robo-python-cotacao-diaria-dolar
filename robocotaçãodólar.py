import pandas as pd
from datetime import date

#https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

#Código da tabela no SGS - Sistema Gerenciador de Séries Temporais
codSerie = '1'

dataInicial = '01/01/1997'
dataFinal = date.today().strftime('%d/%m/%Y')

print('Período dos dados: {} a {}'.format(dataInicial, dataFinal))

print('Acessando API do Banco Central...')
url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}&dataFinal={}'.format(codSerie,dataInicial,dataFinal)

print('Retornando os dados...')
df = pd.read_json(url)
df.set_index('data', inplace=True)

print('Salvando os dados em arquivo csv...')
#Exporta a consulta em arquivo csv
df.to_csv('PreçoDólar.csv', sep=';')

print('Arquivo salvo com sucesso!')
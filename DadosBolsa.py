import yfinance as yf
import pandas as pd
import numpy as np

pd.set_option('display.min_rows', 50)
pd.set_option('display.max_rows', 200)


def busca_carteira_teorica(indice, nome):
    url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteira' \
          'Teorica.aspx?Indice={}&idioma=pt-br'.format(indice.upper())
    dadosB3 = pd.read_html(url, decimal=',', thousands='.', index_col="Código")[0][:-1]
    dadosB3.to_excel(r'C:\Users\gabri\Desktop\Testes\{}.xlsx'.format(nome))



busca_carteira_teorica('ibov', 'dados')


def get_tickers(indice):
    url = 'http://bvmf.bmfbovespa.com.br/indices/Resumo' \
          'CarteiraTeorica.aspx?Indice={}&idioma=pt-br'.format(indice.upper())
    return (pd.read_html(url, decimal=',', thousands='.', index_col="Código")[0][:-1].index + '.SA').to_list()


t = get_tickers('ibov')

ibov = yf.download(t, period='1mo', group_by='ticker')
ibov.to_excel(r'C:\Users\gabri\Desktop\Testes\DadosIBOV.xlsx')

ifix = yf.download(get_tickers('ifix'), period='1mo', group_by='ticker')


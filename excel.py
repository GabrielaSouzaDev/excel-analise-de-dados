# Autor: Gabriela Souza
# Projeto de analise de dados de Excel

# importação do pandas
import pandas as pd

# ler planilha do excel
planilha = pd.read_excel('ocupacao.xlsx')

# agrupar os registros por nome e realizar os cálculos
resultado = planilha.groupby(['Registro', 'Nome'])['Horas'].sum()

# loop para exibir os resultados
for (registro,nome), horas in resultado.items():
    print(f'{registro} - {nome} -> {horas} horas')
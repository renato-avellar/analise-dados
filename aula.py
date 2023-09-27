import pandas as pd
import plotly.express as px

tabela = pd.read_csv('cancelamentos_sample.csv')
tabela = tabela.drop(columns="CustomerID")
tabela = tabela.dropna()

print(tabela)

agrupamento = tabela.groupby("duracao_contrato").mean(numeric_only=True)
print(agrupamento)

print(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='cancelou')
    grafico.write_html(f"grafico_{coluna}.html")

tabela = tabela[tabela['duracao_contrato'] != 'Monthly']
print(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}".format))

tabela = tabela[tabela['ligacoes_callcenter'] < 5]
print(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}".format))

tabela = tabela[tabela['dias_atraso'] <= 20]
print(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}".format))


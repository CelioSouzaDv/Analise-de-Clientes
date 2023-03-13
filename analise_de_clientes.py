# -*- coding: utf-8 -*-
"""Analise de Clientes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kSo76PFBIyTcRBK-Tagb8HNz86Ypszky

# Análise de dados na linguagem Python.
# Nessa análisei irei descobrir o motivo ou motivos que estão levando os clientes de uma indeterminada empresa de cartôes a cancelarem os seus cartões.
"""

#PANDAS é a blibioteca para importar tabelas, utilizando o comando pd.read_TIPO DE ARQUIVO
#Quando se quer exclui uma linha ou coluna, deve-se utilizar o comando 'DROP' axis=0 para linha e axis=1 para coluna



import pandas as pd
import plotly.express as px


table = pd.read_csv('/content/drive/MyDrive/python-estudos/ClientesBanco.csv', encoding='latin1')
table = table.drop('CLIENTNUM', axis=1)
display (table)

"""# Agora vou tratar os valores vazios e exibir um resumo das colunas da base de dados.

"""

#display(NOME-DA-TABELA.info()) serve para voce pegar as informações resumidas da tabela
#NOME-DA-TABELA.dropna() serve para voce exluir todas linhas que estao com valores vazios ou nulos 
#display(NOME-DA-TABELA.describe()) serve para voce fazer um resumo (PRE DEFINIDO) da tabela selecionada.
# .round(QUANTIDADE DE CASAS APOS A VIRGULA) serve para "diminuir o numero da casas decimais apos a virgula"


table = table.dropna()
display(table.info())
display(table.describe().round(1))

"""# Agora vou avaliar a divisão entra Clientes x Cancelados."""

# NOME-DA-TABLEA["NOME-DA-COLUNA"].value_counts()comando para somar as linhas preenchidas com Texto
# (nomalize=true) conta as linhas em forma de porcentagem.


marginc_table = table['Categoria'].value_counts()
display(marginc_table)

marginc_table_p = table['Categoria'].value_counts(normalize=True)
display(marginc_table_p)

"""# Agora irei tentar descobrir por qual motivos os clientes estão cancelando seus cartões.
  - Irei comparar a relação "clientes x cancelados" com cada uma das colunas tentando encontrar os principais motivos.
"""

#px.histogram é o tipo de grafico utilizado em questão. px.histogram(NOME-DA-TABELA, x='NOME DA COLUNA', color='COLUNA-BASE')
# NOME-DO-GRAFICO.show() para exibir o grafico
# FOR- for colum in  table: Para cada coluna na minha tabela execute o camando
for column in table:
  graph = px.histogram(table, x=column, color='Categoria')
  graph.show()

"""# Informações retirada dos graficos
  - Aparentemente quanto menos produtos contratados menor a cance de cancelamento;
  - E os clientes que usam o cartão de forma mais esporadica, com menores valores de transações, menor numero de transações, maio período de inatividade, tendem a cancelar seus cartões;
  - Clientes que entram em contato mais vezes com a empresa acabam cancelando mais também, quanto maior o numero de contatos, maior a proporção de cancelamento;

# Possivel forma de reverter este quadro
  - Eu primeiramente criaria uma area de risco para cliente que entram em contato com a empresa por 2 ou mais vezes, criando um alarme e dando uma maior atenção para estes clientes. Investigando o motivo dos contatos e focando na resolução dos problemas apresentados.
  - Criar algum tipo de pojeto para induzir os clientes a utilizarem mais os seus cartôes, como sistema de recompensas (cash back, milhas, desconto em determinados serviços, desconto em estabelecimentos e etc). E melhorar as vantagens para quem contratar os serviços adicionais, ou fazer promoções especiais dos serviços da empresa para clientes inativos, com 2 ou mais meses de inatividade.
"""


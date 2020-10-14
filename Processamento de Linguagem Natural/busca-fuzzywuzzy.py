# pip install fuzzywuzzy, pandas, OrderedDict

from fuzzywuzzy import process
import pandas as pd
from collections import OrderedDict

# Cria a tabela com os dados
dados = OrderedDict({'Musica': ['Vem me Socorrer','Esperar é Caminhar', 'Esperar é Caminhar', 'Sê Valente', 
                                'Grandes Coisas', 'Grandes Coisas', 'Seu Sangue', 'Mil Cairão', 'Meus Votos'
                                , 'Emáus', 'Só Tu és Santo', 'Pra Onde eu Irei?'],
                    'Cantor': ['Marcos Almeida','Marcos Almeida','Marcos Almeida','Fernandinho',
                                     'Fernandinho','Fernandinho','Fernandinho','Morada','Morada','Morada',
                                     'Morada','Morada'],
                    'Albúm': ['Eu Sarau','Esperar é Caminhar','Eu Sarau','Teus sonhos','Grandes Coisas','Teus sonhos',
                              'Teus sonhos','Ele é','Ele é','Ele é','Ele é','Ele é']
                    })

dataset = pd.DataFrame(dados)

# Mostra a tabela criada
print(dataset)

txtPesquisa = input("\n Digite o que deseja pesquisar: ")
print("\n")

# Atribui o nome pesquisado as 3 colunas da tabela
try:  
    
    musica = process.extractOne(txtPesquisa, choices=dataset.Musica, score_cutoff=90)
    cantor = process.extractOne(txtPesquisa, choices=dataset.Cantor, score_cutoff=90)
    album = process.extractOne(txtPesquisa, choices=dataset.Albúm, score_cutoff=90)

except sr.UnkownValueError:
    print("Não foi encontrado")

if musica != None :
  # Cria uma tabela onde será mostrado o resultado da pesquisa
  tabelaResultado = OrderedDict({'Musica': [musica[0]]})
  dataset = pd.DataFrame(tabelaResultado)
  print(dataset)

elif cantor != None :
  # Cria uma tabela onde será mostrado o resultado da pesquisa
  tabelaResultado = OrderedDict({'Cantor': [cantor[0]]})
  dataset = pd.DataFrame(tabelaResultado)
  print(dataset)

elif album != None :
  # Cria uma tabela onde será mostrado o resultado da pesquisa
  tabelaResultado = OrderedDict({'Albúm': [album[0]]})
  dataset = pd.DataFrame(tabelaResultado)
  print(dataset)

else :
    print("Não foi encontrado")

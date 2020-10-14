#import nltk
#nltk.download('stopwords')

import urllib.request as url
from bs4 import BeautifulSoup
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz


# Texto da ementa original
ementa = "Introdução à inteligência artificial: histórico, conceitos básicos, áreas de aplicação, tendências. Métodos de resolução de problemas. Técnicas de busca: com e sem informação (heurística e meta-heurística – Algoritmos Genéticos). Aprendizado de máquina. Representação do conhecimento. Redes Neurais."
print("\n Ementa Original: ")
print(ementa)

# Abrindo o texto de um site
ementaSite = "https://www.ppgia.pucpr.br/~nievola/Ementa-IA.html"
pagina = url.urlopen(ementaSite)
soup = BeautifulSoup(pagina, 'html.parser')
textoSite = soup.find('p', attrs = {'align': 'JUSTIFY'}).get_text()

print("\n Ementa Site: ")
print(textoSite)

# Abrindo o texto de outro site
ementaSite2 = "https://educa.unitins.br/main/course_description/?cidReq=011001099&id_session=0&gidReq=0&gradebook=0&origin="
pagina2 = url.urlopen(ementaSite2)
soup2 = BeautifulSoup(pagina2, 'html.parser')
textoSite2 = soup2.find(id="breadcrumb-bar").get_text()

print("\n Ementa Site Secundário: ")
print(textoSite2)

# Comparando a similaridade entre os textos
comparacao = fuzz.ratio(ementa, textoSite)
comparacao2 = fuzz.ratio(ementa, textoSite2)

print("\n Similaridade entre a ementa e o texto do site: ")
print(comparacao)

print("\n Similaridade entre a ementa e o texto do site secundário: ")
print(comparacao2)

#import nltk
#nltk.download('stopwords')

from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

# Texto da ementa original
ementa = "Introdução à inteligência artificial: histórico, conceitos básicos, áreas de aplicação, tendências. Métodos de resolução de problemas. Técnicas de busca: com e sem informação (heurística e meta-heurística – Algoritmos Genéticos). Aprendizado de máquina. Representação do conhecimento. Redes Neurais."
print("\n Texto Original: ")
print(ementa)
print("\n")

# Separa o texto da ementa em sentenças/períodos
periodos = sent_tokenize(ementa)
print("\n Texto separado em Períodos: ")
print(periodos)
print("\n")

# Separa o texto da ementa em palavras e retira as stopwords e pontuações
palavras = word_tokenize(ementa)
palavras = [word.lower() for word in palavras if word.isalpha()]
periodo_puro = [word for word in palavras if word not in stopwords.words('portuguese')]
print("Texto com StopWords e pontuações retirados: ")
print(periodo_puro)

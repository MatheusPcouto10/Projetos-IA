# pip install nltk

from nltk.tokenize import RegexpTokenizer

#texto a ser tokenizado
texto = input("Digite o que deseja tokenizar: ")
print("\n")

# Padrão de tokenização separando vírgulas e pontos
tokenizer = RegexpTokenizer('\w+|[^\w\s]+')

print(tokenizer.tokenize(texto))


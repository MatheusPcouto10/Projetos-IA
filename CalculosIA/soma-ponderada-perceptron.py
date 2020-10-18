import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt

w1 = 0.45
w2 = 0.10
w0 = -1

x1 = [8, 1, 4, 2]
x2 = [3, 1, 2, 1]
f = []
classe = []

d1 = round(x1[0]*w1 + x2[0]*w2 + w0, 3)
d2 = round(x1[1]*w1 + x2[1]*w2 + w0, 3)
d3 = round(x1[2]*w1 + x2[2]*w2 + w0, 3)
d4 = round(x1[3]*w1 + x2[3]*w2 + w0, 3)

d = [d1, d2, d3, d4]

for i in d:
    if(i > 0.0):
        f.append(1)
        classe.append('A')
    else:
        f.append(-1)
        classe.append('B')


dados = OrderedDict({'Amostras': ['1','2', '3', '4'],
                    'X1': [x1[0], x1[1], x1[2], x1[3]],
                    'X2': [x2[0], x2[1], x2[2], x2[3]],
                    'd': [d[0], d[1], d[2], d[3]],
                    'f': [f[0], f[1], f[2], f[3]],
                    'Classe': [classe[0], classe[1], classe[2], classe[3]]
                    })

dataset = pd.DataFrame(dados)
print(dataset)

dadosGrafico = OrderedDict({'Amostras': [d[0], d[1], d[2], d[3]],
                            'Classe': [f[0], f[1], f[2], f[3]]
                           })

datasetGrafico = pd.DataFrame(dadosGrafico)
datasetGrafico.plot()
plt.show()

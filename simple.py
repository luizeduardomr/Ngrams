from nltk.util import ngrams
from collections import Counter
import os

nomearquivo = len(os.listdir('ngrams-results')) +1

f = open('/home/luiz/Desktop/Code/my-trigrama/resultados-ngramas/Folha/ECONOMIA/TURISMO/3.abr.2019 às 17h06 - Louco_por_lugares_re.txt', "r")
word_data = f.read()
with open(f'ngrams-results/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
    text.write(str(Counter(ngrams(word_data.split(), 3))))
f = open(f'ngrams-results/{nomearquivo}.txt', "r")
texto = f.read()
quebra = texto.split(', (')
quebra[0] = '(' + quebra[0].split('(')[2]
quebra[-1] = quebra[-1].split('})')[0]
with open(f'teste-resultados-ngramas/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
    text.write("\n(".join(quebra))
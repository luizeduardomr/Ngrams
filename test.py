from nltk.util import ngrams
from collections import Counter
import os
nomearquivo = len(os.listdir('ngrams-results')) +1

for root, dirs, files in os.walk('resultados-ngramas'):
    for file in files:
        filename, extension = os.path.splitext(file)
        if(extension =='.txt'):
            print('Processando arquivo:', os.path.join(root, file))
            f = open(f'{root}/{filename}{extension}', "r")
            word_data = f.read()
            with open(f'ngrams-results/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
                text.write(str(Counter(ngrams(word_data.split(), 3))))
            f = open(f'ngrams-results/{nomearquivo}.txt', "r")
            texto = f.read()
            quebra = texto.split(', (')
            quebra[0] = '(' + quebra[0].split('(')[2]
            quebra[-1] = quebra[-1].split('})')[0]
            with open(f'ngrams-results/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
                text.write("\n(".join(quebra))
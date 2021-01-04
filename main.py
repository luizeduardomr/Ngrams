from nltk.util import ngrams
from collections import Counter
import os

num=0
for root, dirs, files in os.walk('notícias/resultados-ngramas'):
    for file in files:
        nomearquivo = len(os.listdir('teste-resultados-ngramas')) +1

        # Pegar os arquivos do excel, botar em um .txt e ler cada linha
        # Separar pelos que serão excluídos
        # e aí ter que fazer vários 'if's para juntar as pastas..
        # os.walk if(rools)
        filename, extension = os.path.splitext(file)
        if(extension =='.txt'):
            print(num)
            num+=1
            #print(f'-------{filename[:20]}{extension}-----------')
            f = open(f'{root}/{filename}{extension}', "r")
            #print(f'{root}/{filename}{extension}\n')
            word_data = f.read()
            with open(f'teste-resultados-ngramas/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
                text.write(str(Counter(ngrams(word_data.split(), 3))))
            f = open(f'teste-resultados-ngramas/{nomearquivo}.txt', "r")
            texto = f.read()
            quebra = texto.split(', (')
            try:
                quebra[0] = '(' + quebra[0].split('(')[2]
            except:
                print(f'ERRO------------ {root}/{filename}{extension}')
                break
            quebra[-1] = quebra[-1].split('})')[0]
            with open(f'teste-resultados-ngramas/{nomearquivo}.txt', 'w', encoding='utf-8') as text:
                text.write("\n(".join(quebra))
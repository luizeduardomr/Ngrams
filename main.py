from nltk.util import ngrams
from collections import Counter
import os

num=0
for root, dirs, files in os.walk('notícias/automatico-organizado'):
    for file in files:
        filename, extension = os.path.splitext(file)
                    #nomearquivo = len(os.listdir('teste-resultados-ngramas')) +1
        # Coleta as informações do diretório atual   
        size = len(root.split('/'))
        rootbegin = root.split('/')[2:size]
        ano = rootbegin[0]
        jornal = rootbegin[1]
        if('-' in rootbegin[2]):
            keyword = rootbegin[2].split('-')[1]
        else:
            keyword = rootbegin[2]
        try:
            categoria = rootbegin[3]
        except:
            pass

        diretorio = f'teste-resultados-ngramas/{ano}/{jornal}/{keyword}/{categoria}'
        # Procura por arquivos .txt (as matérias) e abre a leitura delas
        if(extension =='.txt'):
            print(num)
            num+=1
            f = open(f'{root}/{file}', "r")
            word_data = f.read()

        if(os.path.exists(diretorio)):
            pass
        else:
            os.makedirs(diretorio)


        # Para cada matéria (.txt) cria um novo arquivo com o ngrama
        try:
            with open(f'{diretorio}/{filename}.txt', 'w', encoding='utf-8') as text:
                text.write(str(Counter(ngrams(word_data.split(), 3))))
            f = open(f'{diretorio}/{filename}.txt', "r")
            texto = f.read()
            quebra = texto.split(', (')
            try:
                quebra[0] = '(' + quebra[0].split('(')[2]
            except:
                print(f'ERRO------------ {root}/{filename}{extension}')
                break
            quebra[-1] = quebra[-1].split('})')[0]
            with open(f'{diretorio}/{filename}.txt', 'w', encoding='utf-8') as text:
                text.write("\n(".join(quebra))
        except:
            os.makedirs(diretorio)
            try:
                with open(f'{diretorio}/{filename}.txt', 'w', encoding='utf-8') as text:
                    text.write(str(Counter(ngrams(word_data.split(), 3))))
            except:
                print('erroooooooooooooooooooooooooo')
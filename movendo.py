from nltk.util import ngrams
from collections import Counter
import os

num=1
count = 0
Oldroot = ''
categoria = ''
Estadao = open('mover-Estadão.txt', 'r')
Folha = open('mover-Folha.txt', 'r')
LinesFolha = Folha.readlines() 
LinesEstadao = Estadao.readlines() 

for root, dirs, files in os.walk('notícias/resultados-filtro-automatico'):
    for file in files:
        for line in LinesFolha:
            # Pega as informações do arquivo
            filename, extension = os.path.splitext(file)         

            # Coleta as informações do diretório atual   
            size = len(root.split('/'))
            rootbegin = root.split('/')[2:size]
            ano = rootbegin[0]
            jornal = rootbegin[1]
            keyword = rootbegin[2]  #.split('-')[1]

            # Coleta as informações das pastas que está sendo lidas
            divide = line.split(',')
            movePasta = divide[0]
            newPasta = divide[1]
            divide = "/".join(divide)

            if('Estadão' in root): #Estadão ou Folha
                count+=1
                continue
            try:
                categoria = rootbegin[3]
            except:
                pass
            rootbegin = "/".join(rootbegin)
            if(f'{categoria}\n' == movePasta): #and root!=Oldroot):
                #Oldroot = root
                print(f'{num}! - {root}')
                for file in files:
                    os.remove(f'{root}/{file}')
                try:
                    os.rmdir(root)
                except:
                    pass
                num+=1
from nltk.util import ngrams
from collections import Counter
import os

num=1
count = 0
Oldroot = ''
categoria = ''
Estadao = open('excluir-Estadão.txt', 'r')
Folha = open('excluir-Folha.txt', 'r')
Tudo = open('excluir-tudo.txt', 'r')
LinesTudo = Tudo.readlines()
LinesFolha = Folha.readlines() 
LinesEstadao = Estadao.readlines() 

# tudo = 932
# Folha = 312
# Estadão = 491
# --- 803
for root, dirs, files in os.walk('notícias/resultados - filtro - automático'):
    for file in files:
        for line in LinesEstadao:
            filename, extension = os.path.splitext(file)            
            size = len(root.split('/'))
            rootbegin = root.split('/')[2:size]
            ano = rootbegin[0]
            jornal = rootbegin[1]
            keyword = rootbegin[2]  #.split('-')[1]
            if('Folha' in root): #Estadão ou Folha
                count+=1
                continue
            try:
                categoria = rootbegin[3]
            except:
                pass
            rootbegin = "/".join(rootbegin)
            if(f'{categoria}\n' == line and root!=Oldroot):
                Oldroot = root
                print(f'{num}! - {root}')
                num+=1
print(f'Count: {count}')
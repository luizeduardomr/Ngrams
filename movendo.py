from nltk.util import ngrams
from collections import Counter
import os
import shutil 

num=0
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
            if('-' in rootbegin[2]):
                keyword = rootbegin[2].split('-')[1]
            else:
                keyword = rootbegin[2]


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
            #print(f'{categoria} ---- {movePasta} >>>> {newPasta}', end="")
            if(f'{categoria}'== movePasta):  #and root!=Oldroot):
                #Oldroot = root
                print('--------------------------')
                for file in files:
                    if(os.path.exists(f'notícias/automatico-organizado/{ano}/{jornal}/{keyword}/{newPasta}')):
                        shutil.copy(f'{root}/{file}', f'notícias/automatico-organizado/{ano}/{jornal}/{keyword}/{newPasta}')
                        print(f'{num}! - {root}')
                        num+=1
                    else:
                        os.makedirs(f'notícias/automatico-organizado/{ano}/{jornal}/{keyword}/{newPasta}')
                        try:
                            shutil.copy(f'{root}/{file}', f'notícias/automatico-organizado/{ano}/{jornal}/{keyword}/{newPasta}')
                            print(f'{num}! - {root}\n')
                            num+=1
                            print('done! =)')
                        except:
                            print('erro pra mover a pasta')
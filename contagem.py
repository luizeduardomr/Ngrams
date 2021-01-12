from glob import glob
import os

sep = '\t'

extension = '.txt'
data = {}
rootdir = 'notícias/automatico-organizado'
names = ['ano', 'jornal', 'keyword', 'categoria']

for root, dirs, files in os.walk(rootdir):
    if len(dirs):
        continue

    elems = []
    amount = len(glob(os.path.join(root, f'*{extension}')))
    print (os.path.join(root, f'*{extension}'))

    while root != rootdir:
        root, entry = os.path.split(root)
        elems.append(entry)

    elems.reverse()

    folderdata = dict(zip(names, elems))

    if 'categoria' not in folderdata:
        continue

    if folderdata['jornal'] == "Folha":
            continue

    folderdata['keyword'] = folderdata['keyword'].split('-')[-1]


    cat = folderdata['categoria'].strip()
    if cat not in data:
        data[cat] = 0
    data[cat] += amount

with open('contagem_categorias-Estadao-arq.tsv', 'w') as outfile:
    outfile.write(f'Categoria{sep}Quantidade\n')

    outfile.write('\n'.join([sep.join([cat, str(quant)]) for cat, quant in data.items()]))
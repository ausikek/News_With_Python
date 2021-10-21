import requests
from bs4 import BeautifulSoup

categorias = ['Brasil', 'Colunistas','Esportes','Locais','Gerais','Mundo','Polícial','Política','Regional']

print('Olá, que tipo de notícia você deseja ver? ')

for item in categorias:
    print(f'{categorias.index(item)+1}-{item}')

while True:
    try:
        while True:
            numeracao = int(input('Insira aqui a sua escolha: ' )) 
            if numeracao <= 0:
                    print('Por favor, insira um número de 1 a 9.')
            else:
                break
        categoria = categorias[numeracao-1]
    except ValueError:
        print('Por favor, insira um número de 1 a 9.')
    except IndexError:
        print('Por favor, insira u número de 1 a 9')
    else:
        break


if 'í' in categoria:
    categoria = categoria.replace('í', 'i')
    
res = requests.get(f'https://www.patosonline.com/category/{categoria.lower()}/')
soup = BeautifulSoup(res.text, 'html.parser')

nome = soup.select('h2.post-title')
link = soup.select('.more-link')


def stories_sorted(nL):
    K = nL
    for item in K:
            x = item.get('title')
            y = item.get('link')
            print(f' \nNotícia: {x}. \n\nLink: https://www.patosonline.com{y}\n\n')
    return 'Tenha um ótimo dia!'

def customList(nome, link):
    L = []
    for index, item in enumerate(nome):
        title = nome[index].getText()
        href = link[index].get('href', None)
        L.append({'title' : title, 'link' : href})
    return stories_sorted(L)

customList(nome, link)


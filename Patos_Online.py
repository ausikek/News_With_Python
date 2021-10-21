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
horas = soup.select('span.date')

def stories_sorted(nL):
    K = nL
    for item in K:
            x = item.get('title')
            y = item.get('link')
            z = item.get('hour')
            print(f' \nNotícia: {x} ({z}) \n\nLink: https://www.patosonline.com{y} \n\n')
    return 'Tenha um ótimo dia!'

def customList(nome, link, horas):
    L = []
    for index, item in enumerate(nome):
        title = nome[index].getText()
        hour = horas[index].getText()
        href = link[index].get('href', None)
        L.append({'title' : title, 'link' : href, 'hour' : hour})
    return stories_sorted(L)

customList(nome, link, horas)


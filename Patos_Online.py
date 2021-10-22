import requests as req
from bs4 import BeautifulSoup

categorias = ['Brasil', 'Colunistas', 'Esportes', 'Locais',
              'Gerais', 'Mundo', 'Polícial', 'Política', 'Regional']

print('Olá, que tipo de notícia você deseja ver? ')

for item in categorias:
    print(f'{categorias.index(item)+1}-{item}')


def validate_type(value):
    if isinstance(value, int):
        return True

    if isinstance(value, str):
        return value.isdigit()

    return False


def validate_value_range(input):
    return 0 < int(input) < 10


def validate(value):
    validated = validate_type(value) and validate_value_range(value)

    return validated


def ask_user_input():
    valid_input = False
    value = None

    while not valid_input:
        value = input('Insira aqui a sua escolha: ')
        valid_input = validate(value)

        if not valid_input:
            print('Por favor, insira um número de 1 a 9.')

    return int(value)


categoria = categorias[ask_user_input()-1]

if 'í' in categoria:
    categoria = categoria.replace('í', 'i')

res = req.get(f'https://www.patosonline.com/category/{categoria.lower()}/')
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
            print(f'''
            \nNotícia: {x} ({z})
            \nLink: https://www.patosonline.com{y}
            ''')
    return 'Tenha um ótimo dia!'


def customList(nome, link, horas):
    L = []
    for index, item in enumerate(nome):
        title = nome[index].getText()
        hour = horas[index].getText()
        href = link[index].get('href', None)
        L.append({'title': title, 'link': href, 'hour': hour})
    return stories_sorted(L)

customList(nome, link, horas)

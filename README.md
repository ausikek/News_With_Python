# 📰 News With Python
This program uses Beautiful-Soup 4 to web-scrape a local news site, returning the most recent news (by category) and the link to each article.

## 🤔Motivation 
I created News with Python as a challenge. When I first had contact with Web Scraping, I felt that it was kinda overwhelming and complicated. Working on News With Python taught me a lot about Web Scraping and the Beautiful Soup library.

## ❗ How it works

### bs4 module
We will use bs4 to parse the html data.

### Initial section 

```python
import requests
from bs4 import BeautifulSoup

categorias = ['Brasil', 'Colunistas','Esportes','Locais','Gerais','Mundo','Polícial','Política','Regional']

print('Olá, que tipo de notícia você deseja ver? ')

for item in categorias:
    print(f'{categorias.index(item)+1}-{item}')
```
This block of code is the first thing the user sees when he runs the program. It displays the categories of the news.

### Catching the user's input

```python
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
 ``` 
Those functions will validate the user's input. It has to be a integer between 0 and 10. 

### Using requests and Beautiful Soup

```python
res = requests.get(f'https://www.patosonline.com/category/{categoria.lower()}/')
soup = BeautifulSoup(res.text, 'html.parser')

nome = soup.select('h2.post-title')
link = soup.select('.more-link')
horas = soup.select('span.date')
```
This is where we get the data from the site. Using requests we get the data from the website, and we use Beautiful Soup to parse it. 
Using soup.select() we get the data from the specific html tags and classes we want.

### The customList() function

```python
def customList(nome, link, horas):
    L = []
    for index, item in enumerate(nome):
        title = nome[index].getText()
        hour = horas[index].getText()
        href = link[index].get('href', None)
        L.append({'title' : title, 'link' : href, 'hour' : hour})
    return stories_sorted(L)
```
In this function, the title, link and time of post of the article will be stored as a dictionary and appended to a list. Then, stories_sorted() will be applied on that list.

### The stories_sorted() function

```python
def stories_sorted(nL):
    K = nL
    for item in K:
            x = item.get('title')
            y = item.get('link')
            z = item.get('hour')
            print(f' \nNotícia: {x} ({z}) \n\nLink: https://www.patosonline.com{y} \n\n')
    return 'Tenha um ótimo dia!'
```
In this function, we get the respective items from the dictionary and print them to the user.

## Credits
A lot of the techniques I used were taught in ZTM's course **Complete Python Developer** Web Scraping section. Thanks again for ZTM for contributing with my programmer career.

This project was made purely with the intention of learning. I do not intend to gain any kind of money with News With Python

The news website used:
https://www.patosonline.com

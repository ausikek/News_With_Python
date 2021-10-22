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
```
This block of code is used to catch the user input. See that in the list "categoria" we have the news categories. Those are specific to the website used in the program.

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

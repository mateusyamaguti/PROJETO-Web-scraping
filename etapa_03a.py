import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')
# print(site.prettify())

# # HTML da notícia
noticia = site.find('div', attrs={'class': 'feed-post-body'})
# print (noticia)

# Título
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

print(titulo.text)

# # Subtítulo: div class="bstn-fd-relatedtext"
# subtitulo = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})

# print(subtitulo.text)
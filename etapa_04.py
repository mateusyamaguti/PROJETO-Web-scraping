import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

print("↓↓Buscador de noticias↓↓")
busca = str(input('Pesquisa: '))

response = requests.get(f'https://g1.globo.com/busca/?q={busca}')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# # HTML da notícia
# noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

# for noticia in noticias:
#   # Título
#   titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

#   # print(titulo.text)
#   # print(titulo['href']) # link da notícia

#   # Subtítulo: div class="feed-post-body-resumo"
#   subtitulo = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})

#   if (subtitulo):
#     # print(subtitulo.text)
#     lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
#   else:
#     lista_noticias.append([titulo.text, '', titulo['href']])


# # news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

# # news.to_excel('noticias.xlsx', index=False)

# # print(news)
# for item in lista_noticias:
#   print(item)


noticias = site.findAll('li', attrs={'class': 'widget widget--card widget--info'})

for noticia in noticias:
    titulo = noticia.find('div', attrs = {'class':'widget--info__title'})
    # print(30*'*')
    # print(f'Título na notícia: {titulo.text}')
    
    # descricao = noticia.p()
    # for item in descricao:
    #   print('Descrição da notícia')
    #   print(item.text)

    links = noticia.find_all('a')
    for link in links:
        sublink = link.get('href')
        # print(sublink)

    descricoes = noticia.p()
    for descricao in descricoes:
        if (descricoes):
            lista_noticias.append([titulo.text, sublink, descricao.text])
        else:
            lista_noticias.append([titulo.text, sublink, ""])

print(lista_noticias)

  

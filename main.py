from bs4 import BeautifulSoup as bs
import requests as rq
import re
from qbittorrent import iniciar_download


def extract_version_and_size(html):
    soup = bs(html, 'html.parser')
    versions_and_sizes = {}

    magnet_links = soup.find_all('a', href=re.compile(r'^magnet:'))

    for link in magnet_links:
        version_element = link.find_previous('strong')
        version = version_element.text.strip()

        size_element = version_element.find_next('span', text=re.compile(r'Tamanho:'))
        if size_element:
            size_text = size_element.find_next('span').text.strip()
            size_gb = re.search(r'(\d+\.\d+) GB', size_text)
            if size_gb:
                size_gb = float(size_gb.group(1))
            else:
                size_gb = None
        else:
            size_gb = None

        magnet_link = link['href']
        versions_and_sizes[version] = {'size_gb': size_gb, 'magnet_link': magnet_link}

    return versions_and_sizes

def main():
    lista_h2 = []
    lista_links = []

    userChoice = str(input("Digite o nome do filme ou série: "))

    site_escolhido = "https://bludvfilmes.net/?s="
    url = site_escolhido + userChoice

    htmlCompleto = rq.get(url)
    htmlFormatado = bs(htmlCompleto.content, 'html.parser')
    div_post = htmlFormatado.find("div", class_="posts")

    i = 0
    if div_post:
        divs_title = div_post.find_all("div", class_="post")

        for div_title in divs_title:
            i = i + 1
            print(i, div_title.text.strip().splitlines()[0])
            lista_h2.append(div_title.text.strip().splitlines()[0])
            links = div_title.find_all("a")
            j = 0
            for link in links:
                link_atual = link.get("href")
                if j == 0:
                    # print(link_atual)
                    lista_links.append(link_atual)
                    j = 0

                j = j + 1
    else:
        print("Não foi achado!")

    print("-"*200)
    escolha = int(input("Digite qual o lançamento selecionado: "))
    escolha = escolha - 1
    print("-"*200)

    i = 1
    link_magnet = []
    response = rq.get(lista_links[escolha])
    if response.status_code == 200:
        html = response.content
        versions_and_sizes = extract_version_and_size(html)
        for version, data in versions_and_sizes.items():
            size_gb = data['size_gb']
            magnet_link = data['magnet_link']
            link_magnet.append(data['magnet_link'])
            
            print(f'{i} - Versão: {version}, Magnet Link: {magnet_link}')
            
            i = i + 1

    print("-" * 200)
    userChoice = int(input("Digite qual release você quer? "))
    print("Escolheu = ", link_magnet[userChoice - 1])
    categoriaChoice = int(input("1 - é um filme?\n2 - é uma série?\n"))
    categoria_para_parametro = {
        1: 'radarr',
        2: 'sonarr'
    }

    if categoriaChoice in categoria_para_parametro:
        categoria_parametro = categoria_para_parametro[categoriaChoice]
        iniciar_download(link_magnet[userChoice - 1], categoria_parametro)
    else:
        print("Escolha de categoria inválida.")


if __name__ == "__main__":
    main()

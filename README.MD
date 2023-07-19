# Projeto de Web Scraping - Buscador de Filmes Brasileiros Dublados

Este é um projeto de web scraping desenvolvido para resolver o problema comum de downloads automatizados de filmes por meio de sites públicos de torrents que raramente oferecem opções de releases dublados. O objetivo deste projeto é fornecer uma solução que possa ser usada inteiramente no terminal e integrar-se facilmente com servidores automatizados que utilizam ferramentas como Radarr e Sonarr.

## Problema

Ao automatizar o processo de download de filmes por meio de sites públicos de torrents, é comum encontrar dificuldades em obter releases dublados de filmes brasileiros. Isso pode ser frustrante para aqueles que preferem assistir aos filmes em seu idioma nativo ou para quem tem restrições de idioma.

## Solução

O buscador de filmes brasileiros dublados utiliza técnicas de web scraping para pesquisar em um site específico de download de filmes, buscando opções de releases dublados e não dublados. A ferramenta foi projetada para funcionar no terminal, oferecendo facilidade de uso e integração com sistemas automatizados como Radarr e Sonarr.

## Como Usar

⚠️ **É necessário realizar algumas configurações antes de executar o script:** ⚠️

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório em sua máquina local.
3. Baixe as dependências listadas no arquivo `requirements.txt` utilizando o seguinte comando no terminal: `pip install -r requirements.txt`.
4. Abra o arquivo `qbittorrent.py` em um editor de texto e modifique as credenciais do web UI do usuário para que o script possa interagir com o qBittorrent. Insira o nome de usuário e senha corretos conforme configurado em seu qBittorrent.
5. Certifique-se de que o qBittorrent esteja configurado com o Web UI habilitado e acessível através das credenciais que você configurou no arquivo `qbittorrent.py`.

Agora você está pronto para executar o script do buscador de filmes brasileiros dublados:

6. No terminal, navegue até o diretório do projeto.
7. Execute o script principal do buscador de filmes usando o comando: `python main.py`.
8. Siga as instruções apresentadas na interface de linha de comando para pesquisar e encontrar filmes brasileiros dublados ou não.

## Disclaimer sobre Pirataria

É importante ressaltar que este projeto é estritamente para fins educacionais e de aprendizado em relação à tecnologia de web scraping e automação. O uso deste projeto para baixar conteúdo protegido por direitos autorais, como filmes e séries, sem a devida autorização dos detentores dos direitos, é ilegal e não é encorajado. A pirataria de filmes e séries no Brasil é uma violação dos direitos autorais e pode resultar em ações legais.

Se você optar por usar este projeto ou qualquer outra ferramenta para baixar filmes ou séries, certifique-se de cumprir as leis de direitos autorais do seu país e de respeitar os direitos dos criadores e produtores de conteúdo.

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma "issue" ou enviar uma "pull request". Qualquer contribuição que esteja em conformidade com os princípios de respeito aos direitos autorais e à legalidade será bem-vinda.

## Aviso Legal

Este projeto é fornecido "no estado em que se encontra" e não oferece garantias ou suporte. Os desenvolvedores deste projeto não são responsáveis pelo uso indevido, ilegal ou não autorizado do software por terceiros.

**Lembre-se: Respeite os direitos autorais e apoie os criadores de conteúdo comprando filmes e séries legalmente.**

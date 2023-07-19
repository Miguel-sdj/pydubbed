def iniciar_download(magnet_link, categoria):
    import qbittorrentapi

    conn_info = dict(
        host="CHANGE-ME",
        port=8080, #MAYBE CHANGE-ME
        username="CHANGE-ME",
        password="CHANGE-ME",
    )
    qbt_client = qbittorrentapi.Client(**conn_info)

    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)

    # Definindo a categoria para "radarr"
    category = categoria

    # Criando uma tarefa de download para o magnet link com a categoria definida
    try:
        qbt_client.torrents_add(urls=magnet_link, category=category)
        print("Download iniciado com sucesso!")
    except Exception as e:
        print(f"Falha ao iniciar o download: {e}")

# iniciar_download("magnet:?xt=urn:btih:5ON2MZB7HG2Q7WW7RKMLMVQIM4OHDNW5&dn=Carros.1.2006.OPEN.MATTE.IMAX.1080p.WEB-DL.H264.AC3.5.1.DUAL-RICKSZ-BLUDV", "radarr")


import qrcode
import os
from qrcode.image.styledpil import StyledPilImage

def verificaLinkW(link):
    """
    Verifica e modifica um link, caso esteja no formato Wi-Fi, para um formato de informação de rede Wi-Fi.

    Esta função verifica se a string 'link' está no formato correto para representar informações de uma rede Wi-Fi.
    O formato esperado é "wifi:ssid,senha", onde 'ssid' é o nome da rede e 'senha' é a senha da rede.
    Se 'link' estiver no formato correto, a função cria uma string de informações de rede Wi-Fi no formato:
    "WIFI:T:<segurança>;S:<ssid>;P:<senha>;;", onde 'segurança' pode ser "WEP", "WPA" ou "nopass", 'ssid' é
    o nome da rede e 'senha' é a senha da rede. Se 'link' não estiver no formato correto, ele permanece inalterado.

    Args:
        link (str): O link ou informações da rede Wi-Fi a serem verificados e, se necessário, modificados.

    Returns:
        str: O link original se 'link' não estiver no formato correto de rede Wi-Fi.
             Caso contrário, uma string de informações de rede Wi-Fi no formato especificado.
    Parameters:
        link (str): O link ou informações da rede Wi-Fi a serem verificados e, se necessário, modificados.

    Example:
        >>> verificaLinkW("wifi:MinhaRede,MinhaSenha")
        'WIFI:T:WPA;S:MinhaRede;P:MinhaSenha;;'
        >>> verificaLinkW("https://example.com")
        'https://example.com'
    """
    if "wifi:" in link:
        partes = link.split(",")
        
        if len(partes) >= 2:
            ssid = partes[0]
            senha = partes[1]
            seguranca = "WPA"
            wifi_info = f"WIFI:T:{seguranca};S:{ssid};P:{senha};;"
            link = wifi_info

    return link

def verificaLinkC(link):
    """
    Verifica e modifica um link, caso seja formado apenas por números, para um link de mensagem do WhatsApp.

    Esta função verifica se a variável 'link' consiste apenas em dígitos numéricos (0 a 9).
    Se 'link' for uma sequência de dígitos, ela é transformada em um link de mensagem do WhatsApp,
    acrescentando 'https://wa.me/55' no início do número.

    Args:
        link (str): O link ou número a ser verificado e, se necessário, modificado.

    Returns:
        str: O link original se 'link' não consistir apenas em dígitos.
             Caso contrário, um link de mensagem do WhatsApp formatado como 'https://wa.me/55XXXXXXXXXX',
             onde 'XXXXXXXXXX' é o número original.

    Parameters:
        link (str): O link ou número a ser verificado e, se necessário, modificado.

    Example:
        >>> verificaLink("16999999999")
        'https://wa.me/551616999999999'
        >>> verificaLink("https://exemplo.com")
        'https://exemplo.com'
    """
    if link.isdigit():
        link = "https://wa.me/55" + link
    return link

def setLogo(link):
    """
    Retorna o caminho para o logotipo associado a um link da web, se disponível.

    Esta função verifica o link fornecido em relação a um dicionário de links conhecidos
    e seus logotipos correspondentes. Se o link corresponder a um dos links conhecidos,
    o caminho para o logotipo associado é retornado. Caso contrário, o caminho padrão
    para um logotipo (no caso, "logos/python_logo.png") é retornado.

    Args:
        link (str): O link da web a ser verificado em relação ao dicionário de links.

    Returns:
        str: O caminho para o logotipo associado ao link, ou o caminho padrão se o
             link não corresponder a nenhum dos links conhecidos.

    Parameters:
        link (str): O link da web que será verificado.
    """
    logos = {
        'tiktok.com':"logos/tiktok_logo.png",'instagram.com':"logos/instagram_logo.png",'whatsapp.com':"logos/whatsapp_logo.png",'wa.me':"logos/whatsapp_logo.png",
        'youtube.com':"logos/youtube_logo.png",'python':"logos/python_logo.png",'spotify.com':"logos/spotify_logo.png",'messenger.com':"logos/messenger_logo",
        'WIFI:T':"logos/wifi_logo.png",'youtu.be':"logos/youtube_logo.png",'facebook.com':"logos/facebook_logo.png",'fb.watch':"logos/facebook_logo.png",
        'linkedin.com':"logos/linkedin_logo.png",'google.com':"logos/google_logo.png"
         }
    k=False
    logoP = "logos/python_logo.png"
    for site in logos:
        if k == True:
            pass
        if site in link and k == False:
            k = True
            logoP = logos[site]

    return logoP

print("\n-*-*-*-*-*-*-*-*-*-*-*-FORMATOS-*-*-*-*-*-*-*-*-*-*-\n")
print("Link....: 'https://www.exemplo.com.br/paginaInicial'\n")
print("Wifi....: 'wifi:Nome,Senha'\n")
print("Whatsapp: '1691234567'\n")

link = input("Digite a informação: ")
link = verificaLinkC(link)
link = verificaLinkW(link)
logo = setLogo(link)

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size = 15)
qr.add_data(link)

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path=logo,
)

imagem.save("qrcode_logo.png")

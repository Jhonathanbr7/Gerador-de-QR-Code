import qrcode
import os
from qrcode.image.styledpil import StyledPilImage
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Backend

try:

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

    import os

    def setLogo(link):
        """
        Retorna o caminho para o logotipo associado a um link da web, se disponível.

        Esta função verifica o link fornecido em relação a um dicionário de links conhecidos
        e seus logotipos correspondentes. Se o link corresponder a um dos links conhecidos,
        o caminho para o logotipo associado é retornado. Caso contrário, o caminho padrão
        para um logotipo (no caso, "python_logo.png") é retornado.

        Args:
            link (str): O link da web a ser verificado em relação ao dicionário de links.

        Returns:
            str: O caminho para o logotipo associado ao link, ou o caminho padrão se o
                link não corresponder a nenhum dos links conhecidos.

        Parameters:
            link (str): O link da web que será verificado.
        """
        pastaAtual = os.path.dirname(os.path.abspath(__file__))
        pastaLogos = os.path.join(pastaAtual, "logos")

        pastaLogoPadrao = os.path.join(pastaLogos, "python_logo.png")
        logoP = pastaLogoPadrao

        logos = {
            'tiktok.com': 'tiktok_logo.png',
            'instagram.com': 'instagram_logo.png',
            'whatsapp.com': 'whatsapp_logo.png',
            'wa.me': 'whatsapp_logo.png',
            'youtube.com': 'youtube_logo.png',
            'python': 'python_logo.png',
            'spotify.com': 'spotify_logo.png',
            'messenger.com': 'messenger_logo.png',
            'WIFI:T': 'wifi_logo.png',
            'youtu.be': 'youtube_logo.png',
            'facebook.com': 'facebook_logo.png',
            'fb.watch': 'facebook_logo.png',
            'linkedin.com': 'linkedin_logo.png',
            'google.com': 'google_logo.png'
        }

        for site, logo in logos.items():
            if site in link:
                logoP = os.path.join(pastaLogos, logo)
                break
        print(logoP)

        return logoP

    
    def atualiza_imagem(nomeArquivo):
        """
        Atualiza um rótulo de imagem com a imagem carregada a partir de um arquivo.

        Args:
            nomeArquivo (str): O nome do arquivo da imagem a ser carregada e exibida.

        Retorna:
            None
        """
        img = Image.open(nomeArquivo)
        photo = ImageTk.PhotoImage(img)
        img_label.config(image=photo)
        img_label.image = photo 


    def criaLink():
        """
        Cria um código QR com um link a partir dos dados inseridos em um campo de entrada.

        Esta função executa as seguintes etapas:
        1. Obtém um link a partir de um campo de entrada (widget Entry).
        2. Limpa o campo de entrada.
        3. Verifica e ajusta o formato do link.
        4. Define uma imagem de logotipo para o código QR.
        5. Cria um objeto QR Code com o link.
        6. Gera uma imagem do código QR com um logotipo embutido.
        7. Salva a imagem como 'qrcode_logo.png'.
        8. Atualiza um rótulo de imagem com a nova imagem gerada.

        Args:
            None

        Retorna:
            None
        """
        gerar.config(state='normal')
        link = dado.get()
        dado.delete(0, 'end')
        link = verificaLinkC(link)
        link = verificaLinkW(link)
        logo = setLogo(link)

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size = 10)
        qr.add_data(link)

        imagem = qr.make_image(
            image_factory=StyledPilImage,
            embeded_image_path=logo,
        )
        
        imagem.save("qrcode_logo.png")
        
        atualiza_imagem("qrcode_logo.png")


except Exception as e:
    print(e)


#Front-end
try:
    fonte_personalizadaT = ("Arial", 30)
    fonte_personalizada = ("Arial", 16)
    fonte_personalizadaI = ("Arial", 50)

    janela = tk.Tk()
    janela.configure(bg="white")
    janela.state('zoomed')
    janela.title("Gerador de QR Code")


    frame = tk.Frame(janela)
    frame.configure(bg="White",height=30)
    frame.pack(fill="both")

    titulo = tk.Label(frame,text="---------------------------------------------------------------------Gerador de QR Code---------------------------------------------------------------------",
                    fg='Black', bg='white',font=fonte_personalizadaT)
    titulo.pack(pady=10,expand=True)

    table = tk.Frame(janela)
    table.configure(bg="white")
    table.pack(fill='both',pady=10,expand=True)

    linha = tk.Label(table,text="", fg='Black', bg='white',font=fonte_personalizada,width = 155)
    linha.grid(row=0, column=0,columnspan=7,sticky="NWE")



    formatos = tk.Label(table,text="FORMATOS ABAIXO", fg='Black', bg='white',font=fonte_personalizada,width = 60)
    formatos.grid(row=1, column=0,sticky="WE")


    lk = tk.Label(table,text="Link....: 'https://www.exemplo.com.br/paginaInicial'", fg='Black', bg='white',font=fonte_personalizada)
    lk.grid(row=2, column=0,sticky="W")

    img_label = tk.Label(table,width=18, height= 8, bg="white")
    img_label.grid(row=1, column=2, columnspan=15,rowspan=15, sticky="NSWE")

    wifi = tk.Label(table,text="Wifi....: 'wifi:Nome,Senha'", fg='Black', bg='white',font=fonte_personalizada)
    wifi.grid(row=3, column=0,sticky="W")

    whatsapp = tk.Label(table,text="Whatsapp: '1691234567'", fg='Black', bg='white',font=fonte_personalizada)
    whatsapp.grid(row=4, column=0,sticky="W")

    separator = ttk.Separator(table, orient="horizontal",)
    separator.grid(row=5, column=0, columnspan=1, sticky="EW")

    info = tk.Label(table,text="Digite a Informação abaixo:", fg='Black', bg='white',font=fonte_personalizada)
    info.grid(row=6, column=0,sticky="WE")

    dado = tk.Entry(table)
    dado.config(font = fonte_personalizada)
    dado.grid(row=7,column=0,sticky="NSWE")

    separator = ttk.Separator(table, orient="horizontal",)
    separator.grid(row=8, column=0, columnspan=1, sticky="EW")

    coluna = tk.Label(table,text="", fg='Black', bg='Black',font=fonte_personalizada,height=35, width=1)
    coluna.grid(row=1, column=30,rowspan=15,sticky="NSEW")
            
    gerar = tk.Button(table,text="Gerar QR Code", command=criaLink,font=fonte_personalizada, fg='Black', bg='white')
    gerar.grid(row=9, column=0, sticky="NSEW")



    separator = ttk.Separator(table, orient="horizontal",)
    separator.grid(row=10, column=0, columnspan=1, sticky="EW")

    janela.configure(bg="white")
    janela.mainloop()

except Exception as e:
    print(e)
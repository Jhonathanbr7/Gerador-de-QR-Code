import qrcode
import os
import customtkinter as ctk
from customtkinter import filedialog
from qrcode.image.styledpil import StyledPilImage
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
        QRCodeImg_Lbl.configure(image=photo)
        QRCodeImg_Lbl.image = photo 

        
    logo = ""

    def escolherLogo():
        """
        Abre uma janela de seleção de arquivo para escolher um logotipo em formato PNG ou JPG.

        Esta função permite ao usuário selecionar um arquivo de imagem no formato PNG ou JPG
        que será utilizado como logotipo no código QR gerado.

        Args:
            None

        Retorna:
            None
        """
        global logo
        logo = filedialog.askopenfilename(initialdir="/Desktop",title="Selecione o arquivo", filetypes=(("Arquivos PNG","*.png"),("Arquivos JPG","*.JPG")))


    def resetLogo():
        """
        Esta função tira o valor da variável global "logo".

        Args:
            None

        Retorna:
            None
        """
        global logo
        logo = ""

    def criaLink():
        """
        Cria um código QR com um link a partir dos dados inseridos em um campo de entrada.

        Esta função executa as seguintes etapas:
        1. Obtém um link a partir de um campo de entrada (widget Entry).
        2. Limpa o campo de entrada.
        3. Verifica e ajusta o formato do link.
        4. Define uma imagem de logotipo para o código QR utilizando a função 'escolherLogo'.
        5. Cria um objeto QR Code com o link.
        6. Gera uma imagem do código QR com um logotipo embutido.
        7. Salva a imagem como 'qrcode_logo.png'.
        8. Atualiza um rótulo de imagem com a nova imagem gerada.

        A função 'escolherLogo' é utilizada para selecionar o logotipo a ser incorporado no código QR.

        Args:
            None

        Retorna:
            None
        """

        global Logo
        link = dado.get()
        tamanho = dadoT.get()
        if not tamanho:
            tamanho = 10
        else:
            tamanho = int(tamanho)

        dado.delete(0, 'end')
        link = verificaLinkC(link)
        link = verificaLinkW(link)


        if logo == "":
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=int(tamanho))
            qr.add_data(link)
            imagem = qr.make_image()
        else:
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(link)
            imagem = qr.make_image(
                image_factory=StyledPilImage,
                embeded_image_path=logo,
            )

        imagem.save("qrcode.png")
        atualiza_imagem("qrcode.png")
    

    def salvarQRCode():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            try:
                os.replace("qrcode.png", file_path)
            except Exception as e:
                print("Erro ao salvar o arquivo:", e)

    



except Exception as e:
    print(e)


#Front-end

try:
    ctk.set_appearance_mode("dark")

    janela = ctk.CTk()

    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    janela.geometry(f"{largura}x{altura}")

    ctk.set_appearance_mode("dark")

    janela.minsize(largura, altura)
    janela.maxsize(largura, altura)
    janela.title("Gerador de QR Code")

    fonte_personalizadaT = ("Arial", int(0.035 * altura))
    fonte_personalizada = ("Arial", int(0.020 * altura),'bold')
    fonte_personalizadaD = ("Arial", int(0.020 * altura), "black")
    fonte_personalizadaI = ("Arial", int(0.080 * altura))

    #TOPO--------------------------------------------------------------------------------------------------------------------------------------------
    frameTopo = ctk.CTkFrame(janela,fg_color="#0074D9",width=largura-(largura*0.02), height=(altura-(altura*0.95)if altura >= 1080 else altura-(altura*0.96)))
    frameTopo.place(relx = 0.01, rely= 0.01)

    frameTopo.pack_propagate(False)

    titulo = ctk.CTkLabel(frameTopo, text="Gerador de QR Code", font=fonte_personalizadaT, anchor="center",text_color="black")
    titulo.pack(pady=1, expand=True)

    #Esquerda----------------------------------------------------------------------------------------------------------------------------------------
    frameEsquerda = ctk.CTkFrame(janela, width=largura-(largura*0.52), height=(altura-(altura*0.15)if altura == 1080 else altura-(altura*0.16)))
    frameEsquerda.place(relx = 0.01, rely= (0.08 if altura >= 1080 else 0.06))

    frameEsquerda.pack_propagate(False)

    formatos_frame = ctk.CTkFrame(frameEsquerda,fg_color="#333333")
    formatos_frame.pack(padx = 10 ,pady = 10, fill="both")

    formatosT_Lbl = ctk.CTkLabel(formatos_frame, font=fonte_personalizada, text="FORMATOS:",anchor="center")
    formatosT_Lbl.pack(pady=10, expand=True)

    formatos_Lbl = ctk.CTkLabel(formatos_frame, font=fonte_personalizada,
                                text="Link...........: 'https://www.exemplo.com.br/paginaInicial'\n\nWifi............: 'wifi:Nome,Senha'\n\nWhatsapp: '1691234567'")
    formatos_Lbl.pack(pady=10,side="left", expand=True)
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    informacoes_frame = ctk.CTkFrame(frameEsquerda,fg_color="#333333")
    informacoes_frame.pack(padx = 10 ,pady = (10 if altura >= 1080 else 5), fill="both")

    info_Lbl = ctk.CTkLabel(informacoes_frame, font=fonte_personalizada, text="Digite a Informação abaixo:",anchor="center")
    info_Lbl.pack(pady = (10 if altura >= 1080 else 5),expand=True)

    dado = ctk.CTkEntry(informacoes_frame,font=fonte_personalizada,fg_color="#0074D9",height=(altura-(altura*0.95)if altura >= 1080 else altura-(altura*0.96)), justify="center",text_color="black",placeholder_text="Link, Wifi ou WhatsApp",placeholder_text_color="black",border_color="#333333")
    dado.pack(padx=10, pady = (10 if altura >= 1080 else 5), expand=True, fill="x")

    infoT_Lbl = ctk.CTkLabel(informacoes_frame, font=fonte_personalizada,text="Digite o tamanho do QR Code abaixo de 0 a 25 (Opcional):",anchor="center")
    infoT_Lbl.pack(pady = (10 if altura >= 1080 else 5),expand=True)

    dadoT = ctk.CTkEntry(informacoes_frame,font=fonte_personalizada,text_color="black",fg_color="#0074D9", justify="center",placeholder_text="10",placeholder_text_color="black", width=50,bg_color="#333333",border_color="#333333")
    dadoT.pack(padx=10, pady = (10 if altura >= 1080 else 5), expand=True)

    gerarQRCode_Btn = ctk.CTkButton(informacoes_frame,text="Clique aqui para gerar o QR Code",height=(altura-(altura*0.95)if altura >= 1080 else altura-(altura*0.96)), command=criaLink,font=fonte_personalizada,fg_color="#0074D9",text_color="black",hover_color="#00FFFF")
    gerarQRCode_Btn.pack(padx=10, pady = (10 if altura >= 1080 else 5), expand=True, fill="x")

    salvarQRCode_Btn = ctk.CTkButton(informacoes_frame, text="Salvar QR Code", command=salvarQRCode, height=(altura-(altura*0.95)if altura >= 1080 else altura-(altura*0.96)), font=fonte_personalizada, fg_color="#0074D9", text_color="black", hover_color="#00FFFF")
    salvarQRCode_Btn.pack(padx=10, pady=(10 if altura >= 1080 else 5), expand=True, fill="x")

    #-------------------------------------------------------------------------------------------------------------------------------------------------

    logo_frame=ctk.CTkFrame(frameEsquerda,fg_color="#333333")
    logo_frame.pack(padx = 10 ,pady = 10, expand=True,fill="both")

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    logo_Lbl = ctk.CTkLabel(logo_frame, font=fonte_personalizada,text="Configurações de Logo: ",anchor="center")
    logo_Lbl.pack(pady = (10 if altura >= 1080 else 5),expand=True)


    escolherLogo_Btn = ctk.CTkButton(logo_frame,text="Clique aqui para selecionar a sua logo" , command=escolherLogo,height=(altura-(altura*0.93)if altura >= 1080 else altura-(altura*0.96)),font=fonte_personalizada,fg_color="#0074D9",text_color="black",hover_color="#00FFFF")
    escolherLogo_Btn.pack(padx=10, pady=(10 if altura >= 1080 else 5), expand=True, fill="x")
    
    resetLogo_Btn = ctk.CTkButton(logo_frame, text="Apagar logo selecionda", command=resetLogo, height=(altura-(altura*0.93)if altura >= 1080 else altura-(altura*0.96)), font=fonte_personalizada, fg_color="#0074D9", text_color="black", hover_color="#00FFFF")
    resetLogo_Btn.pack(padx=10, pady=(10 if altura >= 1080 else 5), expand=True, fill="x")

    
    #Direita-----------------------------------------------------------------------------------------------------------------------------------------
    frameDireita = ctk.CTkFrame(janela, width=largura-(largura*0.52), height=(altura-(altura*0.15)if altura == 1080 else altura-(altura*0.16)))
    frameDireita.place(relx = 0.51, rely= (0.08 if altura >= 1080 else 0.06))

    frameDireita.pack_propagate(False)

    QRCodeLbl_frame = ctk.CTkFrame(frameDireita,fg_color="#333333")
    QRCodeLbl_frame.pack(padx = 10 ,pady = 10, fill="both")
                                

    QRCode_Lbl = ctk.CTkLabel(QRCodeLbl_frame, font=fonte_personalizada, text="QR CODE",anchor="center")
    QRCode_Lbl.pack(pady=10, expand=True)

    QRCodeImg_frame = ctk.CTkFrame(frameDireita,fg_color="#333333")
    QRCodeImg_frame.pack(padx = 10 ,pady = 10, fill="both",expand=True)
    QRCodeImg_frame.pack_propagate(False)

    QRCodeImg_Lbl = ctk.CTkLabel(QRCodeImg_frame,text="")
    QRCodeImg_Lbl.pack(padx = 10 ,pady = 10, fill="both",expand=True)

    #FIM---------------------------------------------------------------------------------------------------------------------------------------------
    janela.state('zoomed')
    janela.mainloop()

except Exception as e:
    print(e)
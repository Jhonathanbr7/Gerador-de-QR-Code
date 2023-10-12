import customtkinter as ctk
import os
from PIL import Image, ImageTk



def criaLink():
    print("Deu certo")




janela = ctk.CTk()

largura = janela.winfo_screenwidth()
altura = janela.winfo_screenheight()
janela.geometry(f"{largura}x{altura}")

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

dado = ctk.CTkEntry(informacoes_frame,font=fonte_personalizada,fg_color="#0074D9", justify="center",text_color="black",placeholder_text="Link, Wifi ou WhatsApp",placeholder_text_color="black",border_color="#333333")
dado.pack(padx=10, pady = (10 if altura >= 1080 else 5), expand=True, fill="x")

infoT_Lbl = ctk.CTkLabel(informacoes_frame, font=fonte_personalizada,text="Digite o tamanho do QR Code abaixo de 0 a 25 (Opcional):",anchor="center")
infoT_Lbl.pack(pady = (10 if altura >= 1080 else 5),expand=True)

dadoT = ctk.CTkEntry(informacoes_frame,font=fonte_personalizada,text_color="black",fg_color="#0074D9", justify="center",placeholder_text="10",placeholder_text_color="black", width=50,bg_color="#333333",border_color="#333333")
dadoT.pack(padx=10, pady = (10 if altura >= 1080 else 5), expand=True)

gerarQRCode_Btn = ctk.CTkButton(informacoes_frame,text="Clique aqui para gerar o QR Code",height=(altura-(altura*0.95)if altura >= 1080 else altura-(altura*0.96)), command=criaLink,font=fonte_personalizada,fg_color="#0074D9",text_color="black",hover_color="#00FFFF")
gerarQRCode_Btn.pack(padx=10, pady = (10 if altura >= 1080 else 5), expand=True, fill="x")

#-------------------------------------------------------------------------------------------------------------------------------------------------

imagemS_frame=ctk.CTkFrame(frameEsquerda,fg_color="#333333")
imagemS_frame.pack(padx = 10 ,pady = 10, fill="both")

diretorio_atual = os.path.dirname(os.path.abspath(__file__))


x = 'exemplos19201080.png' if altura >= 1080 else 'exemplos1280720.png'

caminho_imagemStatica = os.path.join(diretorio_atual, 'logos',x)

imagem = Image.open(caminho_imagemStatica)
imagem = ImageTk.PhotoImage(imagem)

imagemS = ctk.CTkLabel(imagemS_frame,text="", image=imagem)
imagemS.pack(padx=10, pady=10, expand=True)

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


#FIM---------------------------------------------------------------------------------------------------------------------------------------------
janela.state('zoomed')
janela.mainloop()
# Gerador de QR Code

O código é uma aplicação para gerar códigos QR com logotipos incorporados. Ele inclui tanto a parte do backend quanto o frontend.

**Backend:**

1. A parte do backend começa com a definição de três funções principais: `verificaLinkW`, `verificaLinkC`, e `setLogo`. Essas funções são usadas para verificar e formatar links de entrada, tornando-os adequados para a geração de códigos QR.

2. A função `verificaLinkW` verifica se um link está no formato Wi-Fi (por exemplo, "wifi:NomeRede,Senha") e o converte em um formato específico para redes Wi-Fi.

3. A função `verificaLinkC` verifica se um link é um número de telefone (composto apenas por dígitos) e o converte em um link do WhatsApp.

4. A função `setLogo` define o logotipo associado a um link da web, se disponível, usando um dicionário de links conhecidos e seus logotipos correspondentes.

5. Há uma função chamada `atualiza_imagem` que atualiza um rótulo de imagem com a imagem carregada a partir de um arquivo.

6. A função `criaLink` é o coração da geração de QR Codes. Ela obtém um link de entrada, verifica seu formato, define um logotipo e gera um código QR com base nessas informações. A imagem resultante é salva como "qrcode_logo.png" e um rótulo de imagem é atualizado para exibi-la.

**Front-end:**

1. A parte do frontend usa a biblioteca `customtkinter` para criar uma interface gráfica para a aplicação.

2. Ela define a janela da GUI, cria elementos como rótulos, campos de entrada e botões, e organiza-os em diferentes frames.

3. A interface gráfica inclui uma área onde os usuários podem inserir um link e, opcionalmente, o tamanho do QR Code.

4. Um botão "Clique aqui para gerar o QR Code" chama a função `criaLink` para criar o código QR.

5. A imagem do QR Code gerado é exibida na parte direita da interface.

6. Há também informações sobre formatos de links aceitos e exemplos de uso exibidos na parte esquerda da interface.


import cv2
import numpy as np



# Pasta onde estão as imagens para serem comparadas
pastaImagens = '/Users/fabiopegadosilveira/Documents/GitHub/TFC-DEISI6-RiverWatcher/Imagens'
pastaImagensOutput = '/Users/fabiopegadosilveira/Documents/GitHub/TFC-DEISI6-RiverWatcher/Imagens/Output/'
# Carrega as duas imagens que deseja comparar
# Editar o nome para as imagens a comparar
img1 = cv2.imread(pastaImagens + 'rio1.jpeg')
img2 = cv2.imread(pastaImagens + 'rio2.jpeg')

# Lista as Imagens presentes na pasta
'''for imagem in os.listdir(pastaImagens):
    imagemAtual = os.path.join(pastaImagens, imagem)
    print(imagemAtual)'''



def mostra_diferencas(imagem1, imagem2):
    # Calcula a diferença absoluta entre as duas imagens
    diferencaAbsoluta = cv2.absdiff(imagem1, imagem2)
    cv2.imshow("diferenca absoluta", diferencaAbsoluta)
    cv2.waitKey(0)
    # Converte a diferença absoluta em grayscale
    diferencaAbsolutaGray = cv2.cvtColor(diferencaAbsoluta, cv2.COLOR_BGR2GRAY)
    
    # Faz um highlight as diferenças 
    _, diff_thresholded = cv2.threshold(diferencaAbsolutaGray, 30, 255, cv2.THRESH_BINARY)
    
    # Procura os contornos das diferenças 
    contours, _ = cv2.findContours(diff_thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Imagem preta para depois ser usada como base 
    imagemFundoPreto = np.zeros_like(imagem1)
    # Desenha os contornos preenchidos na imagem preta
    cv2.drawContours(imagemFundoPreto, contours, -1, (0, 0, 255), thickness=cv2.FILLED)
    cv2.imshow("imagemFundoPreto", imagemFundoPreto)
    cv2.waitKey(0)


    # Bitwise AND para mostrar a combinação entre as duas imagens, mostra a diferença em "marca de agua"
    diferencaFundoPreto = cv2.bitwise_and(imagem1, imagem2)
    cv2.imshow("diferencaFundoPreto", diferencaFundoPreto)
    cv2.drawContours(diferencaFundoPreto, contours, -1, (0, 0, 255), 2)
    cv2.imwrite(pastaImagensOutput + "diferenca_3.4.jpg", diferencaFundoPreto)


    # Desenha os contornos das diferenças
    # Usa a imagem original para desenhar os contornos das diferenças
    diferencaImagem1 = imagem1.copy()
    diferencaImagem2 = imagem2.copy()
    contornoInternoFilled = imagem1.copy()
    contornoInternoNotFilled = imagem1.copy()
    cv2.drawContours(diferencaImagem1, contours, -1, (0, 0, 255), 2)
    cv2.drawContours(diferencaImagem2, contours, -1, (0, 0, 255), 2)
    cv2.drawContours(contornoInternoFilled, contours, -1, (0, 0, 255), thickness=cv2.FILLED)
    cv2.drawContours(contornoInternoNotFilled, contours, -1, (0, 0, 255), 2)
    
    
    # Mostra as imagens
    cv2.imshow("Imagem 1", imagem1)
    cv2.imshow("Imagem 2", imagem2)
    cv2.imshow("Diferenca Imagem 1", diferencaImagem1)
    cv2.imshow("Diferenca Imagem 2", diferencaImagem2)
    cv2.imshow("contorno interno filled", contornoInternoFilled)
    cv2.imshow("contorno interno not filled", contornoInternoNotFilled)
    cv2.imwrite(pastaImagensOutput + "diferenca_3.1.jpg", diferencaImagem1)
    cv2.imwrite(pastaImagensOutput + "diferenca_3.2.jpg", diferencaImagem2)
    cv2.imwrite(pastaImagensOutput + "diferenca_3.3.jpg", contornoInternoFilled)
    cv2.waitKey(0)


# Executa a função
mostra_diferencas(img1, img2)

# Fecha as janelas abertas durante a execução (imagens e as suas diferenças)
cv2.destroyAllWindows()
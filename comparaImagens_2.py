import cv2
import numpy as np
import os



pastaImagens = '/Users/fabiopegadosilveira/Documents/GitHub/TFC-DEISI6-RiverWatcher/Imagens'
pastaImagensOutput = '//Users/fabiopegadosilveira/Documents/GitHub/TFC-DEISI6-RiverWatcher/Imagens/Output/'


for imagem in os.listdir(pastaImagens):
    imagemAtual = os.path.join(pastaImagens, imagem)
    print(imagemAtual)


# Carrega as duas imagens que deseja comparar
img1 = cv2.imread(pastaImagens + 'rio1.jpeg')
img2 = cv2.imread(pastaImagens + 'rio2.jpeg')


# Compara as imagens
diferencaImagens = cv2.subtract(img1, img2)
#print(diferencaImagens)
cv2.imshow("diferencaImagens",diferencaImagens)
cv2.waitKey(0)
# Verifica se há diferenças entre as imagens
resultadoProvisorio = cv2.cvtColor(diferencaImagens, cv2.COLOR_BGR2GRAY)
print(resultadoProvisorio)
resultadoFinal = cv2.countNonZero(resultadoProvisorio)


if resultadoFinal == 0:
    print("As imagens são iguais.")
else:
    #cv2.imwrite("diferenca.jpg", diferencaImagens)
    cv2.imshow("diferencaImagens1", diferencaImagens)
    #cv2.imwrite(pastaImagensOutput + "diferenca_2.jpg", diferencaImagens)
    cv2.waitKey(0)
    print("As imagens são diferentes. Verifique o arquivo diferenca.jpg para ver as diferenças.")


cv2.destroyAllWindows()
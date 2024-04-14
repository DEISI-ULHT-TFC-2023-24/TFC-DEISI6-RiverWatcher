import cv2
import numpy as np
import os

pastaImagens = '/Users/fabiopegadosilveira/Documents/GitHub/TFC-DEISI6-RiverWatcher/Imagens'
pastaImagensOutput = '/Users/fabiopegadosilveira/Documents/GitHub/TFC-DEISI6-RiverWatcher/Imagens/Output/'

for imagem in os.listdir(pastaImagens):
    imagemAtual = os.path.join(pastaImagens, imagem)
    print(imagemAtual)


# Carrega as duas imagens que deseja comparar
img1 = cv2.imread(pastaImagens + 'rio1.jpeg')
img2 = cv2.imread(pastaImagens + 'rio2.jpeg')


# Converte as imagens em grayscale
# necessário para a função do MSE(Mean Square Error) funcionar
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


# função para calcular a MSE(Mean Square Error) entre as 2 imagens
def meanSquareError(img1, img2):
   alturaImagem, larguraImagem = img1.shape # devolve a altura e largura da imagem, põe os dados nas variáveis
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(alturaImagem*larguraImagem))
   return mse, diff



mse, diff = meanSquareError(img1, img2)
if mse > 25:
    cv2.imshow("diferencaImagens", diff)
    cv2.waitKey(0)

print("Imagens diferentes, valor diferença:",mse)

cv2.imshow("diferencaImagens", diff)
cv2.imwrite(pastaImagensOutput + "diferenca_1.jpg", diff)
cv2.waitKey(0)

cv2.destroyAllWindows()
import math
from matplotlib import pyplot as plt
import Matrices_Vectores
import numeros_complejos


"""
El salto de lo clasico a lo cuantico - CNYT
POR: Andrea Valentina y carolina medina
Fecha: 14/03/2021
"""


""" Funcion del esperimento del las canicas en donce recibe la matriz de adyacencia, el vector estado y el numero de clicks """

def Canicas (matriz, vector_col, clicks):
    resultado = productoMatrices(matriz, vector_col)
    if clicks == 0:
        return matriz
    if clicks > 0:
        for i in range(clicks-1 ):
            resultado = productoMatrices(matriz, resultado)

    return resultado




"""
Funcion de las multiples rendijas clásico probabilístico, con más de dos rendijas para reales y complejos
"""


def multiplesrendijasR(rendijas, blancos, clicks):

    matriz = Matrices_Vectores.crearMatrizProb(rendijas, blancos)
    vector = [0 for i in range(len(matriz))]
    vector[0] = 1
    vectorCol = Matrices_Vectores.transpuesta(vector)
    matrizResultado = Matrices_Vectores.productoMatrices(matriz, matriz)

    if clicks == 0:
        return matriz, vectorCol
    else:
        for times in range(clicks - 1):
            matrizResultado = Matrices_Vectores.productoMatrices(matriz, matrizResultado)

        vectorCol = Matrices_Vectores.productoMatrices(matrizResultado, vectorCol)

        return matrizResultado, vectorCol


def multiplesrendijasC(rendijas, blancos, clicks):

    matriz = Matrices_Vectores.crearMatrizCuant(rendijas, blancos)
    matrizResultado = Matrices_Vectores.productoMatricesComp(matriz, matriz)
    vectorResultado = []
    vectorCol = [[(0, 0) for j in range(1)] for i in range(len(matriz))]
    vectorCol[0][0] = (1, 0)

    if clicks == 0:
        return matriz, vectorCol
    else:
        for times in range(clicks - 1):
            matrizResultado = Matrices_Vectores.productoMatricesComp(matriz, matrizResultado)

        vectorCol = Matrices_Vectores.productoMatricesComp(matrizResultado, vectorCol)
        for i in range(len(vectorCol)):
            for j in range(1):
                vectorResultado.append(numeros_complejos.moduloCplx(vectorCol[i][j])**2)

        return matrizResultado, vectorResultado


"""
Funcion para hacer una grafica de barras del vector de estados
"""


def graficarEstados(valores):

    posiciones = [i for i in range(len(valores))]
    plt.bar(posiciones, valores, color="#E361B4", label="Probabilidades")
    plt.legend()
    plt.xlabel("Posicion")
    plt.ylabel("Probabilidad")
    plt.title("Probabilidades del vector de estados")
    plt.show()

def imprimirMatriz(matriz):

    for i in matriz:
        print(i)
    print()

def imprimirVector(vector):

    for i in vector:
        print(i)
    print()



def main():
    #Los experimentos de la canicas con coeficiente booleanos
    a = [[0, 1,0], [1, 0,1], [1, 0,1]]
    b = [[1], [0],[1]]
    print(Canicas(a,b,2))

    #Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.

    tupla=multiplesrendijasR(3,5,0)
    imprimirMatriz(tupla[0])
    imprimirMatriz(tupla[1])



    #Experimento de las múltiples rendijas cuántico.

    tupla2=multiplesrendijasC(2,5,1)
    imprimirMatriz(tupla2[0])
    print(tupla2[1])


    #Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen.
    graficarEstados(tupla2[1])

if __name__ == '__main__':
    main()
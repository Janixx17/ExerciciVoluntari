import sys
from Solucionador import Solucionador

def read_file():
    """
        Funcio dedicada a llegir un fitxer amb parelles amb format (x,y)\n

        :return columna1: Llista amb els valors corresponent a la x
        :return columna2: Llista amb els valors corresponent a la y
    """
    #contingut = sys.stdin.read()
    contingut = "(baa,b)\n(a,baa)\n(b,aa)\n"
    linees = contingut.split('\n')
    columna1 = []
    columna2 = []

    for linea in linees:
        if linea != '':
            valors = linea.strip('()').split(',')

            columna1.append(valors[0].strip())
            columna2.append(valors[1].strip())
    return columna1, columna2

def trobar_resultat(columna1, columna2):
    """
        Funcio la qual crida la classe Solucionador per tal de rebre el resultat

        :param columna1: Llista amb els valors corresponent a la x
        :param columna2: Llista amb els valors corresponent a la y
        :return trobat: Fals o True
        :return valor: el resultat en cas de de que s'hagi trobat el resultat o '' en cas contrari
    """
    solucionador1 = Solucionador()
    #solucionador2 = Solucionador()
    trobat, valor = solucionador1.ini_backtracking(columna1, columna2, 25)
    #trobat, valor = solucionador1.ini_backtracking(columna1, columna2, 20)
    #if not trobat:
    #    trobat, valor = solucionador2.ini_backtracking(columna1, columna2, 25)

    return trobat, valor


if __name__ == '__main__':
    columna1, columna2 = read_file()
    trobat, valor = trobar_resultat(columna1, columna2)
    print(trobat, valor)
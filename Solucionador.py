from Solucio import Solucio
from Candidat import Candidat

class Solucionador:

    sol: Solucio
    colum1 = []
    colum2 = []

    def ini_backtracking(self, columna1: [], columna2: [], profunditat: int):
        """
            Funcio dedicada a inicialitzar el backtracking

            :param columna1: Llista amb els valors corresponent a la x
            :param columna2: Llista amb els valors corresponent a la y
            :param profunditat: profunditat * n_columnes que es vol que arribi com a màxim el backtracking
            :param trobat: profunditat que es vol que arribi com a màxim el backtracking
            :return: Fals o el resultat del backtracking
        """
        trobat = False
        self.colum1 = columna1
        self.colum2 = columna2
        self.sol = Solucio(columna1, columna2, profunditat)
        trobat = self.backtracking(trobat)
        valor = ''
        if trobat:
            valor = self.sol.resultat()
        return trobat, valor


    def backtracking(self, trobat: bool):
        """
            Funcio encarregada de fer el backtracking

            :param trobat: Fals o True depenent de si s'ha trobat el resultat o no
            :return trobat: Fals o True
        """
        try:
            iCan: Candidat = self.sol.IniCandidats()
            while not iCan.Fi() and not trobat:
                if self.sol.Acceptable(iCan):
                    self.sol.AnotCandidat(iCan)
                    if not self.sol.Completa():
                        trobat = self.backtracking(trobat)
                        if not trobat:
                            self.sol.DesCandidat(iCan)
                    else:
                        trobat = True
                iCan.Seguent()

            return trobat
        except RecursionError as e:
            print("S'ha arribat al màxim de profunditat per a la recursivitat")
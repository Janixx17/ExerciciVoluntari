import random

from Candidat import Candidat

class Solucio:

    index_utilitzats: str
    string1: str
    string2: str
    col1: []
    col2: []
    usats: []
    profunditat: int

    def __init__(self, columna1: [], columna2: [], profunditat: int = 10):
        """
            Constructor amb paràmetres de la classe

            :param columna1: Valors corresponents a la primera columna
            :param columna2: Valors corresponents a la segona columna
        """
        self.index_utilitzats = ""
        self.col1 = columna1
        self.col2 = columna2
        self.string1 = ""
        self.string2 = ""
        self.usats = []
        self.profunditat = profunditat

        for i in range(len(self.col1)):
            self.usats.append(0)

    def Acceptable(self, iCan: Candidat):
        """
            Funcio per avaluar si el proxim candidat es acceptable o no

            :param iCan: Candidat a avaluar
            :return: True o False depenent de si s'accepta o no el candidat
        """
        aux_str1 = "".join([self.string1, str(self.col1[iCan.Actual()])])
        aux_str2 = "".join([self.string2, str(self.col2[iCan.Actual()])])
        llargada_text1 = len(aux_str1)
        llargada_text2 = len(aux_str2)

        retornar = False

        if llargada_text1 == llargada_text2 and aux_str1 == aux_str2:
            retornar = True
        elif llargada_text1 > llargada_text2:
            val = llargada_text1-llargada_text2
            aux_str1 = aux_str1[:-val]
            if aux_str1 == aux_str2:
                retornar = True
        elif llargada_text2 > llargada_text1:
            val = llargada_text2 - llargada_text1
            aux_str2 = aux_str2[:-val]
            if aux_str1 == aux_str2:
                retornar = True

        if retornar and len(self.index_utilitzats) >= 7 and (llargada_text1 * 0.5 >= llargada_text2 or llargada_text1 <= 0.5 * llargada_text2):
            return False

        if retornar and len(self.index_utilitzats) >= self.profunditat * len(self.col1):
            return False

        return retornar

    def AnotCandidat(self, iCan: Candidat):
        """
            Funcio encarregada d'anotar el candidat

            :param iCan: Candidat a anotar
        """
        self.string1 = "".join([self.string1, str(self.col1[iCan.Actual()])])
        self.string2 = "".join([self.string2, str(self.col2[iCan.Actual()])])
        self.index_utilitzats = "".join([self.index_utilitzats, str(iCan.Actual() + 1)])
        self.usats[iCan.Actual()] = 1

    def DesCandidat(self, iCan: Candidat):
        """
            Funcio encarregada de desanotar el candidat

            :param iCan: Candidat a desanotar
        """
        valor1 = len(self.col1[iCan.Actual()])
        valor2 = len(self.col2[iCan.Actual()])
        self.string1 = self.string1[:-valor1]
        self.string2 = self.string2[:-valor2]
        self.index_utilitzats = self.index_utilitzats[:-1]
        if not str(iCan.Actual()+1) in self.index_utilitzats:
            self.usats[iCan.Actual()] = 0

    def Completa(self):
        """
            Funcio per determinar si la solució es completa o no

            :return: True o False corresponentment
        """
        usats_tots = True
        for i in self.usats:
            if i == 0:
                usats_tots=False
                break

        strings_iguals = False
        if self.string1 == self.string2:
            strings_iguals = True
        return usats_tots and strings_iguals

    def IniCandidats(self) -> Candidat:
        """
            Funcio orientada a inicialitzar els candidats

            :return: Candidat inicialitzat
        """
        valorrand = random.randint(1, 150) % 2
        val = len(self.col1)
        iCan = Candidat(0, val, valorrand)
        return iCan

    def resultat(self):
        """
            Funcio per a retornar els index_utilitzats

            :return: index_utilitzats
        """
        return self.index_utilitzats
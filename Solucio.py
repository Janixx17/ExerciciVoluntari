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
    erronis: []
    entrats: []
    index_retorn: str

    def __init__(self, columna1: [], columna2: [], profunditat: int):
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
        self.erronis = []
        self.entrats = []
        self.index_retorn = ''

        for i in range(len(self.col1)):
            self.usats.append(0)

    def Acceptable(self, iCan: Candidat): #TODO: l'error segueix estant aqui
        """
            Funcio per avaluar si el proxim candidat es acceptable o no

            :param iCan: Candidat a avaluar
            :return: True o False depenent de si s'accepta o no el candidat
        """

        if self.index_retorn != '' and self.index_retorn != self.index_utilitzats:
            return False


        if len(self.string1) > 0: #comprovacio de que no estiguem en un cas pel que ja hem passat abans
            erroniaux = []
            erroniaux.append(''.join([self.string1[-1], str(self.col1[iCan.Actual()])]))
            erroniaux.append(''.join([self.string2[-1], str(self.col2[iCan.Actual()])]))
            erroniaux.append(''.join([str(int(self.index_utilitzats[-1]) - 1), str(iCan.Actual())]))
            erroniaux.append(self.usats)
            for i in self.erronis:
                if erroniaux == i:
                    return False

        aux_str1 = "".join([self.string1, str(self.col1[iCan.Actual()])])
        aux_str2 = "".join([self.string2, str(self.col2[iCan.Actual()])])


        retornar = False

        if len(aux_str1) == len(aux_str2) and aux_str1 == aux_str2: #comprovar que els dos strings siguin iguals
            retornar = True
        elif len(aux_str1) > len(aux_str2):
            val = len(aux_str1)-len(aux_str2)
            aux_str1 = aux_str1[:-val]
            if aux_str1 == aux_str2:
                retornar = True
        elif len(aux_str2) > len(aux_str1):
            val = len(aux_str2) - len(aux_str1)
            aux_str2 = aux_str2[:-val]
            if aux_str1 == aux_str2:
                retornar = True

        if retornar and len(self.index_utilitzats) >= 7 and (len(aux_str1) * 0.5 >= len(aux_str2) or len(aux_str1) <= 0.5 * len(aux_str2)):
            return False

        if retornar and len(self.index_utilitzats) >= self.profunditat * len(self.col1):#profunditat maxima arribada
            return False

        return retornar

    def AnotCandidat(self, iCan: Candidat):
        """
            Funcio encarregada d'anotar el candidat

            :param iCan: Candidat a anotar
        """
        if len(self.index_utilitzats) > 0:
            entrat = []
            entrat.append(''.join([self.string1[-1], str(self.col1[iCan.Actual()])]))
            entrat.append(''.join([self.string2[-1], str(self.col2[iCan.Actual()])]))
            entrat.append(''.join([str(int(self.index_utilitzats[-1]) - 1), str(iCan.Actual())]))
            aux_index = "".join([self.index_utilitzats, str(iCan.Actual() + 1)])
            aux_usats = self.usats
            aux_usats[iCan.Actual()] = 1
            entrat.append(aux_usats)
            entrat.append(aux_index)
            self.entrats.append(entrat)

        self.string1 = "".join([self.string1, str(self.col1[iCan.Actual()])])
        self.string2 = "".join([self.string2, str(self.col2[iCan.Actual()])])
        self.index_utilitzats = "".join([self.index_utilitzats, str(iCan.Actual() + 1)])
        self.usats[iCan.Actual()] = 1

    def DesCandidat(self, iCan: Candidat):
        """
            Funcio encarregada de desanotar el candidat

            :param iCan: Candidat a desanotar
        """
        if self.index_retorn == '': #TODO: no entrar erronis repetits
            erroni = []
            erroni.append("".join([self.string1[-1], str(self.col1[iCan.Actual()])]))
            erroni.append("".join([self.string2[-1], str(self.col2[iCan.Actual()])]))
            erroni.append("".join([str(int(self.index_utilitzats[-1]) - 1), str(iCan.Actual())]))
            erroni.append(self.usats)
            self.erronis.append(erroni)


            trobat = False
            for j in self.erronis:
                for i in self.entrats:
                    if j[0] == i[0] and j[1] == i[1] and j[2] == i[2] and i[4] != self.index_utilitzats[:-1] and i[4] != self.index_utilitzats and j[3] == i[3]:
                        self.index_retorn = i[4]
                        trobat = True
                        break
                if trobat:
                    break

        if self.index_retorn == self.index_utilitzats[:-1]:
            self.index_retorn = ''

        valor1 = len(self.col1[iCan.Actual()])
        valor2 = len(self.col2[iCan.Actual()])
        self.string1 = self.string1[:-valor1]
        self.string2 = self.string2[:-valor2]
        self.index_utilitzats = self.index_utilitzats[:-1]
        if not str(iCan.Actual()+1) in self.index_utilitzats:
            self.usats[iCan.Actual()] = 0

        self.entrats = self.entrats[:-1]


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
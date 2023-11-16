import random
class Candidat:

    min_valor: int
    valor_dir: int
    max_valor: int
    val_actual: int
    val_final: int
    visitat: int

    def __init__(self, valor_minim: int, max_valors: int, randvalue: int):
        """
            Funcio amb paràmetres per a inicialitzar el candidat

            :param valor_minim: valor mínim que pot prendre el candidat
            :param max_valors: valor màxim que pot prendre el candidat
            :param randvalue: valor siguent 0 o diferent de 0 per determinar en quin sentit es recorreran els candidats
        """
        self.min_valor = valor_minim #0
        self.max_valor = max_valors #3
        self.valor_dir = randvalue
        self.val_actual = random.randint(0, 123) % max_valors
        self.val_final = self.val_actual
        self.visitat = 0
    def Actual(self):
        """
            Funcio per retornar quin es el candidat actual

            :return: Valor actual que pren el candidat
        """
        return self.val_actual

    def Fi(self):
        """
            Funcio per determinar quan s'han provat tots els candidats

            :return: True o False corresponentment
        """
        return self.val_actual == self.val_final and self.visitat != 0

    def Seguent(self):
        """
            Funcio per passar al següent candidat
        """
        self.visitat = self.visitat+1
        if self.valor_dir == 0:
            self.val_actual = self.val_actual+1
            if self.val_actual == self.max_valor:
                self.val_actual = self.min_valor
        else:
            self.val_actual = self.val_actual-1
            if self.val_actual < self.min_valor:
                self.val_actual = self.max_valor-1
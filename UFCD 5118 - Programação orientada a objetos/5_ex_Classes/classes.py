"""
Classe Bola: Crie uma classe que modele uma bola: <- Done

Atributos: Cor, circunferência, material <- Done
Métodos: trocaCor e mostraCor

"""


class Bola:
    def __init__(self,
                 cor: str,
                 circunferencia:float,
                 material:str
                 ):

        self.cor = cor
        self.material = material
        self.circunferencia = circunferencia


    def trocaCor(self, nova_cor: str):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

"""

class Quadrado:
    def __init__(self,lado:float):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self,lado):
        self.lado = lado

    def calcularArea(self):
        ## return self.lado ** 2
        # return self.lado * self.lado
        return pow(self.lado, 2)

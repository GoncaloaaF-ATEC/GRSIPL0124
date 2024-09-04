from classes import Bola


bola1 = Bola(cor= "Amarelo",
             circunferencia= 20,
             material= "pano")

bola2 = Bola(cor= "Amarelo",
             circunferencia= 20,
             material= "pano")


print(bola1.mostraCor())
print(bola2.mostraCor())
bola1.trocaCor("Vermelho")
print(" bola1.trocaCor(\"Vermelho\") ")
print(bola1.mostraCor())
print(bola2.mostraCor())


print("-------------")

print(2 ** 2)
print(2 ** 10)
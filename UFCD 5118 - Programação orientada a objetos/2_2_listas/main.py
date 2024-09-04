"""

List -> [ ]
set -> {}

"""
from sympy import prime

# lista

lista = ["valor1", "valor2", "valor3", "valor4", "valor5"]

print(lista)

print(lista[0])

lista[0] = "Novo valor"

print(lista[0])


print("----")

nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia",
    "Paulo", "Quintino", "Raquel", "Samuel", "Tatiana",
    "Ursula", "Vitor", "Wesley", "Xavier", "Yasmin"
]

print(nomes[0]) # Ana

print(nomes[-1]) # Yasmin
print(nomes[-4]) # Vitor

print(nomes[2]) # Carlos
print(nomes[6]) # Gabriel

print(nomes[2:7]) # todos os valores entre o index 2 e o index 7-1

print(nomes[0:7]) # todos index ate ao 7-1

print(nomes[:7]) # todos index ate ao 7-1

print(nomes[7:]) # todos index ate ao 7-1


print("----")


numeros = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

print(numeros[5 : 50: 5])

print(numeros[::-5])

print(numeros[-5 : -50: 5])
print(numeros[-50 : -5: 5])

print("---")
print("Ana" in nomes)
# print(nomes in "Ana" )

print("---")

for nome in nomes:
    print(nome)

print("---")
print(nomes)

nomes[0] = "Sem nome"

print(nomes)

nomes[5:8] = ["Sem nome"]

print(nomes)


print("---")

lista = ["valor1"]

print(lista)

lista.append("valor2")
print(lista)


print("------")
lista = ["valor1"]
lista.append(["valor3","valor4"])
print(lista.__len__())
print(len(lista))
print(lista)

print("--")
lista = ["valor1"]
lista.extend(["valor3","valor4"])

print(lista.__len__())
print(len(lista))
print(lista)

print("------")


lista = ["valor1", "valor2", "valor3", "valor4", "valor5"]


lista.insert(1, "Novo valor")
print(lista)


lista.append("Novo valor 1")
lista.append("Novo valor 2")
lista.append("Novo valor 3")
lista.append("Novo valor 4")
lista.append("Novo valor 5")
print(lista)

print("------")
print(lista.count("Novo valor"))
print(lista.count("valor1"))
print(lista.count("valor99"))


print("------")
print(lista)
print(lista.count("Novo valor"))
lista.remove("Novo valor")
print(lista.count("Novo valor"))
print(lista)
print("------")


print(lista)
lista.pop()
print(lista)
print("------")

print(lista)
lista.pop(3)
print(lista)

print("------")
print(lista)
lista.sort(reverse=True)
print(lista)

print("------")
print(nomes)
nomes.sort(reverse=True)
print(nomes)

print("------")

print("--- List Comprehension ---")

# newlist = [expression for item in iterable if condition == True]

print(nomes)
print(nomes[1][-1])

nome = "Gonçalo"
print(nome[-1])


print("------")

novaLista = [n.upper() for n in nomes if "a" in n]
print(novaLista)


# set

print("--- set ---")
print("------")

set1 = {"Polvilho", "Ovos", "Leite", "Sal", "Queijo", "Oleo"}

print(set1)
'''
{'queijo', 'Leite', 'Oleo', 'sal', 'ovos', 'Polvilho'}
{'ovos', 'sal', 'queijo', 'Leite', 'Polvilho', 'Oleo'}

'''

print("---")
set2 = {"Farinha", "Ovos", "Iogurte", "Oleo", "Açucar", "Ovos"}
print(set2)

print("---")

for i in set2:
    print(i)

print("---")
print("ovos")
print("ovos".capitalize())
print("ovos".capitalize() in set2)

print("---")
print("figos".capitalize() in set2)
print("figos".capitalize() not in set2)

print("-- add --")
print(set2)
set2.add("Fermento")
print(set2)

print("---")

print(set2)
set2.add("Fermento")
print(set2)

print("---")

set2.add("figos")
print(set2)
set2.remove("figos")
print(set2)

print("--update--")

print(set2)
lista = ["val1", "val2"]
set2.update(lista)

print(set2)


print("--- operações com Sets ---")
print(set1)
print(set2)

print("-- union --")

print(set1.union(set2))
print(set1.union(set2))


print("-- intersection --")

print(set1.intersection(set2))
print(set1.intersection_update(set2))

print("-- difference --")

print(set1.difference(set2))
print(set2.difference(set1))
#set2.difference_update(set1)

print("---")

print(set1.symmetric_difference(set2))
# set2.symmetric_difference_update(set1)


# dict

print("--- dict ---")

device = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.1",
    "username": "admin",
    "password": "admin"
}

print(device)

print(device["device_type"])

device["device_type"] = "cisco"

print(device)

print("------")

device["model"] = "CISCO2801"

print("------")

print(device)

print("--- ler v2 ---")

print(device["model"])
print(device.get("model"))

print("----")

#print(device["modelo"]) <- se nao existe gera um erro
print(device.get("modelo"))

print("------")

print(device)
device.pop("model")
print(device)

print("------")

print(device.keys())
print(device.values())

print("------")

for elm in device:
    print(elm)
    print(device[elm])
    print("--")

print("------")

for elm in device.values():
    print(elm)

print("------")
for elm in device.items():
    print(f"k: {elm[0]},\t\tv: {elm[1]}")
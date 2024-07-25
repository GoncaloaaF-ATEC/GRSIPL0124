print("Ola Mundo")

nome = "Valor"  # str
print(nome)

'''
comnet 
multi
linha
'''

idade = 10  # int
ano = 2031

soma = idade + ano

print(soma)

media = soma / 2

print(media)

soma2 = media + 20

print(type(soma2))

#max int  java -> 2 147 483 647

soma2 = "sem valor"

print(type(soma2))

idade = 20
print("----prt1----")
print("nome: " + nome + "\nidade: " + str(idade))
print("----prt2----")
print(f"nome: {nome} \nidade: {idade}")

# condições -> if,  "swith"
print("----if----")
val = 2

if val == 1:
    print("val = 1")
    print("ainda dentro do if")
elif val == 2:
    print("val = 2")
    print("ainda dentro do elif (else if)")
else:
    print("val != 1")
    print("ainda dentro do else")

print("Fora do if")

print("----swith - match----")

val = 145678

match val:
    case 1:
        print("val = 1")
    case 5:
        print("val = 5")
    case 10:
        print("val = 10")
    case _:
        print("outro valor")

print(" condição \"complexas\" ")

# && <- and
# || <- or


v1 = True
v2 = False

print(v1 or v2)
print(v1 and v2)

val1 = 10
val2 = 20
print(not (val2 > 10 and val1 < 50))

# loops -> for, while

print("----range----")

r1 = range(0, 10, 2)  # range(lb, ub, step) ->  lb ate ub-1, de step em step, se o step for omitido step = 1

# for(val in ...)
print("----for range----")
for i in r1:
    print(i)

print("----for str----")
for i in "lorem ipsum":
    print(i)

print("----while----")
val = 100
while val > 0:
    print(val)
    val -= 1

print("--------------for v2 ------------")

for i in range(0, 1000, 10):

    if i % 20 == 0:
        continue

    if i == 120:
        break

    print(i)


# func -> funções

def nome():
    print("Ola Mundo")


nome()
nome()
nome()


def nome2(txt: str, ano: int = 1991):
    # pass # <- bloco vazio
    print(f"Ola {txt}, em {ano} ")


print("------")
nome2("Mundo", 2013)
nome2("Gonçalo", 1231)
nome2("bla bla bla", 41212)
nome2("py")

print("-----")


def genMsg(nome: str, ano: int = 1991) -> str:
    return f"Ola {nome}, em {ano}"

print(genMsg("Mundo"))



# lists

# set

#dict


# classes

# herança

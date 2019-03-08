# criar uma lista vazia
lista = []
# criar uma lista com tamanho 10
lista2 =  [""]*10

# adicionar um elemento na lista

lista.append (5)
lista.append (18)
lista.append (1)
lista.append (3)
lista.append (11)
lista.append (15)
lista.append (4)

# alterar valor da lista
lista[3] = 44

print("Resultado da lista:", lista)
# calcular tamanho da lista

t = len(lista)
i = 0

while i < t:
    #print("na posição", i, "tem o valor", lista[i])
    print("na posicao {} tem o valor {}.".format(i, lista[i]))
    i += 1

print("\n___________________________________\n")

# usando o for na maneira foreach

for x in lista:
    print("Valor da lista:", x)

#uso do for normal
# len calcula o tamanho da lista e range cria uma sequencia numeria com o tamanho da lista
for i in range(len(lista)):

    print("na posicao {} tem o valor {}.".format(i, lista[i]))

# criação de função
def dobro(num):
    d = num * 2
    print("O dobro de {} é {}.".format(num, d))
    return d, num

a, b = dobro(5)
print("Os retornos são: {} e {}.".format(a,b))

liczby = input()
lista = liczby.split(',')

print(lista, type(lista))

for i in range (len(lista)):
    lista[i] = int(lista[i])

print(lista, type(lista))

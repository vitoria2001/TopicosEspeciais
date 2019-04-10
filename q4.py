l = list()
for i in range(15):
    valor = int(input())
    l.append(valor)

print("LISTA: ", l)
print("Valor Máximo que está na lista: %d"%(max(l)))
print("Posição onde se encontra o valor máximo da lista: ", l.index(max(l)))

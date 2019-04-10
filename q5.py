l = list()
for i in range(6):
    va = float(input())
    if (va >=1):
        l.append(va)
soma = sum(l)
print("Média dos valores Positivos: %.1f" %(soma/len(l) ))
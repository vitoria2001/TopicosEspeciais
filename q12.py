td = list()
vp = float(input())
while (vp != 0):
    da = int(input())
    if (da==0):
        print("O valor total da Prestação: R$ %.2f" %(vp))
        td.append(vp)
    else:
        juros = vp+(10*0.3)+((10*0.01)*da)
        print("O valor total da Prestação: R$ %.2f" %(juros))
        td.append(juros)
    vp = float(input())


calculoFinal = sum(td)

print("Total de Prestações pagas no dia de hoje: R$ %.2f" %(calculoFinal))


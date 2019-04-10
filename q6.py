qntpzza = int(input("Quantas pizzas desejadas: "))
precopzza = float(input("Valor da Pizza: R$ "))
custo = qntpzza*precopzza
imposto = custo-custo*0.8
total = custo + imposto
print("O valor total do pedido é: R$ %.2f" %(total))
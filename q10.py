qntcigarro = int(input())
anosfumando = int(input())

calc1 = qntcigarro*10 # 100 cigarros diarios = 1000 minutos perdidos
calc2 = anosfumando*12 # 5 anos fumando = 60 meses = 21900 dias fumando = 525600 horas = 31536000 minutos

anosPerdidos=( ( (calc1/60)/24)/365)

calcFinal = ((((calc1*365)*calc2 )/12)/1000)/60

print("Você perdeu %d anos"%(calcFinal))



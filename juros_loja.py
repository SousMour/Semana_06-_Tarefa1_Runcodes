#Valor para pagamento à vista, com desconto de 9%.
# Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
#Valor da prestação para pagamento em 10 vezes, com 17% de juros.

x=float(input())
av=x*0.91
prt_5=x/5
prt_10=(x*1.17)/10

print(f'{av:.2f}')
print(f'{prt_5:.2f}')
print(f'{prt_10:.2f}')


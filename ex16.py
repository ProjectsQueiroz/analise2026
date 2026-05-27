#Desenvolver um código em python que leia um valor e imprima se o valor lido está dentro das faixas abaixo:
#entre 0 e 10, entre 11 e 20 e entre 21 e 30
n = int(input("Por favor digite um número entre 0 e 30: "))
if n >= 0 and n <=10:
    print("Seu número está entre 0 e 10")
elif n >= 11 and n <= 20:
    print("Seu número está entre 11 e 20")
elif n >= 21 and n <= 30:
    print("Seu número está entre 21 e 30")
elif n > 30:
    print("Seu número é maior que 30")
else:
    print("Seu número é negativo")
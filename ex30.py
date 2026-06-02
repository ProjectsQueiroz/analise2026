# Desenvolva um código python que leia um valor e mostre a tabuada desse valor usando 'for'
num = int(input("Digite um número para saber a sua tabuada: "))
for i in range(1,11):
    print(f"{i} x {num} = {num * i}")
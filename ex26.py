#desenvolva um código em python que leia 5 valores e diga cada m deles se é par ou impar
import random

for i in range(0,5):
    num = random.randint(1,10)
    print(f"Número sorteado é: {num}")
    if num % 2 == 0:
        print(f"O número {num} é par!")
    else:
        print(f"O número {num} é impar!")

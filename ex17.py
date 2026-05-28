#Desenvolva um códio python que verifique se a temperatura está fria, agradável ou calor
# segue a tabela:
# < 18 = frio
# entre 18 e 30 = calor
# > 30 = calor

temp = float(input("Qual a temperatura em ºC da sala agora? / "))
if temp < 18:
    print("Está frio!")
elif temp >= 18 and temp <= 30:
    print("A temperatura está agradável!")
else:
    print("Está calor!")
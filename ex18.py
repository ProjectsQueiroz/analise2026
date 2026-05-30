#uma empresa precisa automatizar o cálculo do salário líquido de seus funcionáros com base no cargo que ocupam e nas deduções de impostos (INSS e IRRF). Esceva um programa em Python que receba o cargo de um colaborador e realize os cálculos descritos a seguir:
# Cargo 
# caixa R$ 1500
# vendedor  R$ 2400
# Gerente   R$ 4000
# Outros R$ 0 (Não trabalha aqui)
#Desconto do inss é fixo para todos os cargos 12%
#IRRF se <= 2000 == 8% se > 2000 == 14%
#Ao final, o prorama deve exibir de forma organizada as seguintes informações:
#Salário Bruto Mensal - Valor descontado do INSS - Valor descontado de IRRF - Salário Final (Líquido)

print("Bem vindo ao calculador de salário!")
cargo = input("Digite o seu cargo: ").upper()

if cargo == "CAIXA":
    salario = float(1500)
    inss = salario * 0.12
    irrf = salario * 0.08
    print(f"==============================================")
    print(f"============ Bem-vindo, {cargo}! ===============")
    print(f"==============================================")
    print(f"= Descrição       => Valor                   =")
    print(f"=--------------------------------------------=")
    print(f"= Salário bruto   => {salario} 😊               =")
    print(f"= INSS            => {inss} 💸                =")
    print(f"= IRRF            => {irrf} 💸                =")
    print(f"= Salário líquido => {salario - inss - irrf} 💵               =")
    print(f"==============================================")
elif cargo == "VENDEDOR":
    salario = float(2400)
    inss = salario * 0.12
    irrf = salario * 0.12
    print(f"==============================================")
    print(f"============ Bem-vindo, {cargo}! ============")
    print(f"==============================================")
    print(f"= Descrição       => Valor                   =")
    print(f"=--------------------------------------------=")
    print(f"= Salário bruto   => {salario} 😊               =")
    print(f"= INSS            => {inss} 💸                =")
    print(f"= IRRF            => {irrf} 💸                =")
    print(f"= Salário líquido => {salario - inss - irrf} 💵               =")
    print(f"==============================================")
elif cargo == "GERENTE":
    salario = float(4000)
    inss = salario * 0.12
    irrf = salario * 0.12
    print(f"==============================================")
    print(f"============= Bem-vindo, {cargo}! ============")
    print(f"==============================================")
    print(f"= Descrição       => Valor                   =")
    print(f"=--------------------------------------------=")
    print(f"= Salário bruto   => {salario} 😊               =")
    print(f"= INSS            => {inss} 💸                =")
    print(f"= IRRF            => {irrf} 💸                =")
    print(f"= Salário líquido => {salario - inss - irrf} 💵               =")
    print(f"==============================================")
else:
    print("Não trabalha aqui! Cai fora!")
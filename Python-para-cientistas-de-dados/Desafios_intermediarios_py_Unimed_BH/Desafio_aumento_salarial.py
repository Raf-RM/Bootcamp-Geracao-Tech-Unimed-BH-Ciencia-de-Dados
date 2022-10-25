salario = float(input()) 

def novo_salario(salario, reajuste_percent):
    reajuste = (salario * (reajuste_percent / 100))
    salario_novo = salario + reajuste
    return f"Novo salario: {salario_novo:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {reajuste_percent} %"

if (salario > 0 and salario <= 600):
    reajuste_percent = 17
    print(novo_salario(salario, reajuste_percent))

elif (salario > 600 and salario <= 900):
    reajuste_percent = 13
    print(novo_salario(salario, reajuste_percent))
 
elif (salario > 900 and salario <= 1500):
    reajuste_percent = 12
    print(novo_salario(salario, reajuste_percent))
 
elif (salario > 1500 and salario <= 2000):
    reajuste_percent = 10
    print(novo_salario(salario, reajuste_percent))

else: 
    reajuste_percent = 5
    print(novo_salario(salario, reajuste_percent))
 
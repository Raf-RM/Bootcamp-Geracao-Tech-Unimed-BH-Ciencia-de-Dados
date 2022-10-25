



#for item in lista_entrada:
#    print(dic_papagaio[item])

while True:
    try:
        entrada = input()
#        lista_entrada = entrada.split()
        dic_papagaio = {
            "esquerda" : "ingles",
            "direita" : "frances",
            "nenhuma" : "portugues",
            "ambas" : "caiu"
            }        
        print(dic_papagaio[entrada])
    except EOFError:
        break

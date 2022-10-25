def VerificaLetras( lista_letras_total, senha):
# -- VERIFICA SE A SENHA CONTEM AO MENOS UM ITEM DO TIPO LETRAS

    for i in range(len(lista_letras_total)):
        if lista_letras_total[i] in list(senha):
           letras_verificado = True
           break 
        else:
                letras_verificado = False
    return letras_verificado

def VerificaNumeros( lista_numeros, senha):
# -- VERIFICA SE A SENHA CONTEM AO MENOS UM ITEM DO TIPO NUMEROS

    for i in range(len(lista_numeros)):
        if lista_numeros[i] in list(senha):
            numeros_verificado = True
            break 
        else:
            numeros_verificado = False
    return numeros_verificado        

def VerificaEspeciais( lista_especiais, senha):
# -- VERIFICA SE A SENHA CONTEM AO MENOS UM ITEM DO TIPO CARACTERES ESPECIAIS

    for i in range(len(lista_especiais)):
        if lista_especiais[i] in list(senha):
            especiais_verificado = True
            break 
        else:
            especiais_verificado = False
    return especiais_verificado
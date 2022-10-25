from mailbox import NotEmptyError


class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Rafael", 1235)
aluno_2 = Estudante("Valeria", 2135)

#AMBOS ALUNOS APRESENTARAM A VARIAVEL escola = DIO JÁ QUE ESSA É UMA
#VARIAVEL DE CLASSE
mostrar_valores(aluno_1, aluno_2)

#PODEMOS ALTERAR TANTO NOME QUANTO MATRICULA DE CADA OBJETO ALUNO
#SEM ALTERAR ESSAS INSTANCIAS DOS DEMAIS OBJETOS ALUNO
aluno_1.matricula = 1216
mostrar_valores(aluno_1, aluno_2)

#AO ALTERARMOS A VARIÁVEL escola DA CLASSE NÓS ALTERAMOS SEU VALOR
#PARA TODAS AS INSTANCIAS ALUNO DA CLASSE ESTUDANTE
Estudante.escola = "Alura"
mostrar_valores(aluno_1, aluno_2)

#A PARTIR DE ENTÃO NOVOS OBJETOS ALUNOS INSTANCIADOS TAMBÉM APRESENTARAM
#O NOVO VALOR DA VARIAVEL estudante
aluno_3 = Estudante("Mateus", 3235)
mostrar_valores(aluno_1, aluno_2, aluno_3)

#É POSSÍVEL ALTERARMOS A VARIAL DE CLASSE SOMENTE DE UM DOS
#DOS OBJETOS INSTANCIADOS
aluno_2.escola = "DIO"
mostrar_valores(aluno_1, aluno_2, aluno_3)
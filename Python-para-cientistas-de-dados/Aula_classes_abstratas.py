from abc import ABC, abstractmethod, abstractproperty
#CONSTRUINDO CLASSES ABSTRATAS UTILIZANDO O MÓDULO ABC

#INICIALMENTE ESTENDEMOS A CLASSE COMO UMA EXTENSÃO DO MÓDULO ABC
class ControleRemoto(ABC):
    
#MÉTODOS ABSTRATOS NÃO NESCESSARIAMENTE TERÃO UM CORPO
#E TODAS AS CLASSES FILHAS SÃO OBRIGADAS A IMPLEMENTAR
#ESSES MÉTODOS NÃO PODERAM SER INSTANCIADOS    
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

#TAMBÉM PODEMOS FORÇAR PROPRIEDADES (property) DENTRO DA CLASSE
#EMPREGANDO O DECORADOR @abstractproperty
    @property
    @abstractproperty
    def marca(self):
        pass    

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV ...")
        print("Ligada")

    def desligar(self):
        print("Desligando a TV ...")
        print("Desligada")

    @property
    def marca(self):
        return "Lg"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI=3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura=latura

    def aria(self):
        print(f'Aria este {(self.__latura**2)}')

    def get_latura(self):
        return self.__latura

    def set_latura(self,lungime_latura):
        self.__latura=lungime_latura

    def del_latura(self):
        self.__latura=None

    def descrie(self):
        print('Eu am 4 colturi egale')


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        print(f'Aria este {self.PI*self.__raza**2}')

    def get_raza(self):
        return self.__raza

    def set_raza(self,lungime_raza):
        self.__raza=lungime_raza

    def del_raza(self):
        self.__raza=None

    def descrie(self):
        print('Eu nu am colturi')

p1=Patrat(3)

print(p1.get_latura())
p1.aria()
p1.set_latura(5)
p1.aria()
p1.descrie()
print(p1.get_latura())
# p1.del_latura() - returneaza eroare pt ca latura este setata pe None


c1=Cerc(4)

c1.descrie()
print(c1.get_raza())
c1.aria()
c1.set_raza(5)
c1.aria()
print(c1.get_raza())





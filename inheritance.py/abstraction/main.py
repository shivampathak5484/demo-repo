from abc import ABC ,abstractmethod
class car(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def chasis(self):
        pass
    @abstractmethod
    def color(self):
        pass

class hyundai(car):
    def __init__(self,a):
        self.a=a

    a=""

    def engine(self):
        print("engine",self.a)

    def chasis(self):
        print("chasis")

    def color(self):
        print("color")

a=hyundai(1)
a.engine()



    
    

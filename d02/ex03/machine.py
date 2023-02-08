from beverages import *
import random

class CoffeeMachine:
    def __init__(self):
        self._count = 0
        self._broken = False

    class EmptyCup(HotBeverage):
        pass
        def __init__(self, _price=0.90 , _name="empty cup"):
            super().__init__(_price, _name)
        def description(self):
            return("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        if self._broken == True:
            self._count = 0
            self._broken = False
            print("Machine repaired.")
    
    def serve(self, derived_class):
        if self._count < 10:
            self._count += 1
            num = random.randint(0, 100)
            if num % 2 == 0:
                return(derived_class)
            else:
                return(self.EmptyCup())
        else:
            self._broken = True
            raise CoffeeMachine.BrokenMachineException() 


def test_Machine():
    _CoffeMachine = CoffeeMachine()
    classes = [Coffee, Tea, Chocolate, Cappucino]

    i = 0
    while i < 2:
        count = 1
        while count <= 10:
            for elements in classes:
                if count <= 10:
                    print("-----------------------------------------", count)
                    print(_CoffeMachine.serve(elements()))
                    count += 1
        print("-----------------------------------------", count)
        try:
            print(_CoffeMachine.serve(elements())) 
        except Exception as exception:
            print(exception.args[0])
        print("---------- Fixing machine ------------------------>")
        _CoffeMachine.repair()
        i += 1
    

if __name__ == '__main__':
    test_Machine()
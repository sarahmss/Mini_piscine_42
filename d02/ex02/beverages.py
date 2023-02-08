class HotBeverage:
    def __init__(self, _price=0.30 , _name="hot beverage"):
        self.price = _price
        self.name = _name
    def description(self):
        return("Just some hot water in a cup.")
    def __str__(self):
        return("name : " + self.name + "\nprice : " + format(self.price, '.2f')+ "\ndescription : " + self.description())


class Coffee(HotBeverage):
    def __init__(self, _price=0.40 , _name="coffee"):
       super().__init__(_price, _name)
    def description(self):
        return("A coffee, to stay awake.")
    
class Tea(HotBeverage):
    def __init__(self, _name="tea"):
        super().__init__(_name=_name)

class Chocolate(HotBeverage):
    def __init__(self, _price=0.50 , _name="chocolate"):
       super().__init__(_price, _name)
    def description(self):
        return("Chocolate, sweet chocolate...")

class Cappucino(HotBeverage):
    def __init__(self, _price=0.45 , _name="cappucino"):
       super().__init__(_price, _name)
    def description(self):
        return("Un po’ di Italia nella sua tazza!")

def test_HotBevarage():
    _HotBevarage = HotBeverage()
    _Coffe = Coffee()
    _Tea = Tea()
    _Chocolate = Chocolate()
    _Cappucino = Cappucino()

    print("--------------- Parent Class ------------------")
    print(_HotBevarage)
    print("--------------- Child Class ------------------")
    print(_Coffe)
    print("------------------------------------------------")
    print(_Tea)
    print("------------------------------------------------")
    print(_Chocolate)
    print("------------------------------------------------")
    print(_Cappucino)
    print("------------------------------------------------")



if __name__ == '__main__':
    test_HotBevarage()
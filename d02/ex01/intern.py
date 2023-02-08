
class intern:
    def __init__(self, _name="My name? I’m nobody, an intern, I have no name."):
        self.Name = _name
    def __str__(self):
        return self.Name
    class Coffee:
        def __str__(self):
            return("This is the worst coffee you ever tasted.")
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    def make_coffee(self):
        return(self.Coffee())

def test_intern():
    _intern = intern()
    _parametric_intern = intern("Mark")

    print("--------- Displaying the name of each instance ----------")
    print(_intern)
    print(_parametric_intern)
    print("--------- Asking mark to make a coffee ----------")
    print(_intern.Coffee())
    print("--------- Asking the other intern to work ----------")
    try:
        _parametric_intern.work()
    except Exception as exception:
        print(exception.args[0])
    print("--------- calling make_coffe from an instance of intern ----------")
    print(_intern.make_coffee())

if __name__ == '__main__':
    test_intern()
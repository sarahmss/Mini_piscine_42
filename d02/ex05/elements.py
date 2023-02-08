from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content)

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='meta', attr=attr, content=content)

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', attr=attr, content=content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content) 

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, content=content)   

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content)   

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='simple')

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', attr=attr, content=content, tag_type='simple')

def test_Elements():
   
    classes = [Html, Head, Body, Title, Meta,
                Img, Table, Th, Tr, Td, Ul,
                Ol, Li, H1, H2, P, Div, Span, Hr, Br]

    try:
        print("---------Testing classes-----------")
        for elements in classes:
            print(elements())
        print("------Testing pdf requirements-----")
        print( Html( [Head(), Body()] ) )
        print("---------------------------------")
        print(Html([Head(Title(Text("'Hello ground!'"))), Body([H1(Text("'Oh no, not again!'")), Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])]))
        
    except Exception as exception:
        print(exception.args[0]) 
    
if __name__ == '__main__':
    test_Elements()
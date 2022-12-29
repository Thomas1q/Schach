
class Figur:
    def __init__(self, color):
        self.color = color


class Turm(Figur):
    def __init__(self, color):
        super().__init__(color)
        
class Springer(Figur):
    def __init__(self, color):
        super().__init__(color)
        
class Läufer(Figur):
    def __init__(self, color):
        super().__init__(color)

class Dame(Figur):
    def __init__(self, color):
        super().__init__(color)
        
class König(Figur):
    def __init__(self, color):
        super().__init__(color)
        
class Bauer(Figur):
    def __init__(self, color):
        super().__init__(color)
        

class Move:
    def __init__(self):
        pass

        

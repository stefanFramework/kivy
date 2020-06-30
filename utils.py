class TupleInterface:
    def get_tuple(self):
        pass


class Position(TupleInterface):
    x = None
    y = None

    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y
    
    def get_tuple(self):
        return self.x, self.y

class Size(TupleInterface):
    width = None
    height = None

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def get_tuple(self):
        return self.width, self.height
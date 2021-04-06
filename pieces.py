class Piece():
    def __init__(self,id,bn,x,y):
        self.id=id #Numero identificatorio de pieza
        self.color=bn #Si es blanca 0 o negra 1
        self._x=x #posicion en el tablero
        self._y=y
    
    def get_pos(self):
        return (self._x,self._y)

    def set_pos(self,x,y):
        self._x=x #posicion en el tablero
        self._y=y

    def get_id(self):
        return self.id

    def get_bn(self):
        return self.color

    def __repr__(self):
        return str(self._x)+','+str(self._y)

    
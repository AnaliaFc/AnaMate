import pygame,colors,pieces

#No tocar esta primer variable a no ser que se cambien las dimensiones del tablero
_coords_Tablero=[[120, 40], [170, 40], [220, 40], [270, 40], [320, 40], [370, 40], [420, 40], [470, 40],
                 [120, 90], [170, 90], [220, 90], [270, 90], [320, 90], [370, 90], [420, 90], [470, 90], 
                 [120, 140], [170, 140], [220, 140], [270, 140], [320, 140], [370, 140], [420, 140], [470, 140],
                 [120, 190], [170, 190], [220, 190], [270, 190], [320, 190], [370, 190], [420, 190], [470, 190],
                 [120, 240], [170, 240], [220, 240], [270, 240], [320, 240], [370,240], [420, 240], [470, 240],
                 [120, 290], [170, 290], [220, 290], [270, 290], [320, 290], [370, 290], [420, 290], [470, 290],
                 [120, 340], [170, 340], [220, 340], [270, 340], [320, 340], [370, 340], [420, 340], [470, 340],
                 [120, 390], [170, 390], [220, 390], [270, 390], [320, 390], [370, 390], [420, 390], [470, 390]]

peon_blanco=pygame.image.load("piezasImg\\pawn_white.png")
peon_negro=pygame.image.load("piezasImg\\pawn_black.png")
torre_blanco=pygame.image.load("piezasImg\\rook_white.png")
torre_negro=pygame.image.load("piezasImg\\rook_black.png")
caballo_blanco=pygame.image.load("piezasImg\\knight_white.png")
caballo_negro=pygame.image.load("piezasImg\\knight_black.png")
alfil_blanco=pygame.image.load("piezasImg\\bishop_white.png")
alfil_negro=pygame.image.load("piezasImg\\bishop_black.png")
reina_blanco=pygame.image.load("piezasImg\\queen_white.png")
reina_negro=pygame.image.load("piezasImg\\queen_black.png")
rey_blanco=pygame.image.load("piezasImg\\king_white.png")
rey_negro=pygame.image.load("piezasImg\\king_black.png")

lista_img_blanca=[peon_blanco,torre_blanco,caballo_blanco,alfil_blanco,reina_blanco,rey_blanco]
lista_img_negro=[peon_negro,torre_negro,caballo_negro,alfil_negro,reina_negro,rey_negro]

def crear_piezas(lista_Blancas,lista_Negras):
    x=120
    y=90
    for i in range (8):#peones
        lista_Blancas.append(pieces.Piece(0,0,x,y))
        lista_Negras.append(pieces.Piece(0,1,x,430-y))
        x += 50
    
    x=120
    y=40
    for i in range (2):#torres
        lista_Blancas.append(pieces.Piece(1,0,x,y))
        lista_Negras.append(pieces.Piece(1,1,x,430-y))
        x=470

    x=170
    y=40
    for i in range (2):#caballo
        lista_Blancas.append(pieces.Piece(2,0,x,y))
        lista_Negras.append(pieces.Piece(2,1,x,430-y))
        x=420

    x=220
    y=40
    for i in range (2):#alfil
        lista_Blancas.append(pieces.Piece(3,0,x,y))
        lista_Negras.append(pieces.Piece(3,1,x,430-y))
        x=370
    
    #Reina
    lista_Blancas.append(pieces.Piece(4,0,320,40))
    lista_Negras.append(pieces.Piece(4,1,320,390))

    #Rey
    lista_Blancas.append(pieces.Piece(5,0,270,40))
    lista_Negras.append(pieces.Piece(5,1,270,390))

def dibujarTablero(screen):
    indice = 1
    for c in range(len(_coords_Tablero)):
        x=_coords_Tablero[c][0]
        y=_coords_Tablero[c][1]
        if indice == 1:
                pygame.draw.rect(screen, colors._LIGHT_GRAY, [x,y, 50, 50])
        else:pygame.draw.rect(screen, colors._DARK_GRAY, [x,y, 50, 50])
        indice *= -1
        if c in [7,15,23,31,39,47,55]:
            indice *= -1

def dibujarPiezas(screen,lista):
    for n in range (len(lista)):
        if lista[n].color==0:
            screen.blit(lista_img_blanca[lista[n].id],(lista[n]._x,lista[n]._y))
        elif lista[n].color==1:
            screen.blit(lista_img_negro[lista[n].id],(lista[n]._x,lista[n]._y))   

def convertir_a_coord_tablero(pos):
    contador=0
    retorno=-1
    while contador<len(_coords_Tablero) and retorno == -1:
        if (pos[0] - _coords_Tablero[contador][0]<50) and (pos[1] - _coords_Tablero[contador][1]<50):
            retorno = contador
        contador += 1    
    return(_coords_Tablero[retorno])

def esta_Ocupada(pos,lista):
    contador=0
    retorno = False
    while contador < len(lista) and (not retorno):
        if lista[contador]._x == pos[0] and lista[contador]._y == pos[1]:
            retorno = True
        contador += 1
    return retorno

def obtenerTipo(posicion, lista):
    contador=0
    retorno = -1
    while contador < len(lista) and (retorno == -1):
        if lista[contador]._x == posicion[0] and lista[contador]._y == posicion[1]:
            retorno = lista[contador].id
        contador += 1
    return retorno
        
def _Mover_pieza(piece_origin,piece_destiny,lista):
    contador = 0
    while contador < len(lista):
        if lista[contador]._x == piece_origin[0] and lista[contador]._y==piece_origin[1]:
           lista[contador]._x=piece_destiny[0]
           lista[contador]._y=piece_destiny[1]
        contador += 1

def out_of_board(pos):
    return not((120 <= pos[0] <= 520) and (40 <= pos[1] <= 440))
    
def comprobarAtaque(piece_destiny,lista):
    contador = 0
    posicion = -1
    encontre = False
    while contador < len(lista) and (not encontre):
        if lista[contador]._x == piece_destiny[0] and lista[contador]._y==piece_destiny[1]:
           encontre = True
           posicion = contador
        contador += 1
    return posicion

def esJaque(pieza,lista):#A revisar!!!
#Recibe al rey y lista de piezas enemigas, si alguna lo puede atacar devuelve true
    contador =0
    pos_rey = pieza.get_pos()
    while contador < len(lista):
        org = lista[contador].get_pos()
        piece_tipo = lista[contador].get_id()
        piece_color =lista[contador].get_bn()
        if es_Mov_Valido(org,pos_rey,piece_tipo,piece_color,True):
            print("Entre")
            return True
        contador += 1
    
    return False

def actualizarCoord(resta_x,resta_y,origen):
    if resta_x == 0:
        if resta_y > 0:
            nuevaCoord =(origen[0],origen[1]+50) 
        elif resta_y < 0:
            nuevaCoord =(origen[0],origen[1]-50)
    elif resta_y == 0:
        if resta_x > 0:
            nuevaCoord =(origen[0]+50,origen[1]) 
        elif resta_x < 0:
            nuevaCoord =(origen[0]-50,origen[1])
    elif resta_x > 0:
        if resta_y > 0:
            nuevaCoord =(origen[0]+50,origen[1]+50) 
        elif resta_y < 0:
            nuevaCoord =(origen[0]+50,origen[1]-50)
    elif resta_x < 0:
        if resta_y > 0:
            nuevaCoord =(origen[0]-50,origen[1]+50) 
        elif resta_y < 0:
            nuevaCoord =(origen[0]-50,origen[1]-50)
    return nuevaCoord

def es_Mov_Valido(piece_origin,piece_destiny,pieza,turno,esAtaque):
#peon,torre,caballo,alfil,reina,rey
    if (pieza == 0 and (not esAtaque)):#peon
        if (turno == 0) and (piece_destiny[0]==piece_origin[0]) and ((piece_destiny[1] - piece_origin[1])== 50):
            return True
        if (turno == 1) and (piece_destiny[0]==piece_origin[0]) and ((piece_destiny[1] - piece_origin[1])== -50):
            return True
    if (pieza == 0 and esAtaque):#peon
        if (turno == 0) and abs(piece_destiny[0] - piece_origin[0]) == abs(piece_destiny[1] - piece_origin[1]) and ((piece_destiny[1] - piece_origin[1])== 50):
            return True
        if (turno == 1) and abs(piece_destiny[0] - piece_origin[0]) == abs(piece_destiny[1] - piece_origin[1]) and ((piece_destiny[1] - piece_origin[1])== -50):
            return True

    if (pieza == 1):#torre
        if (piece_destiny[0]==piece_origin[0])^((piece_destiny[1]==piece_origin[1])):
            return True
    if (pieza == 2):#caballo
        if (abs(piece_destiny[0]-piece_origin[0])==50 and abs(piece_destiny[1]-piece_origin[1])==100)^(abs(piece_destiny[0]-piece_origin[0])==100 and abs(piece_destiny[1]-piece_origin[1])==50):
            return True
    if (pieza == 3):#alfil
        if abs(piece_destiny[0] - piece_origin[0]) == abs(piece_destiny[1] - piece_origin[1]):
            return True
    if (pieza == 4):#reina
        if (piece_destiny[0]==piece_origin[0])^((piece_destiny[1]==piece_origin[1])):
            return True
        elif abs(piece_destiny[0] - piece_origin[0]) == abs(piece_destiny[1] - piece_origin[1]):
            return True
    if (pieza == 5):#rey
        if (abs(piece_destiny[0]-piece_origin[0])<=50) and (abs(piece_destiny[1]-piece_origin[1])<=50):
            return True
    return False

def tienePiezasAdelante(tipo,origen,destino,lista1,lista2):
    resta_x = destino[0]-origen[0]
    resta_y = destino[1]-origen[1]
    #nuevaCoord=origen
    if(-51 < resta_y < 51) and (-51 < resta_x < 51): 
        return False
    elif (tipo == 1 or tipo == 3 or tipo == 4):
        nuevaCoord = actualizarCoord(resta_x,resta_y,origen)
        while not(resta_y==0 and resta_x==0):
            if esta_Ocupada(nuevaCoord,lista1) or esta_Ocupada(nuevaCoord,lista2):
                return True
            nuevaCoord = actualizarCoord(resta_x,resta_y,origen)
            origen=nuevaCoord
            resta_x = destino[0]-origen[0]
            resta_y = destino[1]-origen[1]   
    return False

def procesarMovimiento(turno,origen,destino,lista1,lista2):
    retorno = turno
    deseleccionar = True
    piece_type = obtenerTipo(origen,lista1)
    pieza_atacada=comprobarAtaque(destino,lista2)
    if not(tienePiezasAdelante(piece_type,origen,destino,lista1,lista2)):
        if (pieza_atacada != -1) and es_Mov_Valido(origen,destino,piece_type,turno,True):
            lista2.pop(pieza_atacada)
            _Mover_pieza(origen,destino,lista1) 
            deseleccionar = False
            retorno=int(not retorno)
        elif not esta_Ocupada(destino,lista1) and not(esta_Ocupada(destino,lista2)):
            if es_Mov_Valido(origen,destino,piece_type,turno,False):
                _Mover_pieza(origen,destino,lista1) 
                deseleccionar = False
                retorno=int(not retorno)
    print("Negra en jaque:"+str(esJaque(lista2[len(lista2)-1],lista1)))
    return deseleccionar,retorno
    



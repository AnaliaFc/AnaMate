import pygame,random,sys,colors,board,pieces

def main():
    """ Función principal del juego. """
    pygame.init()
    # Establecemos el largo y alto de la pantalla [largo,alto]
    screen_size = [640, 480]
    screen = pygame.display.set_mode(screen_size)
    fuente = pygame.font.Font('Masanbol.ttf', 30)
    texto1 = fuente.render("AnaMate", 0, colors._BLUE)
    turno =0 #Blanco 0, Negro 1
    lista_J1 = []#Blanco
    lista_J2 = []#Negro
    board.crear_piezas(lista_J1,lista_J2)#Blancas, negras
    pygame.display.set_caption("AnaMate")
    done = False
    #Se usa para establecer cuan rápido se actualiza la pantalla
    clock = pygame.time.Clock()
    posM = (0,0)
    piece_type=-1
    piece_is_selected = False
    piece_origin = (0,0)
 
    #-------- Bucle principal del Programa -----------
    while not done:
         # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
       for evento in pygame.event.get():
           if evento.type == pygame.QUIT:
               print("El usuario se fue a la mierda")
               done = True
           if evento.type == pygame.MOUSEBUTTONUP:
                if(not board.out_of_board(pygame.mouse.get_pos())):
                    posM=board.convertir_a_coord_tablero(pygame.mouse.get_pos())
                if(not piece_is_selected)and (turno == 0):
                    piece_is_selected = board.esta_Ocupada(posM,lista_J1)
                    piece_origin=posM      
                elif(not piece_is_selected) and (turno == 1):   
                    piece_is_selected = board.esta_Ocupada(posM,lista_J2)
                    piece_origin=posM    
                elif piece_is_selected and (turno == 0):
                     piece_is_selected,turno = board.procesarMovimiento(turno,piece_origin,posM,lista_J1,lista_J2)
                elif piece_is_selected and (turno == 1):
                     piece_is_selected,turno = board.procesarMovimiento(turno,piece_origin,posM,lista_J2,lista_J1)
                        
           if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    piece_is_selected = False
                  
       # DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
       # Primero, fijamos en blanco el fondo de pantalla. No escribas nada encima de este comando, de otra forma se borrará
       screen.fill(colors._BLACK)
       board.dibujarTablero(screen)
       if(piece_is_selected):
            pygame.draw.rect(screen,colors._BOOK_BLUE, [piece_origin[0],piece_origin[1], 50, 50])
       board.dibujarPiezas(screen,lista_J1)
       board.dibujarPiezas(screen,lista_J2)
      
         
       screen.blit(texto1,(270,0))
       if turno == 0:
        texto2 = fuente.render("Juega Blanco",0,colors._WHITE)
        screen.blit(texto2,(0,0))
       if turno == 1:
        texto2 = fuente.render("Juega Negro",0,colors._WHITE) 
        screen.blit(texto2,(0,440))
           
        # Avanzamos y actualizamos la pantalla que ya hemos dibujado
       pygame.display.flip()
 
        # Limitamos a 60 fps
       clock.tick(60)
         
    # Cerrar la ventana y salir.
    # Si olvidas esto último, el programa se 'colgará' en la salida si lo llamamos desde el IDLE
    pygame.quit()
 
if __name__ == "__main__":
    main()
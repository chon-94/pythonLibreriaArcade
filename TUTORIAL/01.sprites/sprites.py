import arcade

# Constantes dimencion de la pantalla y nombre
ANCHO_PANTALLA = 1366
LARGO_PANTALLA = 768
TITULO_PANTALLA = "CHON"

# Constantes utilizadas para escalar nuestros sprites desde su tamaño original
ESCALA_PERSONAJE = 1
ESCALA_PAREDES = 0.5
ESCALA_CAJAS = 0.7

class MyGame(arcade.Window):# Esta es la clase de la aplicacion principal

    def __init__(self):# Llama a la clase principal y configure la ventana
        
        super().__init__(ANCHO_PANTALLA, LARGO_PANTALLA, TITULO_PANTALLA)# Sino se colocan las constantes se toman los valores por defecto

        # Estas son 'listas' realizan un seguimiento de nuestros sprites. 
        # Cada objeto debe estar en una lista.
        self.pared_lista = None
        self.caja_lista = None
        self.personaje_lista = None
        
        # Variable separada que contiene el sprite del jugador
        self.personaje_sprite = None

        arcade.set_background_color(arcade.csscolor.MIDNIGHT_BLUE) # Para darle color al fondo
        #arcade.set_background_color(arcade.color.DARK_SLATE_GRAY) # Para darle color al fondo

    def setup(self):# Configuracion del juego, si llamas a esta funcion se reinicia el juego 
        
        # Crear las listas de Sprite
        self.personaje_lista = arcade.SpriteList()
        self.caja_lista = arcade.SpriteList(use_spatial_hash=True)
        self.pared_lista = arcade.SpriteList(use_spatial_hash=True)

        # Configura al jugador, colocándolo específicamente en estas coordenadas.
        imagen_personaje = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png" # Variable del personaje
        self.personaje_sprite = arcade.Sprite(imagen_personaje, ESCALA_PERSONAJE)
        self.personaje_sprite.center_x = 40  # Posision en el eje x    
        self.personaje_sprite.center_y = 128 # Posision en el eje y
        self.personaje_lista.append(self.personaje_sprite) # Agregamos el sprite

        # Crear el suelo
        for x in range(0, 1350, 64): # range(Inicio,Fin,Separacion)
            pared = arcade.Sprite(":resources:images/tiles/grassMid.png", ESCALA_PAREDES) # Variable de la pared
            pared.center_x = x  # Posision en el eje x
            pared.center_y = 32 # Posision en el eje y
            self.pared_lista.append(pared) # Agregamos la pared

        # Crear obstaculos
        cordenada_listas_cajas = [[256, 105], [456, 105], [656, 105], [856, 105], [1056, 105]]# Lista de coordenadas para sprites
        for cordenada in cordenada_listas_cajas:#Añadir los obstacuo en el suelo
            caja = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", ESCALA_CAJAS )# Variable de la caja
            caja.position = cordenada # Decimos que la posision de la caja sera  el de la cordenada 
            self.caja_lista.append(caja) # Agregamos la caja

    def on_draw(self):# Renderizado de pantalla

        self.clear()# El código para dibujar la pantalla va aquí

        # Dibujar nuestros sprites
        self.caja_lista.draw()
        self.pared_lista.draw()
        self.personaje_lista.draw()

def main():# Funcion principal
    ventana = MyGame()
    ventana.setup()
    arcade.run()

if __name__ == "__main__":
    main()
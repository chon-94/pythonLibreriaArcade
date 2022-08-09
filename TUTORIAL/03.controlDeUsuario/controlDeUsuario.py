import arcade

# Constantes dimencion de la pantalla y nombre
ANCHO_PANTALLA = 1366
LARGO_PANTALLA = 768
TITULO_PANTALLA = "CHON"

# Constantes utilizadas para escalar nuestros sprites desde su tamaño original
ESCALA_PERSONAJE = 1
ESCALA_PAREDES = 0.5
ESCALA_CAJAS = 0.7

# Velocidad de movimiento del jugador, en píxeles por fotograma
VELOCIDAD_DEL_PERSONAJE = 5

class MyGame(arcade.Window):# Esta es la clase de la aplicacion principal

    def __init__(self):# Llama a la clase principal y configure la ventana
        
        super().__init__(ANCHO_PANTALLA, LARGO_PANTALLA, TITULO_PANTALLA)# Sino se colocan las constantes se toman los valores por defecto

        # Estas son 'listas' realizan un seguimiento de nuestros sprites. 
        # Cada objeto debe estar en una lista.
        #self.pared_lista = None
        #self.caja_lista = None
        #self.personaje_lista = None

        self.escena_0 = None # Nuestro objeto de escena
        self.escena_1 = None # Nuestro objeto de escena

        # Variable separada que contiene el sprite del jugador
        self.personaje_sprite = None

        # Motor de físicas
        self.motor_de_física_0 = None
        self.motor_de_física_1 = None

        arcade.set_background_color(arcade.csscolor.MIDNIGHT_BLUE) # Para darle color al fondo
        #arcade.set_background_color(arcade.color.DARK_SLATE_GRAY) # Para darle color al fondo

    def setup(self):# Configuracion del juego, si llamas a esta funcion se reinicia el juego 
        
        # iniciar escena
        self.escena_0 = arcade.Scene()
        self.escena_1 = arcade.Scene()

        # Create the Sprite lists
        #self.escena.add_sprite_list("personaje")
        #self.escena.add_sprite_list("caja", use_spatial_hash=True)
        #self.escena.add_sprite_list("pared", use_spatial_hash=True)

        # Crear las listas de Sprite
        #self.personaje_lista = arcade.SpriteList()
        #self.caja_lista = arcade.SpriteList(use_spatial_hash=True)
        #self.pared_lista = arcade.SpriteList(use_spatial_hash=True)

        # Configura al jugador, colocándolo específicamente en estas coordenadas.
        imagen_personaje = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png" # Variable del personaje
        self.personaje_sprite = arcade.Sprite(imagen_personaje, ESCALA_PERSONAJE)
        self.personaje_sprite.center_x = 40  # Posision en el eje x    
        self.personaje_sprite.center_y = 128 # Posision en el eje y
        #self.personaje_lista.append(self.personaje_sprite) # Agregamos el sprite
        self.escena_0.add_sprite("personaje", self.personaje_sprite)

        # Crear el suelo
        for x in range(0, 1350, 64): # range(Inicio,Fin,Separacion)
            pared = arcade.Sprite(":resources:images/tiles/grassMid.png", ESCALA_PAREDES) # Variable de la pared
            pared.center_x = x  # Posision en el eje x
            pared.center_y = 32 # Posision en el eje y
            #self.pared_lista.append(pared) # Agregamos la pared
            self.escena_0.add_sprite("pared", pared)

        # Crear obstaculos
        cordenada_listas_cajas = [[256, 105], [456, 105], [656, 105], [856, 105], [1056, 105]]# Lista de coordenadas para sprites
        for cordenada in cordenada_listas_cajas:#Añadir los obstacuo en el suelo
            caja = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", ESCALA_CAJAS )# Variable de la caja
            caja.position = cordenada # Decimos que la posision de la caja sera  el de la cordenada 
            #self.caja_lista.append(caja) # Agregamos la caja
            self.escena_1.add_sprite("caja", caja)

        # Crear el 'motor de física'
        self.motor_de_física_0 = arcade.PhysicsEngineSimple(self.personaje_sprite, self.escena_0.get_sprite_list("pared"))
        self.motor_de_física_1 = arcade.PhysicsEngineSimple(self.personaje_sprite, self.escena_1.get_sprite_list("caja"))

    def on_draw(self):# Renderizado de pantalla

        self.clear()# El código para dibujar la pantalla va aquí
        # Dibujar nuestros sprites
        #self.caja_lista.draw()
        #self.pared_lista.draw()
        #self.personaje_lista.draw()
        
        # Dibuja nuestra Escena
        self.escena_0.draw()
        self.escena_1.draw()

    def on_key_press(self, key, modifiers):# Cuando presionamos una tecla

        if key == arcade.key.UP or key == arcade.key.W:
            self.personaje_sprite.change_y = VELOCIDAD_DEL_PERSONAJE
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.personaje_sprite.change_y = -VELOCIDAD_DEL_PERSONAJE
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.personaje_sprite.change_x = -VELOCIDAD_DEL_PERSONAJE
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.personaje_sprite.change_x = VELOCIDAD_DEL_PERSONAJE

    def on_key_release(self, key, modifiers):# Cuando soltamos la tecla presionada

        if key == arcade.key.UP or key == arcade.key.W:
            self.personaje_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.personaje_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.personaje_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.personaje_sprite.change_x = 0

    def on_update(self, delta_time):# Movimiento y lógica de juego.

        # Mueve al jugador con el motor de física.
        self.motor_de_física_0.update()
        self.motor_de_física_1.update()

def main():# Funcion principal
    ventana = MyGame()
    ventana.setup()
    arcade.run()

if __name__ == "__main__":
    main()
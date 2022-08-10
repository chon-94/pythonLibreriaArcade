from ast import And
import arcade

# Constantes dimencion de la pantalla y nombre
ANCHO_PANTALLA = 1366
LARGO_PANTALLA = 768
TITULO_PANTALLA = "CHON"

# Constantes utilizadas para escalar nuestros sprites desde su tamaño original
ESCALA_PERSONAJE = 1
ESCALA_PAREDES = 0.5
ESCALA_CAJAS = 0.35
ESCALA_MONEDAS = 0.5
ESCALA_DIAMANTES = 0.5


# Velocidad de movimiento del jugador, en píxeles por fotograma
VELOCIDAD_DEL_PERSONAJE = 5
GRAVEDAD = 1.5
VELOCIDAD_DE_SALTO = 25

class MyGame(arcade.Window):# Esta es la clase de la aplicacion principal

    def __init__(self):# Llama a la clase principal y configure la ventana
        
        super().__init__(ANCHO_PANTALLA, LARGO_PANTALLA, TITULO_PANTALLA)# Sino se colocan las constantes se toman los valores por defecto

        # Estas son 'listas' realizan un seguimiento de nuestros sprites. 
        # Cada objeto debe estar en una lista.
        #self.pared_lista = None
        #self.caja_lista = None
        #self.personaje_lista = None

        self.escena = None # Nuestro objeto de escena

        # Variable separada que contiene el sprite del jugador
        self.personaje_sprite = None

        # Motor de físicas
        self.motor_de_física = None

        # Esta cámara se usa para desplazar la pantalla
        self.camara = None

        # Load sounds
        self.coger_moneda_sonido = arcade.load_sound(":resources:sounds/coin1.wav")
        self.coger_moneda_diamante = arcade.load_sound(":resources:sounds/coin5.wav")
        self.salto_sonido = arcade.load_sound(":resources:sounds/jump1.wav")

        arcade.set_background_color(arcade.csscolor.MIDNIGHT_BLUE) # Para darle color al fondo
        #arcade.set_background_color(arcade.color.DARK_SLATE_GRAY) # Para darle color al fondo

    def setup(self):# Configuracion del juego, si llamas a esta funcion se reinicia el juego 
        
        # configurar la cámara
        self.camara = arcade.Camera(self.width, self.height)

        # iniciar escena
        self.escena = arcade.Scene()

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
        self.escena.add_sprite("personaje", self.personaje_sprite)

# SUELOS
        # Crear el suelo
        for x in range(0, 1665, 64): # range(Inicio,Fin,Separacion)
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", ESCALA_PAREDES) # Variable de la pared
            wall.center_x = x  # Posision en el eje x
            wall.center_y = 32 # Posision en el eje y
            #self.pared_lista.append(pared) # Agregamos la pared
            self.escena.add_sprite("walls", wall)
        for x in range(2000,3000,64): # range(Inicio,Fin,Separacion)
            wall = arcade.Sprite(":resources:images/tiles/planetMid.png", ESCALA_PAREDES) # Variable de la pared
            wall.center_x = x  # Posision en el eje x
            wall.center_y = 275 # Posision en el eje y
            #self.pared_lista.append(pared) # Agregamos la pared
            self.escena.add_sprite("walls", wall)

#OBSTACULOS
        # Crear obstaculos
        cordenada_listas_cajas = [[256,86], [356,275] ,[456,86], [556,275] ,[656,86], [756,275] ,[856,86], [956,275] ,[1056,86], [1156,275] ,[1256,86], [1356,275] ,[1456,86], [1556,275] ,[1656,86], [1826,175] ]# Lista de coordenadas para sprites
        for cordenada in cordenada_listas_cajas :#Añadir los obstacuo en el suelo
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", ESCALA_CAJAS )# Variable de la caja
            wall.position = cordenada # Decimos que la posision de la caja sera  el de la cordenada 
            #self.caja_lista.append(caja) # Agregamos la caja
            self.escena.add_sprite("walls", wall)

# COLECCIONABLES
        # Crear monedas
        cordenada_listas_monedas = [[256,175],[456,175],[656,175],[856,175],[1056,175],[1256,175],[1456,175],[1656,175]]# Lista de coordenadas para sprites
        for cordenada in cordenada_listas_monedas :#Añadir los obstacuo en el suelo
            coin = arcade.Sprite(":resources:images/items/coinGold.png", ESCALA_MONEDAS)# Variable de la caja
            coin.position = cordenada # Decimos que la posision de la caja sera  el de la cordenada 
            #self.caja_lista.append(caja) # Agregamos la caja
            self.escena.add_sprite("Coins", coin)
        # Crear diamantes
        cordenada_listas_diamantes = [ [356,375] , [556,375] , [756,375] , [956,375] , [1156,375] , [1356,375] , [1556,375] ]# Lista de coordenadas para sprites
        for cordenada in cordenada_listas_diamantes :#Añadir los obstacuo en el suelo
            gema = arcade.Sprite(":resources:images/items/gemBlue.png", ESCALA_DIAMANTES)# Variable de la caja
            gema.position = cordenada # Decimos que la posision de la caja sera  el de la cordenada 
            #self.caja_lista.append(caja) # Agregamos la caja
            self.escena.add_sprite("Gemas", gema)

        #for x in range(128, 3250, 286): # range(Inicio,Fin,Separacion)
            #coin = arcade.Sprite(":resources:images/items/coinGold.png", ESCALA_MONEDAS)
            #coin.center_x = x
            #coin.center_y = 96
            #self.escena.add_sprite("Coins", coin)

        # Crear el 'motor de física'
        #self.motor_de_física_0 = arcade.PhysicsEngineSimple(self.personaje_sprite, self.escena_0.get_sprite_list("pared"))
        #self.motor_de_física_1 = arcade.PhysicsEngineSimple(self.personaje_sprite, self.escena_1.get_sprite_list("caja"))
        #self.motor_de_física = arcade.PhysicsEngineSimple(self.personaje_sprite, self.escena.get_sprite_list("pared"))

        self.motor_de_física = arcade.PhysicsEnginePlatformer(self.personaje_sprite, gravity_constant=GRAVEDAD, walls=self.escena["walls"])
    
    def on_draw(self):# Renderizado de pantalla

        self.clear()# El código para dibujar la pantalla va aquí
        # Dibujar nuestros sprites
        #self.caja_lista.draw()
        #self.pared_lista.draw()
        #self.personaje_lista.draw()
        
        # Activar la camara
        self.camara.use()

        # Dibuja nuestra Escena
        self.escena.draw()

    def on_key_press(self, key, modifiers):# Cuando presionamos una tecla

        if key == arcade.key.UP or key == arcade.key.W:
            if self.motor_de_física.can_jump():
                self.personaje_sprite.change_y = VELOCIDAD_DE_SALTO
                arcade.play_sound(self.salto_sonido)

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

    def center_camera_to_player(self):
        screen_center_x = self.personaje_sprite.center_x - (self.camara.viewport_width / 2)
        screen_center_y = self.personaje_sprite.center_y - (self.camara.viewport_height / 2)

        # No permita que la cámara viaje más allá de 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camara.move_to(player_centered)

    def on_update(self, delta_time):# Movimiento y lógica de juego.

        # Mueve al jugador con el motor de física.
        self.motor_de_física.update()

        # pegamos los coleccionables 
        coin_hit_list = arcade.check_for_collision_with_list(self.personaje_sprite, self.escena["Coins"])
        gema_hit_list = arcade.check_for_collision_with_list(self.personaje_sprite, self.escena["Gemas"])

        # Recorra cada moneda que golpeamos (si corresponde) y retírela
        for coin in coin_hit_list:
            # quitar la moneda
            coin.remove_from_sprite_lists()
            # reproducir un sonido
            arcade.play_sound(self.coger_moneda_sonido)

#        self.coger_moneda_diamante = arcade.load_sound(":resources:sounds/coin5.wav")

        for gema in gema_hit_list:
            # quitar la moneda
            gema.remove_from_sprite_lists()
            # reproducir un sonido
            arcade.play_sound(self.coger_moneda_diamante)

        # Coloca la cámara
        self.center_camera_to_player()

def main():# Funcion principal
    ventana = MyGame()
    ventana.setup()
    arcade.run()

if __name__ == "__main__":
    main()
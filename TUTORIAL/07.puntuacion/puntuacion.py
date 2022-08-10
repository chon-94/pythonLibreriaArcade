import arcade

# Constantes dimencion de la pantalla y nombre
ANCHO_PANTALLA = 1360
LARGO_PANTALLA = 745
TITULO_PANTALLA = "CHON"

# Constantes para escalar
ESCALA_PERSONAJE = 1
ESCALA_PAREDES = 0.5
ESCALA_CAJAS = 0.35
ESCALA_MONEDAS = 0.5
ESCALA_DIAMANTES = 0.5

# Velocidad de fisicas
VELOCIDAD_DEL_PERSONAJE = 5
GRAVEDAD = 1.5
VELOCIDAD_DE_SALTO = 25

class MyGame(arcade.Window):# Clase principal

    def __init__(self):# Llama a la clase principal y configure la ventana
        
        super().__init__(ANCHO_PANTALLA, LARGO_PANTALLA, TITULO_PANTALLA)# Sino se colocan las constantes se toman los valores por defecto

        # Variable de la Escena
        self.escena = None 

        # Variable del Jugador
        self.personaje_sprite = None

        # Variable del Motor de físicas
        self.motor_de_física = None

        # Variable de la Cámara
        self.camara = None

        # Variable de HUD
        self.hud = None

        # Variable de Puntuacion
        self.monedas_p = 0
        self.diamantes_p = 0

        # Variable de Sonidos
        self.coger_moneda_sonido = arcade.load_sound(":resources:sounds/coin1.wav")
        self.coger_moneda_diamante = arcade.load_sound(":resources:sounds/coin5.wav")
        self.salto_sonido = arcade.load_sound(":resources:sounds/jump1.wav")

        arcade.set_background_color(arcade.csscolor.LIGHT_SEA_GREEN) # Para darle color al fondo
        #arcade.set_background_color(arcade.color.DARK_SLATE_GRAY) # Para darle color al fondo

    def setup(self):# Configuracion del juego, si llamas a esta funcion se reinicia el juego 
        
        # configurar cámara
        self.camara = arcade.Camera(self.width, self.height)

        # iniciar escena
        self.escena = arcade.Scene()

        # Configurar HUD
        self.hud = arcade.Camera(self.width, self.height)

        # Registro de puntuación
        self.monedas_p = 0
        self.diamantes_p = 0

        # Configuracion del jugador
        imagen_personaje = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png" # Variable del personaje
        self.personaje_sprite = arcade.Sprite(imagen_personaje, ESCALA_PERSONAJE)
        self.personaje_sprite.center_x = 40  # Posision en el eje x    
        self.personaje_sprite.center_y = 128 # Posision en el eje y
        self.escena.add_sprite("personaje", self.personaje_sprite)

# SUELOS
        # Crear el suelo
        for x in range(0, 1665, 64): # range(Inicio,Fin,Separacion)
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", ESCALA_PAREDES) # Variable del suelo
            wall.center_x = x  # Posision en el eje x
            wall.center_y = 32 # Posision en el eje y
            self.escena.add_sprite("walls", wall)
        for x in range(2000,3000,64): # range(Inicio,Fin,Separacion)
            wall = arcade.Sprite(":resources:images/tiles/planetMid.png", ESCALA_PAREDES) # Variable del suelo
            wall.center_x = x  # Posision en el eje x
            wall.center_y = 275 # Posision en el eje y
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
        cordenada_listas_monedas = [[256,175],[456,175],[656,175],[856,175],[1056,175],[1256,175],[1456,175],[1656,175] , [1826,215] , [1826,285] ]# Lista de coordenadas para sprites
        for cordenada in cordenada_listas_monedas :#Añadir los obstacuo en el suelo
            coin = arcade.Sprite(":resources:images/items/coinGold.png", ESCALA_MONEDAS)# Variable de la caja
            coin.position = cordenada # Decimos que la posision de la caja sera  el de la cordenada 
            #self.caja_lista.append(caja) # Agregamos la caja
            self.escena.add_sprite("Coins", coin)
        # Crear diamantes
        cordenada_listas_diamantes = [ [356,375] , [556,375] , [756,375] , [956,375] , [1156,375] , [1356,375] , [1556,375] , [1826,250] , [1826,320]  ]# Lista de coordenadas para sprites
        for cordenada in cordenada_listas_diamantes :#Añadir los obstacuo en el suelo
            diamantes = arcade.Sprite(":resources:images/items/gemBlue.png", ESCALA_DIAMANTES)# Variable de la caja
            diamantes.position = cordenada # Decimos que la posision de la caja sera  el de la cordenada 
            #self.caja_lista.append(caja) # Agregamos la caja
            self.escena.add_sprite("Gemas", diamantes)

        self.motor_de_física = arcade.PhysicsEnginePlatformer(self.personaje_sprite, gravity_constant=GRAVEDAD, walls=self.escena["walls"])

# Renderizado de pantalla   
    def on_draw(self):

        self.clear()# El código para dibujar la pantalla va aquí
        
        # Activar la camara
        self.camara.use()

        # Dibuja nuestra Escena
        self.escena.draw()

        # Activate the GUI camera before drawing GUI elements
        self.hud.use()

# PUNTUACION EN LA PANTALLA
        # Monedas
        monedaText = f"Monedas: {self.monedas_p}"
        arcade.draw_text(monedaText,5,725,arcade.csscolor.YELLOW,10,)
        # Diamantes
        diamanteText = f"Diamantes: {self.diamantes_p}"
        arcade.draw_text(diamanteText,100,725,arcade.csscolor.TURQUOISE,10,)

# CONTROLES
    # Cuando presionamos una tecla
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.motor_de_física.can_jump():# Salto
                self.personaje_sprite.change_y = VELOCIDAD_DE_SALTO
                arcade.play_sound(self.salto_sonido)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.personaje_sprite.change_y = -VELOCIDAD_DEL_PERSONAJE
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.personaje_sprite.change_x = -VELOCIDAD_DEL_PERSONAJE
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.personaje_sprite.change_x = VELOCIDAD_DEL_PERSONAJE
    # Cuando soltamos la tecla presionada
    def on_key_release(self, key, modifiers):
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

        #la cámara no viaje más allá de 0
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

# Configuracion de coleccionables
        # Monedas
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()# quitar la moneda
            arcade.play_sound(self.coger_moneda_sonido)# reproducir un sonido
            self.monedas_p += 2
        # Diamantes
        for diamantes in gema_hit_list:
            diamantes.remove_from_sprite_lists()# quitar la moneda
            arcade.play_sound(self.coger_moneda_diamante)# reproducir un sonido
            self.diamantes_p += 5
        
        self.center_camera_to_player()# Coloca la cámara

def main():# Funcion principal
    ventana = MyGame()
    ventana.setup()
    arcade.run()

if __name__ == "__main__":
    main()
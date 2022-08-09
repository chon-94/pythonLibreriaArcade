# Escena

A continuación, agregaremos una escena a nuestro juego. Una escena es una herramienta para administrar una serie de spritelistas diferentes asignando a cada uno un nombre y manteniendo un orden de sorteo.

Las spritelistas se pueden dibujar directamente como vimos en el paso 2 de este tutorial, pero una escena puede ser útil para manejar muchas listas diferentes a la vez y poder dibujarlas todas con una sola llamada a la escena.

Para comenzar, eliminamos nuestras listas de sprites de la función __init__ y las reemplazaremos con un objeto de escena.

    def __init__(self):

        # Llama a la clase principal y configure la ventana
        super().__init__(ANCHO_PANTALLA, LARGO_PANTALLA, TITULO_PANTALLA)

        # Nuestro objeto de escena
        self.escena = None

        # Variable separada que contiene el sprite del jugador.
        self.personaje_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

A continuación, inicializaremos el objeto de escena en la función de configuración y luego le agregaremos SpriteLists en lugar de crear nuevos objetos SpriteList directamente.

Luego, en lugar de agregar los Sprites a SpriteLists directamente, podemos agregarlos a la escena y especificar por nombre a qué SpriteList queremos agregarlos.

    def setup(self):
        """Configura el juego aquí. Llama a esta función para reiniciar el juego."""

        # Inicializar la escena
        self.escena = arcade.Scene()

        # Crear las listas de Sprite
        self.escena.add_sprite_list("personaje")
        self.escena.add_sprite_list("caja", use_spatial_hash=True)
        self.escena.add_sprite_list("pared", use_spatial_hash=True)

        # Configura al jugador, colocándolo específicamente en estas coordenadas.
        imagen_personaje = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.personaje_sprite = arcade.Sprite(imagen_personaje, CHARACTER_SCALING)
        self.personaje_sprite.center_x = 64
        self.personaje_sprite.center_y = 128
        self.escena.add_sprite("Player", self.personaje_sprite)

        # Crea el suelo
        # Esto muestra el uso de un bucle para colocar varios sprites horizontalmente.
        for x in range(0, 1250, 64):
            pared = arcade.Sprite(":resources:images/tiles/grassMid.png", ESCALA_PAREDES)
            pared.center_x = x
            pared.center_y = 32
            self.escena.add_sprite("pared", pared)

        # colocar algunas cajas en el suelo.
        # Esto muestra el uso de una lista de coordenadas para colocar sprites
        cordenada_listas_cajas = [[512, 96], [256, 96], [768, 96]]
        for cordenada in cordenada_listas_cajas:
            # Add a crate on the ground
            caja = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", ESCALA_CAJAS)
            caja.position = cordenada
            self.escena.add_sprite("cajas", caja)

Por último, en nuestra función on_draw podemos dibujar la escena.

    def on_draw(self):
        """Representar la pantalla."""

        # Borrar la pantalla al color de fondo
        self.clear()

        # Dibujar nuestra escena
        self.escena.draw()
# Puntuacion

Ahora que podemos recolectar monedas y obtener puntos, necesitamos una forma de mostrar el puntaje en la pantalla.

Este proceso es un poco más complejo que simplemente dibujar un texto en una ubicación X e Y. Para dibujar correctamente el texto o cualquier elemento de la GUI, necesitamos usar una cámara separada de la que usamos para dibujar el resto de nuestra escena.

Esto se debe a que nos estamos desplazando por la cámara principal del juego, pero queremos que los elementos de nuestra GUI permanezcan quietos. Usar una segunda cámara nos permite hacer esto.

Como ejemplo, si no usáramos una segunda cámara y, en cambio, dibujáramos en la misma cámara que nuestra escena. Necesitaríamos compensar la posición en la que dibujamos nuestro texto por la posición de la cámara. Esto podría ser más fácil si solo está mostrando una cosa, pero si tiene muchos elementos GUI, esto podría salirse de control.

Primero comience creando la nueva cámara GUI y las variables de puntuación en la función __init__.

    # A Camera that can be used to draw GUI elements
    self.gui_camera = None

    # Keep track of the score
    self.score = 0

Luego podemos inicializarlos en la función de configuración. Restablecemos el puntaje a 0 aquí porque esta función está destinada a restablecer completamente el juego a su estado inicial.

    # Set up the GUI Camera
    self.gui_camera = arcade.Camera(self.width, self.height)

    # Keep track of the score
    self.score = 0

Luego, en nuestra función on_draw, primero podemos dibujar nuestra escena como de costumbre, y luego cambiar a la cámara GUI, y finalmente dibujar nuestro texto.

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements

        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport

        score_text = f"Score: {self.score}"

        arcade.draw_text(score_text,10,10,arcade.csscolor.WHITE,18,)

Por último, en la función on_update solo necesitamos actualizar la puntuación cuando un jugador recoge una moneda:

    # Loop through each coin we hit (if any) and remove it
    for coin in coin_hit_list:
        # Remove the coin
        coin.remove_from_sprite_lists()
        # Play a sound
        arcade.play_sound(self.collect_coin_sound)

        # Add one to the score

        self.score += 1

        
# control de usuario
Ahora necesitamos poder hacer que el personaje se mueva.

Primero, en la parte superior del programa, agregue una constante que controla cuántos píxeles por actualización viaja nuestro personaje:

    # Velocidad de movimiento del jugador, en píxeles por fotograma
    VELOCIDAD_DEL _PERSONAJE = 5

Luego, al final de nuestro método de configuración, necesitamos crear un motor de física que mueva a nuestro jugador y evite que atraviese las paredes como los fantasmas. 
La clase PhysicsEngineSimple toma dos parámetros: 
el sprite en movimiento y una lista de sprites por los que el sprite en movimiento no puede moverse.

    # Crea fisicas
    self.physics_engine = arcade.PhysicsEngineSimple(self.personaje_sprite, self.escena.get_sprite_list("pared "))

Cada sprite tiene atributos Center_X y Center_Y. Cambiar estos cambiará la ubicación del sprite. 
(También hay atributos para la parte superior, inferior, izquierda, derecha y ángulo que moverán el sprite).

Cada sprite tiene variables Change_X y Change_Y. Estos se pueden usar para mantener la velocidad con la que se mueve el sprite. Los ajustaremos en función de la clave que golpea el usuario. Si el usuario presenta la tecla de flecha correcta, queremos un valor positivo para Change_x. Si el valor es 5, moverá 5 píxeles por cuadro.

En este caso, cuando el usuario presiona una tecla, cambiaremos los sprites cambian x e y. El motor de física lo verá y moverá al jugador a menos que golpee una pared.

    def on_key_press(self, key, modifiers):
        """cada vez que se presiona una tecla."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.personaje_sprite.change_y = VELOCIDAD_DEL _PERSONAJE
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.personaje_sprite.change_y = -VELOCIDAD_DEL _PERSONAJE
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.personaje_sprite.change_x = -VELOCIDAD_DEL _PERSONAJE
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.personaje_sprite.change_x = VELOCIDAD_DEL _PERSONAJE

Cuando soltamo la tecla, volveremos a poner nuestra velocidad a cero.

    def on_key_release(self, key, modifiers):
        """cuando el usuario suelta una tecla."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.personaje_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.personaje_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.personaje_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.personaje_sprite.change_x = 0

Nuestro método on_update se llama unas 60 veces por segundo. Le pediremos al motor de física que mueva a nuestro jugador en función de su cambio_x y cambio_y.

Bueno yo lo que hice fue crear una escena y una fisica por cada objeto que hay... es decir para las cajas y para la pared


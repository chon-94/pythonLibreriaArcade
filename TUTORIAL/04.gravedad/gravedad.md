# Gravedad

El ejemplo anterior es excelente para vista de arriba hacia abajo, pero ¿y si es una vista lateral con saltos como nuestro juego de plataformas? Necesitamos agregar gravedad. Primero, definamos una constante para representar la aceleración de la gravedad y otra para la velocidad de un salto.

    GRAVITY = 1
    PLAYER_JUMP_SPEED = 20

Al final del método de configuración, cambie el motor de física a PhysicsEnginePlatformer e incluya la gravedad como parámetro.

    # Create the 'physics engine'
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, gravity_constant=GRAVITY, walls=selfscene["Walls"])

Estamos enviando nuestra SpriteList para las cosas con las que el jugador debe chocar al parámetro de paredes del motor de física. Como veremos en capítulos posteriores, el motor de física del juego de plataformas tiene un parámetro de plataformas y paredes. La diferencia entre estos es muy importante. Las listas de sprites estáticas que no se mueven siempre deben enviarse al parámetro de paredes, y los sprites en movimiento deben enviarse al parámetro de plataformas. Asegurarse de hacer esto tendrá beneficios extremos para el rendimiento.

Agregar sprites estáticos a través del parámetro de plataformas es aproximadamente una operación O(n), lo que significa que el rendimiento empeorará linealmente a medida que agregue más sprites. Si agrega sus sprites estáticos a través del parámetro de paredes, entonces es casi O (1) y esencialmente no hay diferencia entre, por ejemplo, 100 y 50,000 sprites que no se mueven.

También vemos aquí una nueva sintaxis relacionada con nuestro objeto Escena. Puede acceder a la escena como lo haría con un diccionario de Python para obtener sus listas de SpriteLists. Hay varias formas de acceder a SpriteLists dentro de una escena, pero esta es la más fácil y directa. Alternativamente, podría usar scene.get_sprite_list ('Mi capa').

Luego, modifique los controladores de eventos key down y key up. Eliminaremos las declaraciones arriba/abajo que teníamos antes, y haremos que 'ARRIBA' salte cuando se presione.

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""


        if key == arcade.key.UP or key == arcade.key.W:

            if self.physics_engine.can_jump():

                self.player_sprite.change_y = PLAYER_JUMP_SPEED

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

al final he tenido que cambiar muchas cosas ... te acuerdas que antes tenias pared y caja pues bueno con esos 2 me da error y ese error dice que debo de usar wall porque si no lo uso hasta este punto  tendremos problemas
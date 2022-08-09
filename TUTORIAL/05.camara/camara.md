# Camara

Podemos hacer que nuestra ventana sea una pequeña ventana hacia un mundo mucho más grande al agregarle una cámara.
Primero necesitamos crear una nueva variable en nuestro método __init__:

    # Esta cámara se puede usar para desplazar la pantalla
    self.camera = None

A continuación podemos inicializar la cámara en la función de configuración:

    # configurar la cámara
    self.camera = arcade.Camera(self.width, self.height)

Luego para usar nuestra cámara al dibujar, podemos activarla en nuestra función on_draw:

    # Activa nuestra Cámara
    self.camera.use()

Ahora, en este punto, todo debería funcionar igual, pero la cámara puede hacer mucho más que esto. Podemos usar la función de movimiento de la cámara para desplazarla a una posición diferente. Podemos usar esta funcionalidad para mantener la cámara centrada en el jugador:

Podemos crear una función para calcular las coordenadas del centro de nuestro reproductor en relación con la pantalla y luego mover la cámara hacia ellas. Luego podemos llamar a esa función en on_update para moverla. La nueva posición se tendrá en cuenta durante la función de uso en on_draw

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)
        
        # No permitir que la cámara viaje más allá de 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)


    def on_update(self, delta_time):
        """Movimiento y lógica de juego"""

        # Muever al jugador con el motor de física.
        self.physics_engine.update()

        # Colocar la cámara
        self.center_camera_to_player()
# Coleccionables y sonido

# Monedas

A continuación, agregaremos algunas monedas que el jugador puede recoger. 
También agregaremos un sonido para que se reproduzca cuando lo recojan, así como un sonido para cuando salten.

Primero necesitamos agregar nuestras monedas a la escena. Comencemos agregando una constante en la parte superior de nuestra aplicación para la escala del sprite de monedas, similar a nuestra TILE_SCALING.

    COIN_SCALING = 0.5

A continuación, en nuestra función de configuración, podemos crear nuestras monedas usando un bucle for como lo hemos hecho anteriormente para el suelo, y luego agregarlas a la escena.

    # Use a loop to place some coins for our character to pick up
    for x in range(128, 1250, 256):
        coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
        coin.center_x = x
        coin.center_y = 96
        self.scene.add_sprite("Coins", coin)

# Sonido

Ahora podemos cargar nuestros sonidos para recoger la moneda y saltar. 
Más adelante usaremos estas variables para reproducir los sonidos cuando sucedan eventos específicos. Agregue lo siguiente a la función __init__ para cargar los sonidos:

    # Load sounds
    self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
    self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

Luego podemos reproducir nuestro sonido de salto cuando el jugador salta, agregándolo a la función on_key_press:

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED

                arcade.play_sound(self.jump_sound)

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

# Colision

Por último, necesitamos averiguar si el jugador golpeó una moneda. 
Podemos hacer esto en nuestra función on_update usando la función arcade.check_for_collision_with_list. 
Podemos pasar el sprite del jugador, junto con una SpriteList que contiene las monedas. La función devolverá una lista de las monedas con las que el jugador está chocando actualmente. 
Si no hay monedas en contacto, la lista estará vacía.

Entonces podemos usar la función Sprite.remove_from_sprite_lists que eliminará un sprite dado de cualquier SpriteLists al que pertenezca, eliminándolo efectivamente del juego.

Agregue lo siguiente a la función on_update para agregar detección de colisión y reproducir un sonido cuando el jugador toma una moneda.

    # See if we hit any coins
    coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["Coins"])

    # Loop through each coin we hit (if any) and remove it
    for coin in coin_hit_list:
        # Remove the coin
        coin.remove_from_sprite_lists()
        # Play a sound
        arcade.play_sound(self.collect_coin_sound)

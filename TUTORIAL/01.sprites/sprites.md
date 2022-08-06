# Sprites

Nuestro siguiente paso es agregar algunos sprites, que son gráficos que podemos ver e interactuar en la pantalla.


**tenemos un método __init__ y una setup :**

* El __init__ es el encargado de crear las variables. Estas se establecen en valores como 0 o nulo. 
* La setup crea las instancias del objeto, como los sprites gráficos.

**¿Por qué tener dos métodos por qué no hacerlo todo en __init__?**

* Con 2 métodos de setup, podemos agregar fácilmente la funcionalidad reiniciar el juego.
* Podemos expandir nuestro juego con diferentes niveles y tener funciones como setup_level_1 y setup_level_2.

# Sprites List

Los sprites se gestionan en listas. La clase SpriteList optimiza el dibujo, el movimiento y la detección de colisiones.

Estamos usando tres grupos lógicos en nuestro juego. Una player_list para el jugador. Una wall_list para los muros por los que no podemos movernos.

    self.player_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList(use_spatial_hash=True)

Las listas de sprites tienen una opción para usar algo llamado 'hashing espacial'. Esto acelera el tiempo que se tarda en encontrar colisiones, pero aumenta el tiempo que se tarda en mover un sprite. Ya que no se espera que la mayoría de mis paredes se muevan, activaré el hashing espacial para estas listas. 

# Agregando Sprites al Juego

Para crear sprites usaremos la clase arcade.Sprite. Podemos crear una instancia de la clase sprite con un código como este:

    self.player_sprite = arcade.Sprite("images/player_1/player_stand.png", CHARACTER_SCALING)

El primer parámetro es una cadena o ruta a la imagen que desea que cargue. Un segundo parámetro opcional escalará el sprite hacia arriba o hacia abajo. Si el segundo parámetro (en este caso, un CHARACTER_SCALING ) se establece en 0,5 y el sprite es de 128x128, tanto el ancho como el alto se reducirán en un 50 % para un sprite de 64x64.

A continuación, debemos saber a dónde va el sprite. Puedes usar los atributos center_x y center_y para posicionar el sprite. También puede usar arriba, abajo, izquierda y derecha para obtener o establecer la ubicación de los sprites por un borde en lugar del centro. También puede usar el atributo de posición para establecer tanto la x como la y al mismo tiempo

    self.player_sprite.center_x = 64
    self.player_sprite.center_y = 120

Finalmente, todas las instancias de la clase Sprite deben ir en una clase SpriteList.

    self.player_list.append(self.player_sprite)

Tenga en cuenta que el código crea Sprites de tres maneras:

* Creando una clase de Sprite, posicionándola, agregándola a la lista

* Crea una serie de sprites en un bucle. 
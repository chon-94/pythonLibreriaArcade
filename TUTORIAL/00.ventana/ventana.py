import arcade

# Constantes dimencion de la pantalla y nombre
ANCHO_PANTALLA = 1366
LARGO_PANTALLA = 768
TITULO_PANTALLA = "CHON"

class MyGame(arcade.Window):# Esta es la clase de la aplicacion principal

    def __init__(self):# Llama a la clase principal y configure la ventana
        
        super().__init__(ANCHO_PANTALLA, LARGO_PANTALLA, TITULO_PANTALLA)# Sino se colocan las variables se toman los valores por defecto

        arcade.set_background_color(arcade.csscolor.MIDNIGHT_BLUE) # Para darle color al fondo
        #arcade.set_background_color(arcade.color.DARK_SLATE_GRAY) # Para darle color al fondo

    def setup(self):# Configuracion del juego, si llamas a esta funcion se reinicia el juego 
        pass

    def on_draw(self):# Renderizado de pantalla

        self.clear()# El código para dibujar la pantalla va aquí

def main():# Funcion principal
    ventana = MyGame()
    ventana.setup()
    arcade.run()

if __name__ == "__main__":
    main()
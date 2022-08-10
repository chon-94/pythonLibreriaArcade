# Usar el editor de mapas en mosaico

Para esta parte, en lugar de colocar los mosaicos a través del código usando puntos específicos, usaremos un editor de mapas con el que podemos construir mapas y luego cargarlos en los archivos de mapas.

Para comenzar, descargue e instale el Editor de mapas en mosaico. (Piense en donar, ya que es un proyecto maravilloso proporcionado de forma gratuita).

Tiled ya tiene una excelente documentación disponible en https://doc.mapeditor.org/, por lo que para este tutorial supondremos que ya está familiarizado con la creación de mapas con Tiled. Si no es así, puede consultar la documentación de Tiled y volver aquí.

A partir de este punto del tutorial, cada capítulo trabajará con un mapa en mosaico. Si aún no desea crear el suyo propio, Arcade incluye algunos ejemplos en la carpeta de recursos incluida, que es de donde se extraen estos ejemplos, por lo que no tiene que crear sus propios mapas todavía si no lo desea.

Comenzaremos con un archivo map.json básico proporcionado por Arcade. Puede abrir este archivo en Tiled y ver cómo está configurado, pero ahora repasaremos algunos de los conceptos básicos. Puede guardar archivos en formato 'JSON' o 'TMX'.

En este mapa tenemos dos capas llamadas “Plataformas” y “Monedas”. En la capa de plataformas están todos los bloques con los que chocará un jugador usando el motor de física, y en la capa de monedas están todas las monedas que el jugador puede recoger para aumentar su puntuación. Eso es todo para este mapa.
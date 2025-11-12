- En lenguajes de marcas, la creacion de un portafolio de este tipo, es muy util, ya que se pueden hacer grandes paginas web de esta manera. Gracias al estilo CSS se le puede dar el diseño que queramos a nuestra pagina web, algo esencial en el mundo del desarrollo de aplicaciones web. En este caso se usa una estructura html sencilla con un css.


- Para empezar el ejercicio, hacemos el css de nuestro portafolio:
```
<style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #e6e6e6;
    }
    header, footer {
      background-color: #7da7df;
      color: white;
      text-align: center;
      padding: 10px;
    }
    main {
      padding: 20px;
    }
    article {
      background-color: white;
      margin-bottom: 15px;
      padding: 10px;
      border-radius: 5px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }
    article div {
        flex: 1;
    }
    article img {
      width: 100%;
      max-width: 300px;
      display: block;
      margin: 10px 0;
      border-radius: 5px;
    }
    </style>
```

- Primero, en el body, le ponemos la fuente que queramos, en este caso `Arial, sans-serif`, le añadimos margen, padding, y un color de fondo:
```
 body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #e6e6e6;
    }
```

- Despues seleccionamos el header y el footer, ya que queremos que sean iguales, le añadimos un color de fondo y de letra, añadimos `text-align: center;` lo que va a hacer es que nuestro texto se alinie automaticamente al centro y añadimos el padding:
```
header, footer {
      background-color: #7da7df;
      color: white;
      text-align: center;
      padding: 10px;
    }
```

- Le añadimos un padding al main:
```
 main {
      padding: 20px;
 }
 ```

- A los articulos, le añadimos el color de fondo, la separacion entre los distintos campos, el padding, añadimos `border-radius` que hace que las esquinas sean redondeadas, añadimos display flex, añadimos ` align-items: center;` lo que hace es que centra verticalmente texto e imagen, usamos `justify-content: space-between;`para separar el texto de la imagen y añadimos `gap` para dejar un espacio entre el texto y la imagen

- El texto de article lo hemos metido en un `div` para que flexbox sepa que parte es el texto


- En las imagenes le añadimos `width` para modificar el tamaño de la imagen, ponemos `height: auto;` para que la altura de la imagen sea automatica y por ultimo le ponemos los bordes redondos con `border-radius`




- Despues, en el body, añadimos `header`, `main` y `footer`

- Dentro de header, añadimos, en este caso mi nombre y mi correo:
```
<header>
    <h1>Daniel Calve Pardo</h1>
    <p>daniel@hola.com</p>
</header>
```

- En main, añadimos 6 articulos, con titulo, descripcion, fecha, imagen y categoria:
```
<article>
            <div>
                <h2>Titulo: Prueba1</h2>
                <p>Descripcion: Esto es una prueba de la prueba 1</p>
                <p>Fecha: 2025/11/12</p>
                <p>Categoria: Prueba</p>
            </div>
            <img src="examen.webp" alt="Prueba">
        </article>

        <article>
            <div>
                <h2>Titulo: Receta de Café Helado</h2>
                <p>Descripcion: Aprende a preparar un delicioso café helado en casa, perfecto para los días calurosos.</p>
                <p>Fecha: 2025/11/10</p>
                <p>Categoria: Bebidas</p>
            </div>
            <img src="cafe.webp" alt="Café helado">
        </article>

        <article>
            <div>
                <h2>Titulo: Paseo por el Parque</h2>
                <p>Descripcion: Un recorrido fotográfico por los rincones más tranquilos y verdes del parque central.</p>
                <p>Fecha: 2025/10/25</p>
                <p>Categoria: Naturaleza</p>
            </div>
            <img src="parque.webp" alt="Parque">
        </article>

        <article>
            <div>
                <h2>Titulo: Nueva Actualización de Software</h2>
                <p>Descripcion: Detalles sobre las mejoras de rendimiento y seguridad incluidas en la última versión.</p>
                <p>Fecha: 2025/11/01</p>
                <p>Categoria: Tecnología</p>
            </div>
            <img src="software.webp" alt="Actualización de software">
        </article>

        <article>
            <div>
                <h2>Titulo: Exposición de Arte Moderno</h2>
                <p>Descripcion: Una muestra de obras contemporáneas que exploran el color y la forma desde nuevas perspectivas.</p>
                <p>Fecha: 2025/09/30</p>
                <p>Categoria: Cultura</p>
            </div>
            <img src="arte.webp" alt="Exposición de arte">
        </article>

        <article>
            <div>
                <h2>Titulo: Consejos para Viajar Ligero</h2>
                <p>Descripcion: Cómo empacar solo lo necesario para disfrutar tus viajes sin exceso de equipaje.</p>
                <p>Fecha: 2025/11/05</p>
                <p>Categoria: Viajes</p>
            </div>
            <img src="viaje.webp" alt="Maleta de viaje">
        </article>
```


- En el footer añado mis redes sociales y el copyright:
```
<footer>
    <a href="https://instagram.com/daaani_.222">Instagram</a>
    <a href="https://github.com/danicp22">GitHub</a>
    <p>© 2025 Daniel Calve Pardo. Todos los derechos reservados.</p>
</footer>
```






- A continuacion se muestra un  ejercicio que, gracias a html y css, permite crear un portafolio basico:
```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portafolio trimestral</title>
    <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #e6e6e6;
    }
    header, footer {
      background-color: #7da7df;
      color: white;
      text-align: center;
      padding: 10px;
    }
    main {
      padding: 20px;
    }
    article {
      background-color: white;
      margin-bottom: 15px;
      padding: 10px;
      border-radius: 5px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }
    article div {
        flex: 1;
    }
    article img {
      width: 100%;
      max-width: 300px;
      display: block;
      margin: 10px 0;
      border-radius: 5px;
    }
    </style>
</head>
<body>
    <header>
        <h1>Daniel Calve Pardo</h1>
        <p>daniel@hola.com</p>
    </header>
    <main>
        <article>
            <div>
                <h2>Titulo: Prueba1</h2>
                <p>Descripcion: Esto es una prueba de la prueba 1</p>
                <p>Fecha: 2025/11/12</p>
                <p>Categoria: Prueba</p>
            </div>
            <img src="examen.webp" alt="Prueba">
        </article>

        <article>
            <div>
                <h2>Titulo: Receta de Café Helado</h2>
                <p>Descripcion: Aprende a preparar un delicioso café helado en casa, perfecto para los días calurosos.</p>
                <p>Fecha: 2025/11/10</p>
                <p>Categoria: Bebidas</p>
            </div>
            <img src="cafe.webp" alt="Café helado">
        </article>

        <article>
            <div>
                <h2>Titulo: Paseo por el Parque</h2>
                <p>Descripcion: Un recorrido fotográfico por los rincones más tranquilos y verdes del parque central.</p>
                <p>Fecha: 2025/10/25</p>
                <p>Categoria: Naturaleza</p>
            </div>
            <img src="parque.webp" alt="Parque">
        </article>

        <article>
            <div>
                <h2>Titulo: Nueva Actualización de Software</h2>
                <p>Descripcion: Detalles sobre las mejoras de rendimiento y seguridad incluidas en la última versión.</p>
                <p>Fecha: 2025/11/01</p>
                <p>Categoria: Tecnología</p>
            </div>
            <img src="software.webp" alt="Actualización de software">
        </article>

        <article>
            <div>
                <h2>Titulo: Exposición de Arte Moderno</h2>
                <p>Descripcion: Una muestra de obras contemporáneas que exploran el color y la forma desde nuevas perspectivas.</p>
                <p>Fecha: 2025/09/30</p>
                <p>Categoria: Cultura</p>
            </div>
            <img src="arte.webp" alt="Exposición de arte">
        </article>

        <article>
            <div>
                <h2>Titulo: Consejos para Viajar Ligero</h2>
                <p>Descripcion: Cómo empacar solo lo necesario para disfrutar tus viajes sin exceso de equipaje.</p>
                <p>Fecha: 2025/11/05</p>
                <p>Categoria: Viajes</p>
            </div>
            <img src="viaje.webp" alt="Maleta de viaje">
        </article>

    </main>
    <footer>
        <a href="https://instagram.com/daaani_.222">Instagram</a>
        <a href="https://github.com/danicp22">GitHub</a>
        <p>© 2025 Daniel Calve Pardo. Todos los derechos reservados.</p>
    </footer>
    
</body>
</html>
```





- Este ejercicio sirve muy bien para ver como un html puede mejorar visualmente de una manera muy sencilla utilizando css, gracias a css podemos alinear contenidos, cambiar tamaños, formas, colores y hacer una gran cantidad de acciones que hacen que nuestro codigo html pase de ser algo "aburrido" a una gran pagina web.

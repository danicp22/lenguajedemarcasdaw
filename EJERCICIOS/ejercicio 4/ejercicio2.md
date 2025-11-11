- Este ejercicio consiste en una versión simplificada de una página personal en HTML. Su objetivo es presentar de forma clara y ordenada información básica sobre una persona, incluyendo una breve biografía, experiencia docente y una imagen representativa. Es ideal como primer proyecto para practicar la estructura semántica de HTML5.





- En este ejercicio se utilizan los siguientes elementos clave:

`<nav>`: Para crear un menú de navegación con enlaces internos.
`<section>`: Para dividir el contenido en bloques temáticos (`inicio`, `sobre-mi`, `docencia`).
`<img>`: Para mostrar una imagen personal.
`<footer>`: Para incluir información de pie de página.
Atributos importantes
       `id`: Permite que los enlaces del menú naveguen a secciones específicas.
       `href="#seccion"`: Enlaces internos que apuntan a los `id` definidos.
       `alt`: Texto alternativo para accesibilidad en imágenes.



- A continuacion se muestra una pagina web en la que se me presenta al mundo digital, esta web contiene enlaces, imagenes y un menu de navegacion:
```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi página personal</title>
</head>
<body>

    <!-- Menú de navegación -->
    <nav>
        <ul>
            <li><a href="#inicio">Inicio</a></li>
            <li><a href="#sobre-mi">Sobre mí</a></li>
            <li><a href="#docencia">Docencia</a></li>
        </ul>
    </nav>

    <!-- Sección de inicio -->
    <section id="inicio">
        <h1>Daniel Calve Pardo</h1>
        <h2>Profesional del mundo digital</h2>
        <p>Bienvenido a mi página personal. Aquí encontrarás información sobre mí y mi experiencia.</p>
    </section>

    <!-- Sección sobre mí -->
    <section id="sobre-mi">
        <h2>Sobre mí</h2>
        <p>Me gusta el desarrollo web y el diseño digital. Disfruto aprender cosas nuevas y compartir conocimientos.</p>
        <img src="foto.webp" alt="Foto personal" width="200">
    </section>

    <!-- Sección docencia -->
    <section id="docencia">
        <h2>Docencia</h2>
        <p>He impartido clases y talleres de introducción al desarrollo web usando HTML y CSS.</p>
    </section>

    <!-- Pie de página -->
    <footer>
        <p>© 2025 Tu Nombre</p>
    </footer>

</body>
</html>

```




- Este ejercicio es una excelente base para comenzar a trabajar con HTML. Permite practicar la estructura semántica, el uso de enlaces internos y la incorporación de imágenes. A partir de aquí, se puede enriquecer con estilos CSS, interactividad con JavaScript o incluso convertirlo en un portafolio profesional.



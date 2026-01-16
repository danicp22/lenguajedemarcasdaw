- Mi proyecto es una pagina web de alquiler de rings de boxeo, he querido hacer una web seria y sin mucha tonteria, pero funcional. En este caso, voy a enfocarme en el tema de lenguaje de marcas, algo esencial, gracias a esto formamos la estructura de la web en HTML, y lo mas importante de cara al usuario, el estilo. La web permite al usuario elegir entre dos rings de boxeo (profesional o entrenamiento), cuando el usuario escoja el ring deseado, se le pedira que inicie sesion o que se registre en caso de que no tenga cuenta. Una vez el usuario haya entrado con su cuenta, se le va a facilitar un calendario para que seleccione el dia que quiere hacer la reserva, una vez elegido el dia, apareceran unas casillas con las horas que esten disponibles, cuando el usuario elija la hora que desea y confirme la reserva, esta reserva sera guardada en `mis reservas`, donde el usuario podra entrar siempre que quiera iniciando sesion. A continuacion, muestro la estructura de carpetas de mi proyecto:
```
├── app.py
├── basededatos
│   └── base.sql
├── static
│   ├── estilo.css
│   ├── logo_ig.png
│   ├── logo_maps.png
│   ├── ring1.jpg
│   └── ring2.jpg
└── templates
    ├── index.html
    ├── login.html
    ├── mis_reservas.html
    ├── registro.html
    └── reservar.html
```


- La pagina web comienza en `index.html`, en esta parte, se encuentra el inicio de la web, el usuario encontrara los botones para registrarse o iniciar sesion (en caso de que aun no se haya hecho, si ya se ha iniciado sesion, estos dos apartados pasaran a ser `Mis reservas` y una opcion para cerrar sesion), tambien encontrara los 2 tipos de ring que disponemos, con su precio y con su boton para alquilarlos, y por ultimo, en el footer se encuentra nuestro instagram y donde nos encontramos. 

- Para empezar, dentro del body, he creado un `nav` para la barra de navegacion:
```
<nav class="navbar">
        <div style="font-size: 1.5rem; color: var(--primary);">BOXING CLUB</div>
        <div class="nav-links">
            <a href="/">Inicio</a>
            {% if session.get("usuario_id") %}
                <a href="/mis_reservas">Mis Reservas</a>
                <a href="/logout">Salir ({{ session["usuario_nombre"] }})</a>
            {% else %}
                <a href="/login">Login</a>
                <a href="/registro">Registro</a>
            {% endif %}
        </div>
    </nav>
```

- Dentro del nav, he puesto el tamaño y el color del nombre del gimnasio:
```
<div style="font-size: 1.5rem; color: var(--primary);">BOXING CLUB</div>
```

- Despues, he utilizado jinja para que, en caso de que el usuario este logueado, aparezcan `mis reservas` y `Salir`, en caso de que no este logueado, aparecera `login` y `registro`:
```
{% if session.get("usuario_id") %}
                <a href="/mis_reservas">Mis Reservas</a>
                <a href="/logout">Salir ({{ session["usuario_nombre"] }})</a>
            {% else %}
                <a href="/login">Login</a>
                <a href="/registro">Registro</a>
            {% endif %}
```

- Despues, he creado un div, en el que hay un bucle jinja, este bucle lo que hace es mostrar una tarjeta con: imagen, nombre, descripcion, precio y el boton para alquilar, toda esta informacion es traida de la base de datos: 
```
<div class="container">
        <h1>Entrena como un Profesional</h1>
        <div class="ring-grid">
            {% for ring in rings %}
            <div class="card">
                <img src="/static/{{ ring.imagen }}" alt="ring">
                <h3>{{ ring.nombre }}</h3>
                <p>{{ ring.descripcion }}</p>
                <p><strong>{{ ring.precio }}€ / hora</strong></p>
                <a href="/reservar/{{ ring.id }}" class="btn">Alquilar Ahora</a>
            </div>
            {% endfor %}
        </div>
```

- Para finalizar la parte html de esta pagina, he creado un footer con dos links, uno para nuestro instagram y otro para nuestra localizacion:
```
<footer>
    <a href=""><img src="static/logo_ig.png"></a>
    <a href="https://maps.app.goo.gl/YhoR3ZVzep3zGAkx8"><img src="static/logo_maps.png"></a>
</footer>
```




- A continuacion, el `login`, el cual es muy similar a la pagina de incio pero tiene algunas diferencias. Esta parte de la web, permite que el usuario introduzca sus credenciales para acceder o crear su cuenta.

- En este caso, dentro del body, he creado un nav, el cual es muy parecido al de la pagina de inicio. La diferencia de este nav es que los links no cambian (no pasan de ser login y registro a ser mis reservas y salir), ya que es algo que no tiene mucho sentido, estas iniciando sesion o creandote una cuenta:
```
<nav class="navbar">
        <div class="nav-logo">BOXING CLUB</div>
        <div class="nav-links">
            <a href="/">Inicio</a>
            <a href="/registro">Registro</a>
        </div>
</nav>
```

- Despues, he creado un formulario que contiene: campos de email y contraseña (dentro de estos campos esta definido que el campo email es `type="email"` y que el campo contraseña es `type="password"`), un boton para iniciar sesion, y un mensaje abajo que muestra: `¿No tienes cuenta? Regístrate aquí`:
```
<div class="auth-container">
        <div class="auth-card">
            <h2>Entrar</h2>
            <form action="/login_usuario" method="post">
                <div class="form-group">
                    <label>Email:</label>
                    <input type="email" name="email" required>
                </div>
                <div class="form-group">
                    <label>Contraseña:</label>
                    <input type="password" name="password" required>
                </div>
                <input type="submit" value="INICIAR SESIÓN" class="btn" style="width: 100%;">
            </form>
            <div class="form-footer">
                ¿No tienes cuenta? <a href="/registro">Regístrate aquí</a>
            </div>
        </div>
</div>
```



- A continuacion, muestro el apartado de `registro`, este apartado permite al usuario crear una cuenta. He creado un formulario el cual le pide al usuario los siguentes campos: nombre completo en tipo texto; email en tipo email; contraseña en tipo password. Despues he añadido un boton para registrarse. Por ultimo, en el footer, he añadido un mensaje y un link que lleva a login para los usuarios que ya tienen una cuenta: `¿Ya eres miembro? <a href="/login">Inicia sesión</a>`

```
<div class="auth-container">
        <div class="auth-card">
            <h2>Crear Cuenta</h2>
            <form action="/guardar_usuario" method="post">
                <div class="form-group">
                    <label>Nombre Completo:</label>
                    <input type="text" name="nombre" required>
                </div>
                <div class="form-group">
                    <label>Email:</label>
                    <input type="email" name="email" required>
                </div>
                <div class="form-group">
                    <label>Contraseña:</label>
                    <input type="password" name="password" required>
                </div>
                <input type="submit" value="REGISTRARSE" class="btn" style="width: 100%;">
            </form>
            <div class="form-footer">
                ¿Ya eres miembro? <a href="/login">Inicia sesión</a>
            </div>
        </div>
    </div>
```









- A continuacion, muestro el apartado de `reservar`, este apartado permite al usuario reservar el ring.

- He creado un formulario para que el usuario elija el dia que desea alquilar un ring, siendo totalmente sincero, el calendario le pedi ayuda a una inteligencia artificial porque no me acordaba como se hacia.

```
<form method="GET" action="/reservar/{{ ring.id }}">
        <label>Elige una fecha para ver disponibilidad:</label><br><br>
        <input type="date" name="fecha" value="{{ fecha }}" onchange="this.form.submit()" style="padding: 10px;">
</form>
```


- Una vez haya fecha seleccionada (`{% if fecha %}`), se muestran las horas disponibles, gracias a un formulario:
```
<form action="/guardar_reserva" method="post" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
                <input type="hidden" name="id_ring" value="{{ ring.id }}">
                <input type="hidden" name="fecha" value="{{ fecha }}">
                
                {% for h in horario %}
                    {% if h in ocupadas %}
                        <button type="button" class="btn" disabled style="background: #333;">{{ h }}:00 Ocupado</button>
                    {% else %}
                        <label class="btn">
                            <input type="radio" name="hora" value="{{ h }}" required> {{ h }}:00
                        </label>
                    {% endif %}
                {% endfor %}
                <div style="grid-column: span 3; margin-top: 20px;">
                    <input type="submit" value="Confirmar Reserva" class="btn" style="width: 100%;">
                </div>
```

- Este formulario, recorre el horario, en caso de que haya una hora ocupada, deshabilita el boton, cambia el color y aparece como ocupado
- En este formulario he añadido css para organizar las horas en 3 columnas




- A continuacion, muestro el apartado `Mis reservas`, esta pagina lista todas las reservas del usuario. En este caso he creado una tabla, la cual tiene los siguientes campos: Ring, Fecha, Hora y Precio. En la tabla, he cleado un bucle jinja, que se conecta a los datos de la base de datos, esto permite que se vaya añadiendo sola la informacion a la tabla conforme el usuario vaya haciendo reservas, por ultimo he añadido un boton enlazado con la pagina de inicio para volver al inicio:

```
<div class="container">
        <h2>Mis Reservas</h2>
        <table>
            <tr><th>Ring</th><th>Fecha</th><th>Hora</th><th>Precio</th></tr>
            {% for r in reservas %}
            <tr>
                <td>{{ r.nombre }}</td>
                <td>{{ r.fecha }}</td>
                <td>{{ r.hora }}:00</td>
                <td>{{ r.precio }}€</td>
            </tr>
            {% endfor %}
        </table>
        <br><a href="/" class="btn">Volver al inicio</a>
</div>
```



- Por ultimo, muestro el css estructurado y claro a la vista, el cual no voy a explicar linea a linea pero voy a explicar con ejemplos:


- Variables globales (`:root`)

```
:root {
    --primary: #ff4d4d; 
    --dark: #121212;
    --gray: #1e1e1e;
    --text: #ffffff;
}
```

Define **variables CSS** para colores reutilizables:
    `--primary`: rojo principal (marca).
    `--dark`: fondo oscuro general.
    `--gray`: gris para tarjetas y contenedores.
    `--text`: color del texto.
Ventaja: si cambias un color aquí, se actualiza en todo el diseño.



- Estilo global del `body`

```
body {
    text-align: center;
    font-family: 'Arial', sans-serif;
    background-color: var(--dark);
    color: var(--text);
    margin: 0;
    line-height: 1.6;
}
```

Centra el texto por defecto.
Fuente legible (`Arial`).
Fondo oscuro y texto blanco (modo oscuro).
`margin: 0` elimina espacios por defecto.
`line-height: 1.6` mejora la legibilidad.



- Navegación (`.navbar`, `.nav-logo`, `.nav-links`)

```
.navbar {
    background: #000;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 3px solid var(--primary);
    margin-bottom: 20px;
}
```

Barra negra, con padding y **flexbox** para distribuir logo y enlaces.
Línea inferior roja para destacar.

```
.nav-logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--primary);
}
```

Logo grande y en color principal.

```
.nav-links a {
    color: white;
    text-decoration: none;
    margin-left: 15px;
    font-weight: bold;
    transition: 0.3s;
}
.nav-links a:hover {
    color: var(--primary);
}
```

Enlaces blancos, sin subrayado, con hover rojo.



- Contenedor principal

```
.container {
    padding: 2rem;
    max-width: 1000px;
    margin: auto;
}
```

Centra el contenido y limita el ancho para no ocupar toda la pantalla.



- Grid de rings

```
.ring-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}
```

Usa CSS Grid para tarjetas responsivas.
`auto-fit` ajusta columnas según espacio disponible.

```
.card {
    background: var(--gray);
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
    transition: 0.3s;
    border: 1px solid #333;
}
.card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 15px var(--primary);
    border-color: var(--primary);
}
```

Tarjetas con fondo gris, bordes redondeados y efecto hover (zoom + sombra roja).



- Botones

```
.btn {
    background: var(--primary);
    color: white;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 5px;
    text-decoration: none;
    cursor: pointer;
    display: inline-block;
    font-weight: bold;
    transition: 0.3s;
}
.btn:hover {
    background: #cc0000;
}
.btn:disabled {
    background: #444;
    cursor: not-allowed;
    opacity: 0.7;
}
```

Botones rojos con hover más oscuro.
Estado deshabilitado gris y con cursor bloqueado.



- Formularios (Login, Registro, Reservas)

```
.auth-container {
    display: flex; 
    justify-content: center; 
    align-items: center; 
    min-height: 70vh;
}
.auth-card {
    width: 100%; 
    max-width: 400px; 
    padding: 2.5rem;
    background: var(--gray);
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
```

Centra el formulario vertical y horizontalmente.
Tarjeta con sombra y bordes redondeados.

```
.form-group input:focus {
    border-color: var(--primary);
    outline: none;
}
```

Resalta el campo activo con borde rojo.



- Tablas (Mis Reservas)

```
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 2rem;
    background: var(--gray);
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 2px 2px 20px rgb(241, 109, 109);
}
th {
    background: var(--primary);
    color: white;
    text-transform: uppercase;
}
tr:hover {
    background: #252525;
}
```

Tabla estilizada con sombra, cabecera roja y efecto hover en filas.



- Footer

```
footer img {
  width: 75px;
  height: 75px;
  filter: drop-shadow(0 0 30px white);
}
```

Iconos con sombra blanca para destacar.






- En resumen, mi proyecto es una web sencilla pero funcional para alquilar rings de boxeo. Desde el principio quise que fuera clara, sin cosas innecesarias, pero que cumpliera bien su objetivo. Me he centrado en el lenguaje de marcas porque es la base de todo: gracias a HTML he podido dar estructura a la web y con CSS darle un estilo atractivo y profesional.

La idea era que el usuario pudiera navegar sin complicaciones: entra, ve los rings, elige el que quiere, se registra o inicia sesión si hace falta, selecciona fecha y hora y listo, su reserva queda guardada en “Mis reservas”. Todo esto lo he organizado con una estructura lógica y usando plantillas dinámicas para que la información se muestre de forma automática según la base de datos.

En cuanto al diseño, he usado variables CSS para mantener una paleta coherente, flexbox y grid para que todo se vea ordenado y responsivo, y pequeños detalles como hover y sombras para darle un toque más profesional. No he querido recargar la web, porque lo importante es que sea fácil de usar.

En definitiva, creo que he conseguido una web que cumple lo que promete: simple, clara y funcional. Si en el futuro la mejoro, añadiría más opciones de personalización y quizá un panel de administración, pero para este proyecto estoy satisfecho con el resultado.



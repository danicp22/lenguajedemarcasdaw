- En muchas aplicaciones, es habitual generar mensajes dinámicos que incluyen información del usuario y del sistema, como la fecha actual o datos de presentación. Para practicar estos conceptos, conviene trabajar con funciones con retorno que construyen textos a partir de parámetros (nombre, edad, ciudad) y emplear la API de fechas en JavaScript para formatear el día actual de forma amigable.




- Declaramos una función que saluda con la fecha
```
function saludarConFecha(nombre) {
    let hoy = new Date();
    return "Hola, " + nombre + ". Hoy es " + hoy.toLocaleDateString() + ".";
}
```

- Declaramos una función de presentación simple
```
function presentacion(nombre, edad) {
    return "Hola, mi nombre es " + nombre + " y tengo " + edad + " años.";
}
```


Declaración de una función con información completa- 
```
function informacionCompleta(nombre, edad, ciudad) {
    return "Hola, mi nombre es " + nombre + ", tengo " + edad + " años y vivo en " + ciudad + ".";
}
```


- Llamadas de ejemplo en consola
```
console.log(saludarConFecha("Dani"));
console.log(presentacion("Dani",18));
console.log(informacionCompleta("Dani",18,"Valencia"));
```



- A continuación se muestra un ejercicio que, gracias a cálculos y a condicionales, formatea la fecha en español, valida entradas y crea mensajes de presentación con plantillas para mejorar la legibilidad:


```
<script>
/* Programa para practicar conceptos de fechas y funciones con retorno
v0.1 Daniel Calve Pardo 2026
Este programa muestra conceptos de fechas y funciones con retorno
*/


// Fechas
function saludarConFecha(nombre) {
    let hoy = new Date();
    return "Hola, " + nombre + ". Hoy es " + hoy.toLocaleDateString() + ".";
}


// Funciones con retorno
function presentacion(nombre, edad) {
    return "Hola, mi nombre es " + nombre + " y tengo " + edad + " años.";
}


// Ejemplo
function informacionCompleta(nombre, edad, ciudad) {
    return "Hola, mi nombre es " + nombre + ", tengo " + edad + " años y vivo en " + ciudad + ".";
}

console.log(saludarConFecha("Dani"));
console.log(presentacion("Dani",18));
console.log(informacionCompleta("Dani",18,"Valencia"));


</script>
```




- Este ejercicio me ha servido para reforzar cómo trabajar con fechas en JavaScript y cómo construir funciones con retorno bien estructuradas. Además, al aplicar validaciones y plantillas de texto, siento que el código queda más claro y robusto para casos reales.


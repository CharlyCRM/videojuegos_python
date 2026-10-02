# Un ahorcado para practicar Python

Este juego de terminal fue una forma de practicar clases, entradas de usuario y cambios de estado. Separé las reglas del ahorcado de la interfaz que muestra la palabra, los intentos y la puntuación.

## Jugar

Necesitas Python 3 y una terminal interactiva. Solo utiliza módulos de la biblioteca estándar.

```sh
python3 ahorcado.py
```

Puedes introducir una letra o la palabra completa. Cada fallo resta un intento y 25 puntos; una letra correcta suma 50 puntos por aparición. Acertar la palabra completa suma 50 por su longitud. Hay seis intentos para cada palabra.

## Revisar el código

`Ahorcado` conserva letras, errores e intentos. `Interfaz` muestra el progreso y limpia la terminal. Es un ejemplo pequeño de separación entre reglas y presentación.

Mantengo el comportamiento de la práctica, incluidos los casos límite de reinicio. No tiene interfaz gráfica, guardado ni pruebas automatizadas. Es parte de mi aprendizaje de Python, no un videojuego publicado.

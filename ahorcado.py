import random
import os
import sys
import time

class Ahorcado:
    DIBUJOS_AHORCADO = [
        '''
           +---+
               |
               |
               |
              ===''',
        '''
           +---+
           O   |
               |
               |
              ===''',
        '''
           +---+
           O   |
           |   |
               |
              ===''',
        '''
           +---+
           O   |
          /|   |
               |
              ===''',
        '''
           +---+
           O   |
          /|\  |
               |
              ===''',
        '''
           +---+
           O   |
          /|\  |
          /    |
              ===''',
        '''
           +---+
           O   |
          /|\  |
          / \  |
              ==='''
    ]

    def __init__(self, lista_palabras: list):
        self.palabra = self._elegir_palabra(lista_palabras)
        self.adivinar_letra = []
        self.letras_incorrectas = []
        self.intentos_permitidos = 6
        self.puntuacion = 0  # Nueva variable para la puntuación

    def _elegir_palabra(self, lista_palabras):
        """
        Elige una palabra aleatoria de la lista
        """
        return random.choice(lista_palabras).upper()

    def adivinar(self, entrada):
        """
        Adivina la letra o palabra y actualiza el estado
        """
        entrada = entrada.upper()
        if not entrada.isalpha():
            return False
            
        if len(entrada) > 1:  # Si es una palabra
            if entrada == self.palabra:
                self.adivinar_letra.extend(list(self.palabra))
                self.puntuacion += 50 * len(self.palabra)  # Bonus por adivinar la palabra completa
                return True
            else:
                self.intentos_permitidos -= 1
                self.puntuacion -= 25  # Penalización por palabra incorrecta
                return False
        
        if entrada in self.adivinar_letra or entrada in self.letras_incorrectas:
            return False
            
        if entrada in self.palabra:
            self.adivinar_letra.append(entrada)
            # Sumamos puntos por cada vez que aparece la letra en la palabra
            self.puntuacion += 50 * self.palabra.count(entrada)
            return True
        else:
            self.letras_incorrectas.append(entrada)
            self.intentos_permitidos -= 1
            self.puntuacion -= 25  # Penalización por letra incorrecta
            return False

    def ganar(self):
        """
        Comprueba si todas las letras han sido adivinadas
        """
        return all(letras in self.adivinar_letra for letras in self.palabra)

    def perder(self):
        """
        Comprueba si se han agotado los intentos
        """
        return self.intentos_permitidos <= 0

    def reiniciar_palabra(self, lista_palabras):
        """
        Reinicia el juego con una nueva palabra
        """
        self.palabra = self._elegir_palabra(lista_palabras)
        self.adivinar_letra = []
        self.letras_incorrectas = []


class Interfaz:
    """
    Clase encargada de mostrar el estado del juego
    """
    def __init__(self, juego):
        self.juego = juego

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_progreso(self):
        """
        Muestra el progreso de la partida
        """
        self.limpiar_pantalla()
        print(Ahorcado.DIBUJOS_AHORCADO[6 - self.juego.intentos_permitidos])
        progreso = [letra if letra in self.juego.adivinar_letra else "_" for letra in self.juego.palabra]
        print("\nPalabra: ", " ".join(progreso))

    def mostrar_estado(self):
        """
        Muestra el estado del juego
        """
        print(f"\nIntentos restantes: {self.juego.intentos_permitidos}")
        print(f"Letras correctas: {', '.join(sorted(self.juego.adivinar_letra))}")
        print(f"Letras incorrectas: {', '.join(sorted(self.juego.letras_incorrectas))}")


class Jugador:
    def __init__(self, interfaz):
        self.interfaz = interfaz
        self.nombre = self._solicitar_nombre()

    def _solicitar_nombre(self):
        """Solicita y valida el nombre del jugador con una animación de bienvenida"""
        titulo_ascii = [
            """
    ╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗
    ╠═╣╠═╣║ ║╠═╝║  ╠═╣ ║║║ ║
    ╩ ╩╩ ╩╚═╝╩  ╚═╝╩ ╩═╩╝╚═╝
        """,
            """
     █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗
    ██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗
    ███████║███████║██║   ██║██████╔╝██║     ███████║██║  ██║██║   ██║
    ██╔══██║██╔══██║██║   ██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║
    ██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝
        """
        ]
        
        loading = [
            "[    ]",
            "[=   ]",
            "[==  ]",
            "[=== ]",
            "[====]",
            "[ ===]",
            "[  ==]",
            "[   =]",
            "[    ]",
            "[   =]",
            "[  ==]",
            "[ ===]",
            "[====]",
            "[=== ]",
            "[==  ]",
            "[=   ]"
        ]
        
        # Animación del título
        for _ in range(3):  # Repetir 3 veces
            for titulo in titulo_ascii:
                self.interfaz.limpiar_pantalla()
                print("\n" * 3)
                print(titulo)
                time.sleep(0.3)
        
        # Animación de carga
        self.interfaz.limpiar_pantalla()
        print(titulo_ascii[1]) 
        print("\nCargando juego...")
        
        for _ in range(2): 
            for frame in loading:
                print(f"\r{frame}", end="", flush=True)
                time.sleep(0.1)
        
        self.interfaz.limpiar_pantalla()
        print(titulo_ascii[1])
        print("\n¡Bienvenido al juego del Ahorcado!\n")
        
        # Solicitar nombre con validación
        while True:
            nombre = input("👤 Introduce tu nombre: ").strip().capitalize()
            if not nombre:
                print("❌ El nombre no puede estar vacío")
                time.sleep(1)
                continue
            if not nombre.replace(" ", "").isalpha():
                print("❌ El nombre solo puede contener letras")
                time.sleep(1)
                continue
                
            # Animación de confirmación
            print("\n✨ Validando nombre", end="")
            for _ in range(3):
                time.sleep(0.3)
                print(".", end="", flush=True)
            
            print(f"\n\n🎮 ¡Bienvenido {nombre}! Preparando el juego...")
            time.sleep(2)
            return nombre

    def solicitar_letra(self):
        """
        Solicita una letra o palabra y valida la entrada
        """
        while True:
            entrada = input("\nIntroduce una letra o adivina la palabra: ").strip()
            if entrada and entrada.isalpha():
                return entrada
            print("Por favor, introduce solo letras")


class Creditos:
    def __init__(self):
        self.desarrollador = "Carlos Ramírez Martín"
        self.nombre_juego = "JUEGO DEL AHORCADO"
        self.año = "2024"
    
    def _limpiar_pantalla(self):
        """Limpia la pantalla en cualquier sistema operativo"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_creditos(self):
        """Muestra la pantalla de créditos y espera 5 segundos"""
        self._limpiar_pantalla()
        
        print("\n" * 10)  # Espaciado superior
        print("=" * 50)
        print(f"\n        {self.nombre_juego}")
        print("        Desarrollado por:\n")
        print(f"        {self.desarrollador}")
        print(f"        www.linkedin.com/in/carlosramirezmartin")
        print(f"\n        © {self.año} Todos los derechos reservados")
        print("\n" + "=" * 50)
        
        time.sleep(5)
        self._limpiar_pantalla()


class ControladorJuego:
    """
    Clase encargada de coordinar el juego entre el jugador, el juego y la interfaz
    """
    def __init__(self, lista_palabras):
        self.lista_palabras = lista_palabras  # Guardamos la lista para poder elegir nuevas palabras
        self.juego = Ahorcado(lista_palabras)
        self.interfaz = Interfaz(self.juego)
        self.jugador = Jugador(self.interfaz)
        self.creditos = Creditos()
    
    def jugar(self):
        try:
            while not self.juego.perder():  # verifico si ha perdido
                self.interfaz.mostrar_progreso()
                self.interfaz.mostrar_estado()
                adivinar = self.jugador.solicitar_letra()
                self.juego.adivinar(adivinar)

                if self.juego.ganar(): # verifico si ha ganado
                    self.interfaz.mostrar_progreso()
                    print(f"\n¡Felicidades {self.jugador.nombre}, has adivinado la palabra! 🎉")
                    print(f"Puntuación actual: {self.juego.puntuacion} puntos")
                    print("\nPreparando nueva palabra...")
                    time.sleep(2)
                    self.juego.reiniciar_palabra(self.lista_palabras)
                    continue

            # El jugador ha perdido
            self.interfaz.mostrar_progreso()
            print(f"\nLo siento {self.jugador.nombre}, te has quedado sin intentos 😢")
            print(f"La última palabra era: {self.juego.palabra}")
            print(f"\nPuntuación final: {self.juego.puntuacion} puntos")
            
            input("\nPresiona Enter para ver los créditos...")
            self.creditos.mostrar_creditos()
        except KeyboardInterrupt:
            print("\n\nJuego interrumpido. ¡Hasta luego!")
            time.sleep(2)
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")
            time.sleep(2)


if __name__ == "__main__":
    
    try:
        lista_palabras = [
            # Conceptos básicos de Python
            "python", "programacion", "interprete", "cython", "tecnologia",
            "jython", "algoritmo", "variable", "rpython", "guido"
            "funcion", "clase", "objeto", "herencia", "polimorfismo",
            
            # Tipos de datos
            "string", "integer", "float", "boolean", "lista",
            "tupla", "diccionario", "conjunto", "vector", "matriz",
            
            # Estructuras de control
            "bucle", "while", "for", "if", "else",
            "elif", "switch", "match", "break", "continue",
            
            # Conceptos de POO
            "instancia", "metodo", "atributo", "constructor", "decorador",
            "encapsulamiento", "abstraccion", "interfaz", "superclase", "subclase",
            
            # Módulos y paquetes
            "modulo", "paquete", "biblioteca", "framework", "dependencia",
            "importacion", "namespace", "pip", "virtual", "entorno",
            
            # Manejo de datos
            "archivo", "json", "csv", "xml", "base",
            "mysql", "postgresql", "sqlite", "mongodb", "redis",
            
            # Conceptos avanzados
            "assert", "threading", "multiprocess", "decorator", "generator",
            "iterator", "exception", "lambda", "closure", "recursion",
            
            # Herramientas y frameworks
            "django", "flask", "fastapi", "pytest", "selenium",
            "jupyter", "pandas", "numpy", "tensorflow", "pytorch",
            
            # Buenas prácticas
            "debug", "testing", "docstring", "comentario", "pep8",
            "refactoring", "clean", "solid", "patron",
        ]
        
        controlador = ControladorJuego(lista_palabras)
        controlador.jugar()
    except Exception as e:
        print(f"Error al iniciar el juego: {e}")
        input("\nPresiona Enter para salir...")



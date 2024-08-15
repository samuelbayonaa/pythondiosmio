from abc import ABC, abstractmethod

class Juego(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def mostrar_puntaje(self):
        pass

    @abstractmethod
    def terminar(self):
        pass

class JuegoSencillo(Juego):
    def iniciar(self):
        print("¡Bienvenido al juego")

    def mostrar_puntaje(self):
        print("Puntaje: 100")

    def terminar(self):
        print("Fin del juego.")

juego = JuegoSencillo()
juego.iniciar()
juego.mostrar_puntaje()
juego.terminar()

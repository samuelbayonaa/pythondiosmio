from tabulate import tabulate

class Estudiante:
    # Atributos de clase
    institucion = "Instituto Académico"  # Todos los estudiantes pertenecen a la misma institución
    contador_estudiantes = 0  # Contador del número de estudiantes

    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        Estudiante.contador_estudiantes += 1  # Incrementa el contador al crear un nuevo estudiante

    def obtener_nota_promedio(self):
        return (self.nota1 + self.nota2) / 2

    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Nombre: {self.nombre}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Nota Promedio: {promedio:.2f}")

    def __str__(self):
        return f"Estudiante: {self.nombre}, Nota Promedio: {self.obtener_nota_promedio():.2f}"

    @classmethod
    def cambiar_institucion(cls, nueva_institucion):
        cls.institucion = nueva_institucion

    @classmethod
    def ver_escala(cls):
        escala = [
            ["0 a 2.9", "Baja"],
            ["3 a 3.9", "Media"],
            ["4 a 4.5", "Alta"],
            ["4.6 a 5", "Sobresaliente"]
        ]
        print(tabulate(escala, headers=["Nota", "Calificación"], tablefmt="grid"))

# Ejemplo de uso
estudiante1 = Estudiante("Samuel Bayona", 4.2, 4.8)
estudiante2 = Estudiante("Maria Avila", 3.5, 3.9)

estudiante1.mostrar_informacion()
print(estudiante2)

Estudiante.ver_escala()

# Cambiar la institución para todos los estudiantes
Estudiante.cambiar_institucion("Nueva Institución Educativa")
print(f"Institución: {Estudiante.institucion}")
print(f"Número de estudiantes: {Estudiante.contador_estudiantes}")

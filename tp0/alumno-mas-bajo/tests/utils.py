class Alumno:
    def __init__(self, nombre: str, altura: float):
        self.nombre = nombre
        self.altura = altura

    def __repr__(self):
        return f"{self.nombre}({self.altura})"

alice = Alumno("Alice", 1.50)
bob = Alumno("Bob", 1.40)
carl = Alumno("Carl", 1.30)
daisy = Alumno("Daisy", 1.20)
emily = Alumno("Emily", 1.45)
frank = Alumno("Frank", 1.50)
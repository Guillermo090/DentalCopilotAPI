class Paciente:
    def __init__(self, id, nombre, apellido, edad, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años"

    # Puedes agregar más métodos según las necesidades, como métodos de validación o formateo
from db.modelo_paciente import Paciente
from base_de_datos import BaseDeDatos

class ControladorPacientes:
    def __init__(self):
        # self.lista_pacientes = []
        self.base_de_datos = BaseDeDatos()

    def agregar_paciente(self, nombre, apellido, edad, direccion, telefono):
        # nuevo_paciente = Paciente(nombre, apellido, edad, direccion, telefono)
        # self.lista_pacientes.append(nuevo_paciente)
        # return nuevo_paciente
        nuevo_paciente = Paciente(None, nombre, apellido, edad, direccion, telefono)
        self.base_de_datos.agregar_paciente(nuevo_paciente)
        return nuevo_paciente

    def obtener_lista_pacientes(self):
        return self.base_de_datos.obtener_lista_pacientes()

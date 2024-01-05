import tkinter as tk
from tkinter import ttk
from controlador_pacientes import ControladorPacientes
from utilidades import cargar_estilos_desde_archivo

class VentanaPacientes:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestionar Pacientes")

        # Crear controlador de pacientes
        self.controlador_pacientes = ControladorPacientes()

        # Crear la ventana de pacientes
        self.frame_pacientes = ttk.Frame(self.master)
        self.frame_pacientes.pack(fill=tk.BOTH, expand=True)

        # Crear widgets para gestionar pacientes (ejemplo: un botón para agregar pacientes)
        btn_agregar_paciente = tk.Button(self.frame_pacientes, text="Agregar Paciente", command=self.abrir_ventana_agregar_paciente)
        btn_agregar_paciente.pack(pady=10)

        btn_listar_pacientes = tk.Button(self.frame_pacientes, text="Listar Pacientes", command=self.abrir_ventana_listar_pacientes)
        btn_listar_pacientes.pack(pady=10)

    def abrir_ventana_agregar_paciente(self):
        # Lógica para abrir la ventana de agregar pacientes
        nueva_ventana = tk.Toplevel(self.master)
        nueva_ventana.title("Agregar Paciente")

        # Crear widgets en la nueva ventana para recopilar información del paciente
        label_nombre = tk.Label(nueva_ventana, text="Nombre:")
        label_nombre.grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(nueva_ventana)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        label_apellido = tk.Label(nueva_ventana, text="Apellido:")
        label_apellido.grid(row=1, column=0, padx=10, pady=10)
        entry_apellido = tk.Entry(nueva_ventana)
        entry_apellido.grid(row=1, column=1, padx=10, pady=10)

        label_edad = tk.Label(nueva_ventana, text="Edad:")
        label_edad.grid(row=2, column=0, padx=10, pady=10)
        entry_edad = tk.Entry(nueva_ventana)
        entry_edad.grid(row=2, column=1, padx=10, pady=10)

        label_direccion = tk.Label(nueva_ventana, text="Dirección:")
        label_direccion.grid(row=3, column=0, padx=10, pady=10)
        entry_direccion = tk.Entry(nueva_ventana)
        entry_direccion.grid(row=3, column=1, padx=10, pady=10)

        label_telefono = tk.Label(nueva_ventana, text="Teléfono:")
        label_telefono.grid(row=4, column=0, padx=10, pady=10)
        entry_telefono = tk.Entry(nueva_ventana)
        entry_telefono.grid(row=4, column=1, padx=10, pady=10)

        # Función para manejar el clic en el botón de agregar paciente
        def agregar_paciente():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            edad = entry_edad.get()
            direccion = entry_direccion.get()
            telefono = entry_telefono.get()

            # Validar y agregar el paciente al controlador
            nuevo_paciente = self.controlador_pacientes.agregar_paciente(nombre, apellido, edad, direccion, telefono)
            if nuevo_paciente:
                # Puedes realizar acciones adicionales si el paciente se agrega con éxito
                print(f"Paciente agregado: {nuevo_paciente}")
                nueva_ventana.destroy()

        # Botón para agregar paciente
        btn_agregar = tk.Button(nueva_ventana, text="Agregar", command=agregar_paciente)
        btn_agregar.grid(row=5, column=0, columnspan=2, pady=10)

    def abrir_ventana_listar_pacientes(self):
        # Lógica para abrir la ventana de listar pacientes
        ventana_listar_pacientes = VentanaListarPacientes(tk.Toplevel(self.master), self.controlador_pacientes)


class VentanaListarPacientes:
    def __init__(self, master, controlador_pacientes):
        self.master = master
        self.master.title("Listar Pacientes")

        # Controlador de pacientes
        self.controlador_pacientes = controlador_pacientes

        # Crear la ventana de listar pacientes
        self.frame_listar_pacientes = ttk.Frame(self.master)
        self.frame_listar_pacientes.pack(fill=tk.BOTH, expand=True)

        # Crear una tabla para mostrar los pacientes
        self.tree = ttk.Treeview(self.frame_listar_pacientes, columns=("Nombre", "Apellido", "Edad"))
        # self.tree.heading("#0", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Edad", text="Edad")

        # self.tree.column("#0", width=50)
        self.tree.column("Nombre", anchor=tk.W, width=100)
        self.tree.column("Apellido", anchor=tk.W, width=100)
        self.tree.column("Edad", anchor=tk.W, width=50)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Llenar la tabla con datos de pacientes
        self.actualizar_lista_pacientes()

    def actualizar_lista_pacientes(self):
        # Limpiar la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtener la lista de pacientes desde el controlador
        lista_pacientes = self.controlador_pacientes.obtener_lista_pacientes()
        print(lista_pacientes)

        # Llenar la tabla con datos de pacientes
        for paciente in lista_pacientes:
            self.tree.insert("", "end", values=(paciente.nombre, paciente.apellido, paciente.edad))


class Paciente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
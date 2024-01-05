import tkinter as tk
from ventana_pacientes import VentanaPacientes
# from ventana_citas import VentanaCitas
# from ventana_informes import VentanaInformes
from utilidades import cargar_estilos_desde_archivo

class VentanaPrincipal:
    def __init__(self, master):

        # Configurar estilos
        cargar_estilos_desde_archivo(master, "estilos/estilo.css")

        self.master = master
        self.master.geometry("800x600")

        # Botones para acceder a diferentes módulos
        btn_pacientes = tk.Button(master, text="Gestionar Pacientes", command=self.abrir_ventana_pacientes)
        btn_pacientes.pack(pady=10)

        # btn_citas = tk.Button(master, text="Gestionar Citas", command=self.abrir_ventana_citas)
        # btn_citas.pack(pady=10)

        # btn_informes = tk.Button(master, text="Generar Informes", command=self.abrir_ventana_informes)
        # btn_informes.pack(pady=10)

    def abrir_ventana_pacientes(self):
        ventana_pacientes = VentanaPacientes(self.master)

    # def abrir_ventana_citas(self):
    #     ventana_citas = VentanaCitas(self.master)

    # def abrir_ventana_informes(self):
    #     ventana_informes = VentanaInformes(self.master)

# Este bloque permite ejecutar la aplicación al ejecutar este script directamente
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
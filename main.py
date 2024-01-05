import tkinter as tk
from ventana_principal import VentanaPrincipal

def main():
    # Crear la aplicación Tkinter
    app = tk.Tk()
    app.title("Clínica Dental App")

    # Crear la ventana principal y pasar la aplicación como parámetro
    ventana_principal = VentanaPrincipal(app)

    # Iniciar el bucle principal de la aplicación
    app.mainloop()

if __name__ == "__main__":
    main()
# Dental Copilot App

La aplicación Dental Copilot es una aplicación de escritorio desarrollada en Python con Tkinter para la gestión de una clínica dental. Permite realizar operaciones como agregar pacientes, programar citas y generar informes.

## Estructura de carpetas

- **imagenes/**
  - Contiene imágenes utilizadas en la interfaz gráfica.
- **estilos/**
  - Almacena archivos CSS para personalizar la apariencia de la interfaz.
- **controladores/**
  - Módulos que contienen la lógica de control para gestionar pacientes, citas, etc.
- **modelos/**
  - Módulos que definen las clases de datos, como el modelo de paciente y el modelo de cita.
- **ventanas/**
  - Módulos que contienen las clases para las ventanas de la interfaz gráfica, como la ventana principal y la ventana para listar pacientes.
- **utilidades/**
  - Módulos con funciones y clases de utilidad utilizadas en toda la aplicación.
- **base_de_datos.py**
  - Módulo para la gestión de la base de datos SQLite.
- **main.py**
  - Archivo principal que inicia la aplicación y configura la interfaz.

## Requisitos

Asegúrate de tener Python 3.x instalado en tu sistema. Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
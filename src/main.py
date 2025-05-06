
import tkinter as tk
from views.view import View
from controllers.controller import Controller
from models.model import DataModel as Model

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Calculadora de Fracciones")
    root.geometry("600x400+100+0")
    root.config(bg="lightblue")
    root.iconbitmap("src/logo.ico")  # Asegúrate de que el archivo logo.ico exista y esté en la ruta correcta

    # Crear el modelo, la vista y el controlador
    model = Model()
    view = View(root)
    controller = Controller(model, view)

    # Iniciar el bucle principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
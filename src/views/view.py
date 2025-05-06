from tkinter import Tk, Label, Button, Frame, Entry

class View:
    def __init__(self, master):
        self.master = master
        master.title("MVC Fracciones")

        self.frame = Frame(master)
        self.frame.pack()

        # Entrada para numerador y denominador
        self.numerador_entry = Entry(self.frame)
        self.numerador_entry.pack()
        self.denominador_entry = Entry(self.frame)
        self.denominador_entry.pack()

        # Botón para añadir fracción
        self.add_button = Button(self.frame, text="Añadir Fracción", command=self.on_add_button_click)
        self.add_button.pack()

        # Botones para operaciones
        self.suma_button = Button(self.frame, text="Sumar", command=lambda: self.on_operate_button_click("suma"))
        self.suma_button.pack()

        self.resta_button = Button(self.frame, text="Restar", command=lambda: self.on_operate_button_click("resta"))
        self.resta_button.pack()

        self.multiplicacion_button = Button(self.frame, text="Multiplicar", command=lambda: self.on_operate_button_click("multiplicacion"))
        self.multiplicacion_button.pack()

        self.division_button = Button(self.frame, text="Dividir", command=lambda: self.on_operate_button_click("division"))
        self.division_button.pack()

        # Etiqueta para mostrar resultados
        self.result_label = Label(self.frame, text="")
        self.result_label.pack()

    def update_display(self, text):
        """Actualiza la etiqueta con el texto proporcionado."""
        self.result_label.config(text=text)
from tkinter import Tk,Frame, Entry, Button, Label

class View:
    def __init__(self, master):
        self.master = master
        master.title("MVC Fracciones")

        self.frame = Frame(master)
        self.frame.pack()

        # Inicializa el atributo como None
        self.on_add_button_click = None
        self.on_sumar_button_click = None
        self.on_subtract_button_click = None
        self.on_multiply_button_click = None
        self.on_divide_button_click = None
        self.on_view_button_click = None
        self.on_clear_button_click = None
        self.on_simplificar_button_click = None

        # Entrada para numerador y denominador
        self.numerador_entry = Entry(self.frame, width=10)
        self.numerador_entry.config(bg="lightblue", fg="black")
        self.numerador_entry.pack()
        self.denominador_entry = Entry(self.frame, width=10)
        self.denominador_entry.config(bg="lightblue", fg="black")
        self.denominador_entry.pack()

        # Botón para añadir fracción
        self.add_button = Button(self.frame, text="Añadir Fracción", command=self._handle_add_button_click)
        self.add_button.config(bg="white", fg="black", activebackground= "lightblue")
        self.add_button.pack()

        # Botón para sumar fracciones
        self.sumar_button = Button(self.frame, text="Sumar", command=self._handle_sumar_button_click)
        self.sumar_button.config(bg="white", fg="black")
        self.sumar_button.pack()

        # Botón para restar fracciones
        self.subtract_button = Button(self.frame, text="Restar", command=self._handle_subtract_button_click)
        self.subtract_button.pack()

        # Botón para multiplicar fracciones
        self.multiply_button = Button(self.frame, text="Multiplicar", command=self._handle_multiply_button_click)
        self.multiply_button.pack()

        # Botón para dividir fracciones
        self.divide_button = Button(self.frame, text="Dividir", command=self._handle_divide_button_click)
        self.divide_button.pack()

        # Botón para ver fracciones
        self.view_button = Button(self.frame, text="Ver Fracciones", command=self._handle_view_button_click)
        self.view_button.pack()

        # Boton para simplificar fracción
        self.simplificar_button = Button(self.frame, text="Simplificar Fracción", command=self._handle_simplificar_button_click)
        self.simplificar_button.pack()
        
        #Boton para limpiar
        self.clear_button = Button(self.frame, text="Limpiar", command=self._handle_clear_button_click)
        self.clear_button.pack()

    def _handle_add_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_add_button_click:
            numerador = int(self.numerador_entry.get())
            denominador = int(self.denominador_entry.get())
            self.on_add_button_click(numerador, denominador)
        else:
            print("Error: No se ha asignado un controlador para el botón 'Añadir Fracción'")

    def _handle_sumar_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_sumar_button_click:
            self.on_sumar_button_click()
        else:
            print("Error: No se ha asignado un controlador para el botón 'Sumar'")
    
    def _handle_subtract_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_subtract_button_click:
            self.on_subtract_button_click()
        else:
            print("Error: No se ha asignado un controlador para el botón 'Restar'")

    def _handle_multiply_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_multiply_button_click:
            self.on_multiply_button_click()
        else:
            print("Error: No se ha asignado un controlador para el botón 'Multiplicar'")
    
    def _handle_divide_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_divide_button_click:
            self.on_divide_button_click()
        else:
            print("Error: No se ha asignado un controlador para el botón 'Dividir'")

    def _handle_simplificar_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_simplificar_button_click:
            self.on_simplificar_button_click()
        else:
            print("Error: No se ha asignado un controlador para el botón 'Simplificar Fracción'")

    def _handle_view_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_view_button_click:
            self.on_view_button_click()
        else:
            print("Error: No se ha asignado un controlador para el botón 'Ver Fracciones'")

    def update_display(self, text):
        """Actualiza la etiqueta con el texto proporcionado."""
        if not hasattr(self, 'result_label'):
            self.result_label = Label(self.frame, text="")
            self.result_label.config(bg="yellow", fg="black", font=("Arial", 14))
            self.result_label.pack()
        self.result_label.config(text=text)

    def _handle_clear_button_click(self):
        """Llama al método asignado por el controlador."""
        if self.on_clear_button_click:
            self.on_clear_button_click()
        else:
            print("Error: No se ha asignado un controlador para el botón 'Limpiar'")
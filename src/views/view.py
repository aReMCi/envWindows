from tkinter import Tk, Label, Button, Frame

class View:
    
    def __init__ (self, master):
        #Master = Ventana principal
        self.master = master
        master.title("MCV Tkinter App Practice")

        #Muestra la ventana principal
        self.frame = Frame(master)
        self.frame.pack()

        #Crea y posiciona la etiqueta en la ventana
        self.label = Label(self.frame, text= "Hola MVC!")
        self.label.pack()

        #Cera y muestra el botón en la ventana
        self.button = Button(self.frame, text="Click aqui", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Boton Presionado")

    def update_label(self, text):   
        self.label.config(text=text)     
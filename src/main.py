import tkinter as tk
from views.view import View
from controllers.controller import Controller
from models.model import DataModel as Model

def main():
    root = tk.Tk()
    root.title("Tkinter MVC App")
    root.geometry("600x400")
    root.iconbitmap("logo.bmp")
    root.config(bg="lightblue")

    model = Model()
    model.add_data("Sample Data option 1")
    view = View(root)
    controller = Controller(model, view)
    
    root.mainloop()

if __name__ == "__main__":
    main()
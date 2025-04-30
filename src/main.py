import tkinter as tk
from view.view import View
from controller.controller import Controller
from models.model import data_model as Model

def main():
    root = tk.Tk()
    root.title("Tkinter MVC App")
    
    model = Model()
    model.set_data("Sample Data option 1")
    view = view(root)
    controller = Controller(view,model)
    
    root.mainloop()

if __name__ == "__main__":
    main()
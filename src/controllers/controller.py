
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Vincula los botones de la vista con los métodos del controlador
        self.view.on_add_button_click = self.add_fraccion
        self.view.on_operate_button_click = self.operate_fracciones

    def add_fraccion(self, numerador, denominador):
        """Añade una fracción al modelo."""
        try:
            self.model.add_fraccion(numerador, denominador)
            self.view.update_display(f"Fracción añadida: {numerador}/{denominador}")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")

    def operate_fracciones(self, operation):
        """Realiza una operación entre las dos últimas fracciones."""
        try:
            if operation == "suma":
                resultado = self.model.suma()
            elif operation == "resta":
                resultado = self.model.resta()
            elif operation == "multiplicacion":
                resultado = self.model.multiplicacion()
            elif operation == "division":
                resultado = self.model.division()
            else:
                self.view.update_display("Operación no válida.")
                return

            # Actualiza la vista con el resultado
            self.view.update_display(f"Resultado: {resultado.numerador}/{resultado.denominador}")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")
        
        

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Vincula los botones de la vista con los métodos del controlador
        self.view.on_add_button_click = self.add_fraccion
        self.view.on_sumar_button_click = self.sumar_fracciones
        self.view.on_subtract_button_click = self.restar_fracciones
        self.view.on_multiply_button_click = self.multiplicar_fracciones
        self.view.on_divide_button_click = self.dividir_fracciones
        self.view.on_view_button_click = self.view_fracciones
        self.view.on_clear_button_click = self.clear_fracciones
        self.view.on_simplificar_button_click = self.simplificar_fraccion

    def add_fraccion(self, numerador, denominador):
        """Añade una fracción al modelo."""
        try:
            self.model.add_fraccion(numerador, denominador)
            self.view.update_display(f"Fracción añadida: {numerador}/{denominador}")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")

    def sumar_fracciones(self):
        """Suma las dos últimas fracciones del modelo."""
        try:
            resultado = self.model.suma()
            self.view.update_display(f"Resultado: {resultado.numerador}/{resultado.denominador}")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")

    def restar_fracciones(self):
        """Resta las dos últimas fracciones del modelo."""
        try:
            resultado = self.model.resta()
            self.view.update_display(f"Resultado: {resultado.numerador}/{resultado.denominador}")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")

    def multiplicar_fracciones(self):
        """Multiplica las dos últimas fracciones del modelo."""
        try:
            resultado = self.model.multiplicacion()
            self.view.update_display(f"Resultado: {resultado.numerador}/{resultado.denominador}")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")

    def dividir_fracciones(self):
        """Divide las dos últimas fracciones del modelo."""
        try:
            resultado = self.model.division()
            self.view.update_display(f"Resultado: {resultado.numerador}/{resultado.denominador}")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")        

        except ValueError as e:
            self.view.update_display(f"Error: {e}")

    def view_fracciones(self):
        """Muestra todas las fracciones del modelo"""
        fracciones = self.model.get_fracciones()
        if fracciones:
            fraccion_texto = ", ".join([f"{f.numerador}/{f.denominador}" for f in fracciones])
            self.view.update_display(f"Fracciones: {fraccion_texto}")
        else:
            self.view.update_display("No hay fracciones en el modelo")   

    def simplificar_fraccion(self):
        """Simplifica la última fracción del modelo."""
        try:
            fraccion = self.model.get_fraccion(-1)
            if fraccion:
                resultado = fraccion.simplificar()
                self.model.reemplazar(resultado.numerador, resultado.denominador,-1)
                self.view.update_display(f"Fracción simplificada: {resultado.numerador}/{resultado.denominador}")
            else:
                self.view.update_display("No hay fracciones para simplificar")
        except ValueError as e:
            self.view.update_display(f"Error: {e}")

    def clear_fracciones(self):
        """Limpia todas las fracciones del modelo."""
        self.model.clear_fracciones()
        self.view.update_display("Fracciones limpiadas")     
        
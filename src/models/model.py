from .fraccion import Fraccion

class DataModel:
    def __init__(self):
        self.fracciones = [] # Lista para almacenar las fracciones

    def add_fraccion(self, numerador, denominador):
        try:
            fraccion = Fraccion(numerador, denominador)
            self.fracciones.append(fraccion)
        except ValueError as e:
            print(f"Error: {e}")

    def get_fracciones(self):
        return self.fracciones
    
    def get_fraccion(self, pos):
        try:
            return self.fracciones[pos]
        except IndexError:
            print("Error: Posición fuera de rango")
            return None
    
    def clear_fracciones(self):
        self.fracciones.clear()

    #Metodos para operaciones

    def suma(self):
        if len(self.fracciones) < 2:
            raise ValueError("Error: Se requieren al menos dos fracciones para sumar")
        else:
            fraccion1 = self.fracciones[-2]
            fraccion2 = self.fracciones[-1]
            resultado = fraccion1.suma(fraccion2)
        return resultado
    
    def resta(self):
        if len(self.fracciones) < 2:
            raise ValueError("Error: Se requieren al menos dos fracciones para restar")
        else:
            fraccion1 = self.fracciones[-2]
            fraccion2 = self.fracciones[-1]
            resultado = fraccion1.resta(fraccion2)
        return resultado
    
    def multiplicacion(self):
        if len(self.fracciones) < 2:
            raise ValueError("Error: Se requieren al menos dos fracciones para multiplicar")
        else:
            fraccion1 = self.fracciones[-2]
            fraccion2 = self.fracciones[-1]
            resultado = fraccion1.multiplicacion(fraccion2)
        return resultado
    
    def division(self):
        if len(self.fracciones) < 2:
            raise ValueError("Error: Se requieren al menos dos fracciones para dividir")
        else:
            fraccion1 = self.fracciones[-2]
            fraccion2 = self.fracciones[-1]
            resultado = fraccion1.division(fraccion2)
        return resultado
    
    def simplificar(self):
        if len(self.fracciones) < 1:
            raise ValueError("Error: Se requiere al menos una fracción para simplificar")
        else:
            fraccion = self.fracciones[-1]
            resultado = fraccion.simiplificar()
            self.fracciones[-1] = resultado

    def reemplazar(self, nuevo_numerador, nuevo_denominador,pos):  
        try:
            fraccion = self.fracciones[pos]
            fraccion.reemplazar(nuevo_numerador, nuevo_denominador,pos)
        except IndexError:
            print("Error: Posición fuera de rango")
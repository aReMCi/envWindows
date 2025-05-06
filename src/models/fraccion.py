import math

class Fraccion:
    def __init__ (self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def set_numerador(self, numerador):
        if numerador == 0:
            raise ValueError("El numerador no puede ser cero")
        self.numerador = numerador

    def get_numerador(self):
        return self.numerador
    
    def set_denominador(self, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.denominador = denominador
    
    def get_denominador(self):
        return self.denominador
    
    def suma(self, otra_fraccion):
        if self.denominador == otra_fraccion.denominador:
            return Fraccion(self.numerador + otra_fraccion.numerador, self.denominador)
        elif self.denominador == 0 or otra_fraccion.denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        else:
            mcm = math.lcm(self.denominador, otra_fraccion.denominador)
            nuevo_denominador = mcm
            nuevo_numerador = (self.numerador * mcm/self.denominador) + (otra_fraccion.numerador * mcm/otra_fraccion.denominador)
            return Fraccion(nuevo_numerador, nuevo_denominador)

    def resta(self, otra_fraccion):
        if self.denominador == otra_fraccion.denominador:
            return Fraccion(self.numerador - otra_fraccion.numerador, self.denominador)
        elif self.denominador == 0 or otra_fraccion.denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        else:
            mcm = math.lcm(self.denominador, otra_fraccion.denominador)
            nuevo_denominador = mcm
            nuevo_numerador = (self.numerador * mcm/self.denominador) - (otra_fraccion.numerador * mcm/otra_fraccion.denominador)
            return Fraccion(nuevo_numerador, nuevo_denominador)
        
    def multiplicacion(self, otra_fraccion):
        if self.denominador == 0 or otra_fraccion.denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        else:
            nuevo_numerador = self.numerador * otra_fraccion.numerador
            nuevo_denominador = self.denominador * otra_fraccion.denominador
            return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def division(self, otra_fraccion):
        if self.denominador == 0 or otra_fraccion.denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        else:
            nuevo_numerador = self.numerador * otra_fraccion.denominador
            nuevo_denominador = self.denominador * otra_fraccion.numerador
            return Fraccion(nuevo_numerador, nuevo_denominador)
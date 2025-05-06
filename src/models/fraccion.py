import math

class Fraccion:
    def __init__ (self, numerador, denominador):
        if denominador == 0: 
            raise ValueError("El denominador no puede ser cero")
        else:    
            self.numerador = numerador
            self.denominador = denominador

    @property
    def numerador(self):
        return self._numerador

    @numerador.setter
    def numerador(self, value):
        self._numerador = value

    @property
    def denominador(self):
        return self._denominador

    @denominador.setter
    def denominador(self, value):
        if value == 0:
            raise ValueError("El denominador no puede ser cero")
        self._denominador = value

    def reemplazar(self, nuevo_numerador, nuevo_denominador,pos):  
        if nuevo_denominador == 0: 
            raise ValueError("El denominador no puede ser cero")
        else:    
            self.numerador = nuevo_numerador
            self.denominador = nuevo_denominador

    
    def suma(self, otra_fraccion):
        if self.denominador == otra_fraccion.denominador:
            return Fraccion(self.numerador + otra_fraccion.numerador, self.denominador)
        else:
            mcm = math.lcm(self.denominador, otra_fraccion.denominador)
            nuevo_denominador = mcm
            nuevo_numerador = (self.numerador * (mcm//self.denominador)) + (otra_fraccion.numerador * (mcm//otra_fraccion.denominador))
            return Fraccion(nuevo_numerador, nuevo_denominador)

    def resta(self, otra_fraccion):
        if self.denominador == otra_fraccion.denominador:
            return Fraccion(self.numerador - otra_fraccion.numerador, self.denominador)
        else:
            mcm = math.lcm(self.denominador, otra_fraccion.denominador)
            nuevo_denominador = mcm
            nuevo_numerador = (self.numerador * (mcm//self.denominador)) - (otra_fraccion.numerador * (mcm//otra_fraccion.denominador))
            return Fraccion(nuevo_numerador, nuevo_denominador)
        
    def multiplicacion(self, otra_fraccion): 
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def division(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def simiplificar(self):
        mcd = math.gcd(self.numerador, self.denominador)
        return Fraccion(self.numerador // mcd, self.denominador // mcd)
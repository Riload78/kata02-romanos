from romannumber import *

class RomanNumber:
    def __init__(self,entrada):
        if isinstance(entrada, int): # Valida el tipo de la variable . Se puede usar type(valor)
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif isinstance(entrada, str) :
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError('Es una entrada errónea')
    @property  # Es un decoraador que lo que hace es transformat una función en una propiedad    
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)
        
    @property
    def simbolo(self):
        return self._simbolo
    
    @simbolo.setter
    def simbolo(self, entrada):
        self._simbolo = entrada
        self._numero = romano_a_entero(entrada)
        
        
    """ Métodos mágicos para aritmética """
    def __eq__(self, other):
        return self.numero == other.numero
    
    def __mul__(self,otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        resultado =  self.numero * otro.numero
        return RomanNumber(resultado)
    
    def __rmul__(self,otro):
        return self.__mul__(otro)
    
    def __repr__(self):
        return f"{self.romano} - {self.simbolo}"
    
    def __str__(self):
        return self.__repr__()
    
    
    """Hacer sumas, restas y divisiones"""

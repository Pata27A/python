print('*** ENCAPSULAMIENTO ARITMETICA ***')

class Aritmetica:
    def __init__(self, operando1, operando2):
        self._operando1 = operando1  # CORREGIDO
        self._operando2 = operando2

    @property
    def operando1(self):
        return self._operando1  # CORREGIDO
    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1  # CORREGIDO

    @property
    def operando2(self):
        return self._operando2
    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2  # CORREGIDO

    def suma(self):
        resultado = self._operando1 + self._operando2  # CORREGIDO
        print(f'La suma es de: {resultado}')

    def resta(self):
        resultado = self._operando1 - self._operando2  # CORREGIDO
        print(f'La Resta es de: {resultado}')
    
    def multiplicacion(self):
        resultado = self._operando1 * self._operando2  # CORREGIDO
        print(f'La Multiplicacion es de: {resultado}')

    def Division(self):
        if self._operando2 != 0:
            resultado = self._operando1 / self._operando2  # CORREGIDO
            print(f'El resultado de la division es {resultado}')
        else:
            print('No se puede dividir por cero')

if __name__ == '__main__':
    ari1 = Aritmetica(5, 7)
    ari1.suma()
    ari1.resta()
    ari1.multiplicacion()
    ari1.Division()
    
    #-----------------------------
    ari2 = Aritmetica(12, 16)
    ari2.suma()
    ari2.resta()
    ari2.multiplicacion()
    ari2.Division()

    print(f'Valor de operando 1: {ari1.operando1}')
    print(f'Valor de operando 2: {ari1.operando2}')

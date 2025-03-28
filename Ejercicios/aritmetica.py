class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operendo1 = operando1
        self.operando2 = operando2

    def suma(self):
        resultado = self.operendo1 + self.operando2
        print(f'La suma es de: {resultado}')

    def resta(self):
        resultado = self.operendo1 - self.operando2
        print(f'La Resta es de: {resultado}')
    
    def multiplicacion(self):
        resultado = self.operendo1 * self.operando2
        print(f'La MUltiplicacion es de: {resultado}')

    def Division(self):
        if self.operando2 != 0:
            resultado = self.operendo1 / self.operando2
            print(f'El resultado de la division es {resultado}')
        else:
            print('No se puede dividir por cero')


if __name__ == '__main__':
    ari1 = Aritmetica (5, 7)
    ari1.suma()
    ari1.resta()
    ari1.multiplicacion()
    ari1.Division()
    #-----------------------------
    ari2 = Aritmetica (12, 16)
    ari2.suma()
    ari2.resta()
    ari2.multiplicacion()
    ari2.Division()
class Calculadora:
    def __init__(self, operacion):
        self.operacion = operacion

    def calcular(self):
        try:
            resultado = eval(self.operacion)
            return resultado
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    operacion = input("Introduce tu operación: ")
    calculadora = Calculadora(operacion)
    resultado = calculadora.calcular()
    print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    main()

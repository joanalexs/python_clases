#Programa qu muestre la suma de dos numeros usando funciones 
num1=int (input("Ingrese el primer numero"))
num2=int (input("Ingrese el segundo numero"))

def sumar(numero1, numero2):
    suma= numero1 + numero2
    print(f"La suma de los numeros es: {suma}")

sumar(num1, num2)
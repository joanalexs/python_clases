num1=float(input("Ingrese un primer numero: "))
num2=float(input("Ingrese un segundo numero: "))
if num1 > num2:
    print(f"El numero mayor es: {num1}")
elif num2 > num1:
    print(f"El numero mayor es: {num2}")
else:
    print("Los numeros son iguales, porfavor ingrese numeros distintos")
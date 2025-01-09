n1 = int(input("Introduzca el primer número. "))
n2 = int(input("Introduzca el segundo número. "))
if (n1>n2):
    print("El número", n1, "es mayor que", n2)
else:
    if (n1<n2):
        print("El número", n2, "es mayor que", n1)
    else:
        print("Los números son iguales.")
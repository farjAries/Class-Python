n1 = int(input("Qual o valor do primeiro? "))
n2 = int(input("Qual o valor do primeiro? "))
n3 = int(input("Qual o valor do primeiro? "))


if (n1 + n2 ) > n3:
    print("NAo é um triangulo")
    
else:
    if n1 == n2 == n3:
        resultado =  "EQUILATERO"
    elif n1 == n2 or n1 == n2 or n2 == n3:
        resultado = "ISOSCELES"
    else:
        resultado =  "ESCALENO"
    print( f"o Triangulo é um {resultado}")

iteraciones = int(raw_input("Numero de Iteraciones: "))
cont = 0
resultado = ""

if iteraciones > 0:
    fibonacci1 = 0
    fibonacci2 = 1

    while cont < iteraciones:
        fibonacci1 = fibonacci1 + fibonacci2
        if cont == 0:
            resultado = resultado + "" + format(fibonacci1)
        else:
            resultado = resultado + ", " + format(fibonacci1)

        cont = cont + 1
        if cont < iteraciones:
            fibonacci2 = fibonacci1 + fibonacci2
            resultado = resultado + ", " + format(fibonacci2)
            cont = cont + 1

print(resultado)
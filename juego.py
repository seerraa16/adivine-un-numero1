def menu():
    print("Adivine un numero")
    print("nivel debutante\nnivel aficionado\nnivel profesional\nnivel clase mundial")
    modo = input("Escoja un nivel: ")
    print(modo)
    if modo == "nivel debutante":
        juego(0, 100, random = numeroaleatorio(0,100))
    elif modo == "nivel aficionado":
        juego(0, 1000, random = numeroaleatorio(0,1000))
    elif modo == "nivel profesional":
        juego(0, 1000000, random = numeroaleatorio(0,1000000))
    elif modo == "nivel clase mundial":
        juego(0, 1000000000000, random = numeroaleatorio(0,1000000000000))
    else:
        return menu()
def numeroaleatorio(minimo, maximo):
    import random
    naleatorio = random.randint(minimo, maximo)
    return naleatorio
def juego(minimo, maximo, random, ):
    ayuda = 0
    random = numeroaleatorio(minimo, maximo)
    numero = input("Introduzca numero entre " + str(minimo) + " y " + str(maximo) + ": ")
    numero = int(numero)
    print(numero)
    while True:
        if numero == random:
            print("has ganado")
            ayuda+=1
            victoria(ayuda)
        elif numero > random:
            print("El numero es mas pequeño")
            ayuda+=1
            if ayuda == 7:
                cuestionayuda(minimo, maximo, random)
            elif ayuda == 10
                maximointentos()
        elif numero < random:
            print("El numero es mas alto")
            ayuda+=1
            if ayuda == 7:
                cuestionayuda(minimo, maximo, random)
            elif ayuda == 10
                maximointentos()

        else:
            return juego(minimo, maximo, random)
def cuestionayuda(minimo, maximo, naleatorio):
    respuesta = input("¿Quiere usted ayuda?")
    print(respuesta)
    if respuesta == "si":
        print("El numero se comprende entre",minimo, "y", maximo) 
    elif respuesta == "no":
        print("No hay ayuda") 
        return juego()
    else:
        return cuestionayuda()
def maximointentos(minimo, maximo):
    print("Has perdido. Alcanzaste el numero maximo de intentos.")
def victoria(ayuda):
    print("has ganado en", ayuda, "intentos.")
    Nombre = input ("Ingrese su nombre: ")
    pregunta2 = input(Nombre, ", ¿Desea volver a jugar?")
    print(pregunta2)
    if pregunta2 == "si":
        lista=[]
        lista.append(Nombre)
        print (lista)
    else:
        print("Gracias por jugar")

        


menu()
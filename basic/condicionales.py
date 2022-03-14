while True:
    menu = """ Podemos utilizar los dos tipos de escritura mas comunes
        con el triple de comillas dobles para imprimir en pantalla varias
    filas de texto, respetando los espacios de escritura
            1 - Mex
            2 - Col

        🎂 emojis con teclas windows + .
    Escribe un numero (0 para salir): 

    """

    option = int(input(menu))

        
    if option != 0:
        print("Usted escribio: ",option)
    elif option == 0:
        print("Bye") 
        break
    else:       # Observe que lleva dos puntos al final, ademas de los indentados
        print("Doesn't exist Invalid option with int")


edad = int(input("Escribe tu edad "))
if edad > 17: # despues de dos puntes se deja un indentado de 4 espacios
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad")
    pass    # pass es una palabra reservada se interpreta como: 
            # el codigo queda pendiente para despues

### #### ### ### ###

numero = int(input('Escribe un numero: '))
if numero > 5:
    print("es mayor a 5")
elif numero == 5:       # else if
    print(numero , "es igual a 5")  # deja un espacio automatico entre numero y el string
else:
    print('es menor a 5')


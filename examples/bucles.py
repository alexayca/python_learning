# Potencias de 2


def run_while():
    print("\n\nCiclo While")
    LIMITE = 1000     # constante
    i = 0
    potencia_2 = 2**i
    while potencia_2 < LIMITE:
        print('2 ^' + str(i) + ' = ' + str(potencia_2))  # con + solo concatena strings
        i = i+1       # i += 1
        potencia_2 = 2**i


def run_for():
    print("\n\nCiclo For")
    print(range(9))         # rango de 0 - 8
    print(list(range(9)))   # lista de 0 - 8
    for i in range(9):      # range(start, stop, step) -> (start, stop) -> (stop)
        print('2 ^' + str(i) + ' = ' + str(2**i))


def recorrer_string():
    nombre = input("Escribe tu nombre: ")
    for letra in nombre:    # obtiene en automatico la longitud de la cadena nombre, el iterador es letra
        print(letra.upper())


def run_break_continue():
    # Mostrar numeros pares
    for i in range(100):
        if i %2 !=0:
            continue    # Salta la vuelta del ciclo For
        print(i)
    # Lista los numeros del 1 - 100, con break
    for i in range(100):
        if i == 64:
            break    # Sale del ciclo For
        print(i)


if __name__ == "__main__":
    run_while()
    run_for()
    recorrer_string()
    run_break_continue()
    
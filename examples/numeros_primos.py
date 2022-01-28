# Los números primos son todos los números naturales mayores a que 
# tienen exactamente dos factores: la unidad y ellos mismos
import random


def es_primo(number):
    # metodo ineficiente al recorrer todo el rango de numeros
    contador_divisores = 0
    for i in range(1, number+1):
        if i==1 or i==number:      # excluimos el 1 y el numero introducido
            continue               # Salta la vuelta del ciclo For
        if number % i ==0:  # si el residuo es cero existe otro divisor (al menos 3)
            contador_divisores +=1
    if contador_divisores==0:     # el numero es primo al tener máximo dos divisores
        return True
    else:
        return False


def do_teorema_wilson(p):
    # Si p es un número primo, entonces (p − 1)! ≡ -1 (mod p)
    # Este metodo requiere bastantes recursos en numeros grandes, debido al factorial
    #           (n-1)! + 1 
    factorial = do_factorial(p-1)+1
    residuo = factorial%p
    if residuo==0:
        return True
    else:
        return False


def do_factorial(n):
    # n! = n(n-1)!      -> recursivo
    if n==0:
        return 1
    return (n*do_factorial(n-1))


# Prueba de primalidad
def run():
    numero = int(input ('Escribe un numero: '))
    if do_teorema_wilson(numero):
        print('SI es primo (Wilson)')
    if es_primo(numero):
        print('SI es primo')
    else:
        print('NO es primo')

# QED = Quod erat demonstrandum



if __name__ == '__main__':
    run()
    #print(do_factorial(5))

   
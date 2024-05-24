def borrar_pantalla():
    """Borra la pantalla.
    """
    system("cls")

def pausar(): 
    """Pausa la iteracion para mostrar un dato en pantalla.
    """
    system("pause")

def validar_opcion (option: int)->int:
    """valida que el usuario ingrese una opcion correcta

    Args:
        option (int): opcion ingresada

    Returns:
        int: opcion validada
    """
    while (not(option.isdigit())) or (int(option) != 1 and int(option) != 2 and int(option) != 3 and int(option) != 4 and int(option) != 5): 
        option = input("Error vuelva a ingresar una opción: ")

    option = int(option)
    return(option)

def validar_operacion (operation: str)->str:
    """valida la opcion de operación ingresada

    Args:
        operation (str): opcion de operación ingresada

    Returns:
        str: opcion de operación validada
    """
    while ((operation.lower()).isdigit()) or (operation.lower() != "a" and operation.lower() != "b" and operation.lower() != "c" and operation.lower() != "d" and operation.lower() != "e"): 
        operation = input("Error, vuelva a ingresar una operación: ")
    return operation.lower()

def validar_operando (operando: int)->int:
    """valida los operandos ingresados

    Args:
        operando (int): operando 

    Returns:
        int: operando validado
    """
    while not(operando.isdigit()): 
        operando = input("Ingrese A: ")
    operando = int(operando)

    return operando

def menu_opciones (a: int, b: int) ->int:
    """Menu de opciones de la calculadora.

    Args:
        a (int): primero operando
        b (int): segundo operando

    Returns:
        int: La opción ingresada por el usuario.
    """
    borrar_pantalla()

    print("--MENU DE OPCIONES--")
    print (f"1 - Ingresar 1er operando A={a}")
    print (f"2 - Ingresar 2do operando B={b}")
    print ("3 - Calcular todas las operaciones")
    print ("4 - Informar resultados")
    print ("5 - Salir")

    opcion = input("Ingrese una opción: ")
    opcion = validar_opcion(opcion)

    return opcion

def menu_operaciones () -> str: 
    """Manu de operaciones matemáticas de la calculadora.

    Returns:
        str: La opción ingresada por el usuario.
    """
    borrar_pantalla()

    print("--MENU DE OPERACIONES--")
    print ("A - Calcular suma")
    print ("B - Calcular la resta")
    print ("C - Calcular el producto")
    print ("D - Calcular la división")
    print ("E - Calcular el factorial de A")

    operacion = input("Ingrese una opción: ")

    operacion = validar_operacion (operacion)
    return operacion

def error_no_ingreso_datos (operando_a: str, operando_b: str) -> bool:
    """Controla que el usuario haya ingresado valores para los operandos.

    Args:
        operando_a (str): primer operando
        operando_b (str): segundo operando

    Returns:
        bool: Si el usuario no ingreso nada, la función devuelve True. Si ingreso devuelve False. 
    """
    if operando_a == "X" or operando_b == "Y":
        return True
    else: 
        return False

def error_no_realiza_operacion (operacion_local: int) -> bool:
    """Controla que el usuario haya realizado una operación antes de mostrarla en pantalla.

    Args:
        operacion_local (int): bandera de control. 

    Returns:
        bool: Si la bandera es 0 la función devulve True. Si cambió su valor es False. 
    """
    if operacion_local == 0:
        return True
    else: 
        return False
    
def muestra_resultados (operacion: str, suma: int, resta: int, producto: int, division: int, factorial: int)-> str: 
    """Muestra los resultados de la operación ingresada

    Args:
        operacion (str): operación elegida por el usuario
        suma (int): operación suma
        resta (int): operación resta
        producto (int): operación producto
        division (int): operación division
        factorial (int): operación factorial

    Returns:
        str: muestra por pantalla la operacion, los operandos y el resultado de la operación
    """
    print ("--------------------------------------")
    match operacion:
        case "a": 
            print(f"El resultado de A+B es: {suma}")
        case "b":
            print(f"El resultado de A-B es: {resta}")
        case "c":
            print(f"El resultado de A*B es: {producto}")
        case "d":
            print(f"El resultado de A/B es: {division}")                        
        case "e":
            print(f"El resultado de A! es: {factorial}")
    print ("--------------------------------------")

def salir ()-> bool:
    """confirma si el usuario desea abandonar el programa

    Returns:
        bool: devuelve True si desea salir o False si no desea salir
    """
    salir = input("Confirma que desea salir? Ingresese 'SI' o 'NO' ")

    while (salir.isdigit()) or (salir.lower() != "si" and salir.lower() != "no"):
        salir = input("Opción incorrecta. Confirma que desea salir? ")

    if salir.lower() == "si":
        print("---CALCULADORA FINALIZADA---")
        return True
    else: 
        return False


#----------- PROGRAMA PRINCIPAL-------------
from os import system
from Operaciones import *

a = "X"
b = "Y"

suma = 0
resta = 0
producto = 0
division = 0
factorial = 0
operacion = " "

while True:

    match menu_opciones(a,b): 
        case 1: 
            a = input("Ingrese A: ")
            a = validar_operando(a)
        case 2: 
            b = input("Ingrese B: ")
            b = validar_operando(b)
        case 3: 
            if error_no_ingreso_datos (a,b):
                print("No se puede realizar la operación sin ingresar ambos operandos.")
            else:    
                while True:
                    operacion = menu_operaciones ()  
                    match operacion:
                        case "a": 
                            suma = funcion_suma (a,b)
                        case "b":
                            resta = funcion_resta (a,b)
                        case "c":
                            producto = funcion_producto (a,b)
                        case "d":
                            if b == 0:
                                print("No se puede dividir por cero")
                                pausar()
                                continue
                            else: 
                                division = funcion_division (a,b)                         
                        case "e":
                            factorial = funcion_factorial (a)
                    print ("Operacion realizada")
                    break
        case 4: 
            if error_no_ingreso_datos (a,b):
                print("No se pueden informar resultados sin ingresar ambos operandos.")
            elif error_no_realiza_operacion (operacion): 
                print("No se pueden informar resultados sin realizar una operación.")
            else:
                muestra_resultados (operacion, suma, resta, producto, division, factorial)
                a = "X"
                b = "Y"

                suma = 0
                resta = 0
                producto = 0
                division = 0
                factorial = 0
                operacion = " "
        case 5: 
            if salir ():
                break
            else: 
                continue
    pausar()


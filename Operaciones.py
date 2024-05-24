def funcion_suma (operando_a: int, operando_b: int) -> int:
    """realiza la operación de suma

    Args:
        operando_a (int): primer operando
        operando_b (int): segundo operando

    Returns:
        int: suma de ambos operandos
    """
    suma = operando_a + operando_b
    return suma

def funcion_resta (operando_a: int, operando_b: int) -> int:
    """realiza la operación de resta

    Args:
        operando_a (int): primer operando
        operando_b (int): segundo operando

    Returns:
        int: resta de ambos operandos
    """
    resta = operando_a - operando_b
    return resta

def funcion_division (operando_a: int, operando_b: int) -> float:
    """realiza la operación de divisón

    Args:
        operando_a (int): primer operando
        operando_b (int): segundo operando

    Returns:
        float: división de ambos operandos
    """
    division = operando_a / operando_b
    return division

def funcion_producto (operando_a: int, operando_b: int) -> int:
    """realiza la operación de producto

    Args:
        operando_a (int): primer operando
        operando_b (int): segundo operando

    Returns:
        int: producto de ambos operandos
    """
    producto = operando_a * operando_b
    return producto

def funcion_factorial (operando_a: int) -> int:
    """realiza el factorial del primer operando

    Args:
        operando_a (int): primer operando

    Returns:
        int: factorial del primer operando
    """
    factorial = 1
    
    for i in range (1, operando_a+1):
        factorial *= i

    return factorial
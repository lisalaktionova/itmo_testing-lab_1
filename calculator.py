def add(a: float, b: float) -> float:
    """Сложение двух чисел"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание b из a"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение двух чисел"""
    return a * b


def divide(a: float, b: float) -> float:
    """Деление a на b"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def power(a: float, b: int) -> float:
    """Возведение числа a в степень b"""
    return a ** b


import cmath


def get_discriminant(a: [float, int] = 0, b: [float, int] = 0, c: [float, int] = 0) -> [float, int]:
    """
    Return discriminant
    """
    return b ** 2 - 4 * a * c


def get_coefficient(coeff_name: str) -> float:
    """
    Takes and check coefficient
    """
    done = False
    while not done:
        coefficient = input(f'Please enter the value of the coefficient {coeff_name}')
        if coeff_name == 'a' and coefficient == 0:
            print('a - must be not 0')
            continue
        try:
            coefficient = float(coefficient)
            done = True
        except ValueError:
            print('Please enter valid value (number positive/negative number)')
    return coefficient


def create_equation() -> tuple:
    """
    Return equation data
    """
    a = get_coefficient('a')
    b = get_coefficient('b')
    c = get_coefficient('c')
    return a, b, c


def roots_of_equation() -> tuple:
    """
    Equation solution
    """
    coefficient_a, coefficient_b, coefficient_c = create_equation()
    discriminant = get_discriminant(coefficient_a, coefficient_b, coefficient_c)
    if discriminant > 0:
        x1 = round((-coefficient_b + discriminant ** 0.5) / (2 * coefficient_a), 3)
        x2 = round((-coefficient_b - discriminant ** 0.5) / (2 * coefficient_a), 3)
    elif discriminant == 0:
        x1 = x2 = round((-coefficient_b) / (2 * coefficient_a), 3)
    else:
        discriminant = cmath.sqrt(discriminant)
        real = round((-coefficient_b) / (2 * coefficient_a), 3)
        imag = round(discriminant.imag / (2 * coefficient_a), 3)
        x1 = f'{real} + j{imag}'
        x2 = f'{real} - j{imag}'
    return x1, x2


def main():
    """
    Information about equation
    """
    print('The quadratic equation has the following form:')
    print('a*x^2+b*x+c=0')
    x1, x2 = roots_of_equation()
    print('The result of solving the equation')
    print(f'x1 = {x1}, x2 = {x2}')
    return True


if __name__ == '__main__':
    main()

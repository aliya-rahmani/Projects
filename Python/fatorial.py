def fatorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fatorial(number-1)

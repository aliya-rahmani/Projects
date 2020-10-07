num = int(input('Input number '))

memoArr = [None] * num


def factorial(number):
    if number < 0:
        print('No factorial for negative numbers')
        return -1
    elif number == 0:
        return 1
    if memoArr[number - 1] is None:
        memoArr[number - 1] = number * factorial(number - 1)

    print(memoArr)
    return memoArr[number - 1]


print(factorial(num))

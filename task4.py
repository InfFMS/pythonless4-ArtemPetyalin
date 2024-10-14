# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

a = int(input())
b = int(input())

def NOD(a, b):

    if a == b:
        return a

    while a != b:

        if a > b:
            a -= b

        if b > a:
            b -= a

    return a
print('НОД: ' + str(NOD(a, b)))

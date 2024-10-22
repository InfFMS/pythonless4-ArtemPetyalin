# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

a = int(input())

def rome_nums(a):
    s = ''

    if a < 1 or a > 3999:
        return('error')

    while a // 1000 != 0:
        s = s + 'M'
        a -= 1000

    while a // 900 != 0:
        s = s + 'CM'
        a -= 900

    while a // 500 != 0:
        s = s + 'D'
        a -= 500

    while a // 400 != 0:
        s = s + 'CD'
        a -= 400

    while a // 100 != 0:
        s = s + 'C'
        a -= 100

    while a // 90 != 0:
        s = s + 'XC'
        a -= 90


    while a // 50 != 0:
        s = s + 'L'
        a -= 50

    while a // 40 != 0:
        s = s + 'XL'
        a -= 40

    while a // 10 != 0:
        s = s + 'X'
        a -= 10

    while a // 9 != 0:
        s = s + 'IX'
        a -= 9

    while a // 5 != 0:
        s = s + 'V'
        a -= 5

    while a // 4 != 0:
        s = s + 'IV'
        a -= 4

    while a // 1 != 0:
        s = s + 'I'
        a -= 1

    return s

print(rome_nums(a))
# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.

num = int(input())
from_base = int(input())
to_base = int(input())

def convert_base(a, b, c):
    a_dec = 0
    a_str = str(a)
    #print(a_str)

    for i in range(len(a_str)):
        a_dec = a_dec + int(a_str[-i - 1]) * (b ** i)


    a_new = ''
    razr = 1

    while c ** razr < a_dec:
        razr += 1

    print(razr)

    for j in range(razr):
        a_new = a_new + str(a_dec // (c ** (razr - j)))
        print(a_dec // (c ** (razr - j)))
        a_dec -= a_dec // c ** (razr - j)

    return a_new

print(convert_base(num, from_base, to_base))

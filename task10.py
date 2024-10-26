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

num = input()
from_base = int(input())
to_base = int(input())

def convert_base(a, b, c):
    a_dec = 0
    a_str = str(a)
    #print(a_str)

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    #перевод числа в десятичную систему

    for i in range(len(a_str)):

        for j in range(len(alphabet)):

            if a_str[i] == alphabet[j]: #если цифра больше 9
                a_dec += (j + 10) * b ** (len(a_str) - i - 1)

                if j + 10 >= b:
                    return 'error' #проверка, меньше ли цифра основания системы счисления
                    break

                break

        else:
            a_dec += int(a_str[i]) * b ** (len(a_str) - i - 1)

            if int(a_str[i]) >= b:
                return 'error' #проверка, меньше ли цифра основания системы счисления
                break

        print(a_dec)


    #перевод в требуемую систему счисления
    a_new = ''
    razr = 1

    while c ** razr < a_dec:
        razr += 1

    for j in range(1, razr + 1):

        if a_dec // c ** (razr - j) >= 10 and c > 10:
            a_new = a_new + alphabet[a_dec // c ** (razr - j) - 10]

        else:
            a_new = a_new + str(a_dec // c ** (razr - j))

        a_dec = a_dec - (a_dec // c ** (razr - j) * c ** (razr - j))

    return a_new

print(convert_base(num, from_base, to_base))

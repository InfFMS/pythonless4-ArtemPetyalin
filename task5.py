# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.
a = int(input())
s = str(a)


def reverse(s):
    answer = ''

    for i in range(1, len(s) + 1):
        answer = answer + s[-i]

    return answer

print(reverse(s))

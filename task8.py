# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

N = int(input())

def razlogator(a):

    if a == 1:
        return 1

    divs = []
    i = 2

    while a != 1:

        if a % i == 0:
            a = a // i
            divs.append(i)
            i = 2

        elif a % i != 0:
            i += 1

    answer = ''

    for j in range(len(divs)):
        answer = answer + str(divs[j]) + '*'

    answer = answer[:-1]

    return answer

print(razlogator(N))
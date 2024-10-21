# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

a = int(input())

def razlogator(b):
    divs = []

    def dividors(c):
        i = 2

        while c % i != 0 and i < c:
            i += 1

        if c != 1:
            divs.append(i)

        c = c / i

        if c != 1:
            dividors(c)

    if b >= 2:
        dividors(b)
        s = ''

        for j in range(len(divs)):
            s = s + str(divs[j]) + '*'

        s = s[:-1]
        print(s)

    else:
        print('error')





razlogator(a)
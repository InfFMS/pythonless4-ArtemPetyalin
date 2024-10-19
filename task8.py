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

        for i in range(2, int(c ** 0.5)):

            if c % i == 0:
                divs.append(i)
                dividors(c / i)
                c = c / i
                print(i)

    dividors(b)

    s = ''

    for j in range(len(divs)):
        s = s + str(divs[j]) + '*'

    s = s[:-2]
    print(s)

razlogator(a)
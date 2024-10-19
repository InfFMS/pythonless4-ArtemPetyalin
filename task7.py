# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
a = int(input())
b = int(input())
c = int(input())

def is_valid_triangle(side1, side2, side3):

    if max(side1, side2, side3) < side1 + side2 + side3 - max(side1, side2, side3):
        return True

    else:
        return False

print(is_valid_triangle(a, b, c))

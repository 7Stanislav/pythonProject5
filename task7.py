"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

def my_func(n, my_num, my_sum, count):
    if my_sum < my_num:
        my_sum += count
        count += 1
        return my_func(n, my_num, my_sum, count)
    else:
        print(f"Для n = {n}\nверно равенство: {my_sum} = {n}({n}+1)/2")

n = int(input("Введите натуральное число: "))
my_num = n * (n + 1) / 2
my_sum = 0
count = 0
my_func(n, my_num, my_sum, count)

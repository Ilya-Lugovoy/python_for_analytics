# Задача 28: Напишите рекурсивную функцию sum(a, b)
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

a = 5
b = 3
n = 0

def find_numb(numb,n):
        if numb == 0:
            return n
        return find_numb(numb-1, n+1)

def sum(a,b,n):
    return find_numb(a, n) + find_numb(b, n)

print(sum(a, b, n))
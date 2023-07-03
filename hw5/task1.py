# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))

def rec_1(a, b, degree_numb=1):
    if b == 0:
        return degree_numb
    b -= 1
    return rec_1(a, b, degree_numb*a)

print(rec_1(a, b))

# def func_2(a, b, degree_numb=1):
#     while b != 0:
#         degree_numb *= a
#         b -= 1
#     return degree_numb

# print(func_2(a, b))
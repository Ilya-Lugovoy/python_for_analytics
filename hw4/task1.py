# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями)
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

n = int(input("Enter number of elements from the first set: "))
m = int(input("Enter number of elements from the second set: "))

set1 = set()
set2 = set()

print("Enter elements from the first set: ")
for i in range(n):
    num = int(input())
    set1.add(num)

print("Enter elements from the second set: ")
for i in range(m):
    num = int(input())
    set2.add(num)

common_elements = set1.intersection(set2)
sorted_elements = sorted(common_elements)

print(f'-> {sorted_elements}')
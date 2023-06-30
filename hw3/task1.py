# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Enter number of elements in the array: '))
x = int(input('Enter the number that we find: '))

list = [i for i in range(1, n+1)]
print(*list)
print(x)

count = 0
for i in list:
    if i == x:
        count += 1
print(f'-> {count}')
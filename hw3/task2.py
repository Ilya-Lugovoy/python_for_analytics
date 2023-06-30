# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

n = int(input('Enter number of elements in the array: '))
x = int(input('Enter the number that we are aiming for: '))

list = [i for i in range(1, n+1)]
print(*list)
print(x)

min_diff = float('inf')
closest_element = None

for i in range(n):
    diff = abs(list[i] - x)
    if diff < min_diff:
        min_diff = diff
        closest_element = list[i]

print(f'-> {closest_element}')
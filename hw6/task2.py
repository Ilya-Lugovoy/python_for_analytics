# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

numbers = [-10, 3, -2, 7, 40]
indices = [0, 0]
indices[0] = int(input('Enter where to start indices range: '))
indices[1] = int(input('Enter up to where indices: '))
indices = tuple(indices)

for i in range(indices[0], indices[1] + 1):
    print(numbers[i])
    i+=1
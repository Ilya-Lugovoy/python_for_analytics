# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику
# Она растёт на круглой грядке, причём кусты высажены только по окружности
# Таким образом, у каждого куста есть ровно два соседних
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки

list_1 = []
for i in range(1, 5):
    n = int(input(f'Сколько ягод на кусте {i}: '))
    list_1.append(n)

print(list_1)

def max_1(list):
    max = list[0] + list[1] + list[2]
    if max < list[1] + list[2] + list[3]:
        max = list[1] + list[2] + list[3]
    if max < list[2] + list[3] + list[0]:
        max = list[2] + list[3] + list[0]
    if max < list[3] + list[0] + list[1]:
        max = list[1] + list[0] + list[1]

    return max

print(max_1(list_1))
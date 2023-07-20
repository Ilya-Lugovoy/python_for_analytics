# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

x = y = 1

def print_operation_table(operation, num_rows=6, num_columns=6):
    global x, y
    while y <= num_columns:
        x = 1
        list = [None] * 6
        for x in range(1, num_rows+1):
            list[x-1] = operation(x,y)
            if x == num_rows:
                y += 1
        print(list)

print_operation_table(lambda x, y: x * y)
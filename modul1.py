# import random
# def generate_list(len_list):
#     list_res = []
#     for i in range(len_list):
#         list_res.append(random.randint(1, 10))
    
#     return list_res

# def find_minus_list(len_1, len_2):
#     list_end = []
#     for item in len_1:
#         if item not in len_2:
#             list_end.append(item)

#     return list_end

# len_1 = int(input('Enter len of list 1: '))
# list_1 = generate_list(len_1)
# print(list_1)
# len_2 = int(input('Enter len of list 2: '))
# list_2 = generate_list(len_2)
# print(list_2)

# list_end = find_minus_list(list_1, list_2)
# print(list_end)

# list_2 = [int(input(f'Введите {i+1} эллемент второго списка')) for i in range(num2)]
# Задача 2: Найдите сумму цифр трехзначного числа

n = int(input('Enter a three-digit number: '))
sum = n//100 + n//10 % 10 + n%10
print(sum)
# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

ticket = int(input("Введите номер вашего билета: "))

n1 = ticket//1000
sum1 = n1//100 + n1//10 % 10 + n1%10
print(sum1)

n2 = ticket
sum2 = n2//100%10 + n2//10%10 + n2%10
print(sum2)

if sum1 == sum2:
    print("Поздравляю! Ваш билет счастливый ))")
else:
    print('Ваш билет не счастливый (())')
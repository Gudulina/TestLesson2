# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:   6782 -> 23
#           0.56 -> 11

num = float (input('Введите число: '))

# def summa (num):
#     if num > 0:
#         sum = sum + num % 10
#         num /= 10
#     return sum
sum = 0
while num > 0:
    sum = sum + num % 10
    num /= 10
print('Сумма цифр = ', "{:.0f}".format(sum))

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:   6782 -> 23
#           0.56 -> 11

num = (input('Введите число: '))
sum = 0
for i in num:
    if i != '.':
        sum += int(i)
print('Сумма цифр = ', sum)

# def summa (num):
#     if num > 0:
#         sum = sum + num % 10
#         num /= 10
#     return sum
# sum = 0
# while num > 0:
#     sum = sum + num % 10
#     num /= 10
# print('Сумма цифр = ', "{:.0f}".format(sum))

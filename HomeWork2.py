# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:   6782 -> 23
#           0.56 -> 11

# num = (input('Введите число: '))
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print('Сумма цифр = ', sum)


# 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число: '))
# set = 1
# for i in range(1, num+1):
#     set *= i
#     print(set, end=' ')

# 3. Задайте список из n чисел последовательности (1+1/N)^n и выведите на экран их сумму.

# n = int (input('Введите число: '))
# sum = 0 
# for i in range(1, n + 1): 
#     sum += ((1 + 1 / i)**i) 
# print("%.2f" % sum)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементво на указанных поизциях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("N = "))

a = [i for i in range(-n, n+1)]
print(a)

mult = 1
with open('file.txt') as file:
    for i in file:
        if int(i) < n:
            mult *= a[int(i)]
        else: mult *= 1
print(mult)


# for i in range(number):
# numbers.append(randint(number * -1, number + 1))

# 5. Реализуйте алгоритм перемешивания списка.

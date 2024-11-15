# Task 1
# Лямбда-функция для добавления 15
add_15 = lambda x: x + 15

num = int(input("Input: "))

print("Output:", add_15(num))

# Лямбда-функция для умножения
multiply = lambda x, y: x * y

x, y = map(int, input("Input: ").split())

print("Output:", multiply(x, y))

# Список целых чисел
numbers = [78, 2, 13, 46, 5, 61, 74, 81, 94, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Список четных чисел:", even_numbers)
print("Список нечетных чисел:", odd_numbers)

import datetime

# Лямбда-функция для получения текущего времени
current_datetime = lambda: datetime.datetime.now()

now = current_datetime()

print(now)  # Полный формат
print(now.year)  # Год
print(now.month)  # Месяц
print(now.day)  # День
print(now.time())  # Время

# Task 3
numbers = [147, 241, 39, 5, 778, 18, 0, 10]

even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd_count = len(list(filter(lambda x: x % 2 != 0, numbers)))

print("Список целых чисел:", numbers)
print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)

#Task 1 Moduls
import random

matrix = [[random.randint(0, 100) for _ in range(10)] for _ in range(10)]

print("Массив 10x10:")
for row in matrix:
    print(row)

min_value = min(min(row) for row in matrix)
max_value = max(max(row) for row in matrix)

print("\nМинимальное значение:", min_value)
print("Максимальное значение:", max_value)


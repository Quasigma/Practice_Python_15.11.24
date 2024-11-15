# total_sum = 0

# while True:
#     number = int(input())
#     if number == 0:
#         break
    
#     total_sum += number
# print(total_sum)


# start = int(input("Введите первое число: "))
# end = int(input("Введите второе число: "))
# if start > end:
#     start, end = end, start 
# print("Все числа в диапазоне:")
# for i in range(start, end + 1):
#     print(i, end=" ")
# print()
# print("Нечетные числа в диапазоне:")
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         print(i, end=" ")
# print()
# print("Четные числа в диапазоне:")
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(i, end=" ")
# print()
# print("Все числа в диапазоне в порядке убывания:")
# for i in range(end, start - 1, -1):
#     print(i, end=" ")
# print()


# Треугольник
# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# while True:
#     number = int(input("Введите целое число: "))

#     if number < 10:
#         continue
#     elif number > 100:
#         break
#     else:
#         print(number)


print("Совершенные числа от 1 до 100:")
for num in range(1, 101):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(num)


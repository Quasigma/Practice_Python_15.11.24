# a = int(input())
# b = int(input())
# c = int(input())
# if (a+b)>c:
#     print("True")
# else:
#     print("False")


# a = int(input())
# if (a % 2) == 0:
#     print("True")
# else:
#     print("False")

# n = int(input())
# if n > 0:
#     n += 1
#     print(n)
# if n < 0:
#     n -=2
#     print(n)
# if n == 0:
#     n = 10
#     print(n)

# x = int(input())
# if (-15 < x <= 12) or (14 < x < 17) or (19 <= x):
#     print("True")
# else:
#     print("False")

n = int(input())
if n % 10 == 1 and n % 100 != 11:
    suffix = "программист"
if n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
    suffix = "программиста"
else:
    suffix = "программистов"
print(f"{n} {suffix}")

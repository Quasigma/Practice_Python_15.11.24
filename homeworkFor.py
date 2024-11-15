# Task 2 
n = int(input("Enter a natural number (n ≤ 9): "))

if 1 <= n <= 9:
    for i in range(1, n + 1):
        print("".join(str(x) for x in range(1, i + 1)))
else:
    print("Invalid input. Please enter a number between 1 and 9.")

#Task 2
N = int(input())
i = 1
while i * i <= N:
    print(i * i, end=" ")
    i += 1

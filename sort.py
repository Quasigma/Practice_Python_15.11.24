# Task 1
def IsAscending(a):
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            return "No"
    return "Yes"

a = list(map(int, input("Input: ").split()))

print("Output:", IsAscending(a))

# Task 2
def KthAppearance(A, a, k):
    count = 0 
    for i in range(len(A)):
        if A[i] == a:
            count += 1
            if count == k:
                return i
    return -1  

A = list(map(int, input("Введите список чисел: ").split()))
a, k = map(int, input("Введите число a и k через пробел: ").split())
print("Output:", KthAppearance(A, a, k))

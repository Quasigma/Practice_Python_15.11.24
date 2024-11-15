add_three_calls = 0
def add_three(number):
    global add_three_calls
    print(f'Returning {number +3 }')
    add_three_calls += 1
    return number + 3

a = 3
v = add_three(a)
print(v)
print(add_three_calls)
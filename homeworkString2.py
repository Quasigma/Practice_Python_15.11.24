# Dictionary 
my_dict = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5
}
keys = list(my_dict.keys())
my_dict[keys[0]], my_dict[keys[-1]] = my_dict[keys[-1]], my_dict[keys[0]]

del my_dict[keys[1]]
my_dict["new_key"] = "new_value"
print(my_dict)

# Натуральные числа(не уверен что правильно сделал)
numbers = [4, 5, 4, 6, 4, 5, 7, 8, 4, 5, 8, 8]

counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1

result_set = set()

for number, count in counts.items():
    for i in range(1, count + 1):
        if i == 1:
            result_set.add(number)
        else:
            result_set.add(str(number) * i) 

print(result_set)

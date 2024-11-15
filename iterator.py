# def mygenerator(lst):
#     n=0
#     while True:
#         if lst[n]%2==0:
#             yield lst [n]
#         elif lst[n]<0:
#             yield lst[n]**3
#         else:
#             yield lst[n]**2
#         n +=1

# g = mygenerator([4, -2, 3])
# print(next(g))
# print(next(g))
# print(next(g))

import itertools

g = (x**2 for x in itertools.count())


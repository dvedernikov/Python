#V1
# numbers = [0, 1, 12, 0, 0, 5, 1]
# result = []
# for num in numbers:
#     if num !=0:
#         result.append(num)
# for num in numbers:
#     if num == 0:
#         result.append(num)
# print(result)


#V2 Спробував через рандом, але 0 так и не вийшло отримати =(

import random
numbers = [random.randint(0, 20) for _ in range(5)]
result = []
for num in numbers:
    if num !=0:
        result.append(num)
for num in numbers:
    if num == 0:
        result.append(num)
print(result)

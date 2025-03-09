#v1
# numbers = [5, 9, 8, 4, 7, 3]
# result = 0
# if numbers:
#     for i in range(0, len(numbers), 2):
#         result += numbers[i]
#     result *= numbers[-1]
# print(result)

#v2
import random
numbers = [random.randint(0, 10) for _ in range(8)]
result = 0
if numbers:
    for i in range(0, len(numbers), 2):
        result += numbers[i]
    result *= numbers[-1]
print(result)

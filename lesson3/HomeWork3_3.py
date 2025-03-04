numbers = [1, 2, 3, 4, 5]
if numbers:
    mid = len(numbers) // 2
    if len(numbers) % 2 != 0:
        mid += 1
    list1 = numbers[:mid]
    list2 = numbers[mid:]
else:
    list1 = []
    list2 = []

print( list1)
print(list2)
result = [list1, list2]
print(result)
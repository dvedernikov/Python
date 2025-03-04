numbers = [1, 2, 3, 4, 5, 6]

# Якщо список порожній, повертаємо два порожні списки
if not numbers:
    list1 = []
    list2 = []
else:
    # Розділяємо список навпіл (ціле ділення довжини на 2)
    mid = len(numbers) // 2
    list1 = numbers[:mid]  # Перша половина
    list2 = numbers[mid:]  # Друга половина

print("Список 1:", list1)
print("Список 2:", list2)
result = [list1, list2]
print(result)
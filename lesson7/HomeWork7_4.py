def common_elements():
    multiples_of_3 = [num for num in range(100) if num % 3 == 0]
    multiples_of_5 = [num for num in range(100) if num % 5 == 0]
    result = set(multiples_of_3) & set(multiples_of_5)
    print("Числа, кратні 3:", multiples_of_3)
    print("Числа, кратні 5:", multiples_of_5)
    print("Перетин:", result)
    return result

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

try:
    numbers = int(input("Введіть числа: "))
    print(f"Початкове число: {numbers}")

    while numbers > 9:
        digits = [int(digit) for digit in  str(numbers)]
        product = 1
        print("Множимо цифри:", " * ".join(map(str, digits)), "=", end= " ")
        for digit in digits:
            product *= digit
        print(product)
        numbers = product
    print(f"Кінцевий результат: {numbers}")

except ValueError:
    print("Введіть лише число!")
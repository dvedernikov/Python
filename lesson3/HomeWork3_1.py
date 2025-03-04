print("Калькулятор")
print("Доступні математичні  операції: +, -, *, /")

try:
    # Отримуємо ввід від користувача
    num1 = int(input("Введіть перше число: "))
    operation = input("Введіть операцію (+, -, *, /): ")
    num2 = int(input("Введіть друге число: "))

    # Виконуємо операцію
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Помилка: ділення на нуль!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Невірна операція! Використовуйте +, -, *, /")

except ValueError:
    print("Помилка: введіть коректні числа!")

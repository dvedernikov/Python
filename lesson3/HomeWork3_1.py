#V1
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


#V2 При використанні calculator() щоб запустити калькулятор в цикле
# def calculator():
#     print("Калькулятор")
#     print("Доступні математичні  операції: +, -, *, /")
#
#     while True:
#         try:
#             # Отримуємо ввід від користувача
#             num1 = int(input("Введіть перше число: "))
#             operation = input("Введіть операцію (+, -, *, /): ")
#             num2 = fint(input("Введіть друге число: "))
#
#             # Виконуємо операцію
#             if operation == '+':
#                 result = num1 + num2
#                 print(f"{num1} + {num2} = {result}")
#             elif operation == '-':
#                 result = num1 - num2
#                 print(f"{num1} - {num2} = {result}")
#             elif operation == '*':
#                 result = num1 * num2
#                 print(f"{num1} * {num2} = {result}")
#             elif operation == '/':
#                 if num2 == 0:
#                     print("Помилка: ділення на нуль!")
#                 else:
#                     result = num1 / num2
#                     print(f"{num1} / {num2} = {result}")
#             else:
#                 print("Невірна операція! Використовуйте +, -, *, /")
#
#             # Запитуємо, чи хоче користувач продовжувати
#             continue_calc = input("Бажаєте продовжити? (так/ні): ").lower()
#             if continue_calc != 'так':
#                 print("Дякуємо за використання калькулятора!")
#                 break
#
#         except ValueError:
#             print("Помилка: введіть коректні числа!")
#         except Exception as e:
#             print(f"Сталася помилка: {e}")
#
#
# if __name__ == "__main__":
#     calculator()
#v1 Проста версія
numbers = int(input("Введіть чотиризначне число: "))

number1 = numbers // 1000
number2 = (numbers % 1000) // 100
number3 = (numbers % 100) // 10
number4 = numbers % 10  #

print(number1)
print(number2)
print(number3)
print(number4)

#v1.1 Проста версія через divmod
number = int(input("Введіть чотиризначне число: "))

number1, remainder = divmod(number, 1000)
number2, remainder = divmod(remainder, 100)
number3, number4 = divmod(remainder, 10)

print(number1)
print(number2)
print(number3)
print(number4)

#v2 Проста версія + перевірка валідаціЇ
numbers = input("Введіть чотиризначне число: ")

# Перевіряємо, що введене значення складається із 4 цифр і є числом
if numbers.isdigit() and len(numbers) == 4:
    numbers = int(numbers)

    number1 = numbers // 1000
    number2 = (numbers % 1000) // 100
    number3 = (numbers % 100) // 10
    number4 = numbers % 10

    print(number1)
    print(number2)
    print(number3)
    print(number4)
else:
    print("Помилка: Введено некоректне число")
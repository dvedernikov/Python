numbers = int(input("Введіть  числа: "))

n1 = numbers % 10
n2 = (numbers // 10) % 10
n3 = (numbers // 100) % 10
n4 = (numbers // 1000) % 10
n5 = (numbers // 10000) % 10

reversed_number = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5
#reversed_number = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1 - не вийшло як в файлі
print(reversed_number)


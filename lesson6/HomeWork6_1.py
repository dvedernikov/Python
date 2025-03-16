import string

input_letter= input("Ведіть дві букви: ")

if "-" not in input_letter:
    print("Помилка: Невірний формат. Введіть рядок у форматі 'а-b' ")
else:
    start, end = input_letter.split("-")

    start_index = string.ascii_letters.index(start)
    end_index = string.ascii_letters.index(end)

    if start_index <= end_index:
        result = string.ascii_letters[start_index:end_index + 1]
    else:
        result = string.ascii_letters[end_index:start_index + 1][::-1]


    print(result)
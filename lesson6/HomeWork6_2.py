try:

    seconds = int(input("Введіть кількість секунд: "))

    if 0 <= seconds <8640000:
        days, seconds = divmod(seconds, 24 * 60 * 60)
        hours, seconds = divmod(seconds, 60*60)
        minutes, seconds = divmod(seconds, 60)

        hours_str = str(hours).zfill(2)
        minutes_str = str(minutes).zfill(2)
        seconds_str = str(seconds).zfill(2)

        if days == 1:
            dey_word = "день"
        elif 2 <= days <= 4:
            dey_word = "дні"
        else:
            dey_word = "днів"

        result = f"{days} {dey_word}, {hours_str}:{minutes_str}:{seconds_str}"
        print(result)

    else:
        print("Число має бути від 0 до 8639999")


except ValueError:
    print("Введіть лише число!")
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    try:
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html = file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл {html_file} не знайдено!")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return

    result = ''
    i = 0
    while i < len(html):
        if html[i] == '<':
            while i < len(html) and html[i] != '>':
                i += 1
            i += 1
        else:
            result += html[i]
            i += 1

    lines = [line.strip() for line in result.splitlines() if line.strip()]
    cleaned_text = '\n'.join(lines)  # Виправлено: '/n' → '\n'

    try:
        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(cleaned_text)
        print(f"Очищений текст записано у файл {result_file}")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")


delete_html_tags('draft.html', 'cleaned.txt')
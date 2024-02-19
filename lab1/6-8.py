print("Выберите задачу:")
print("1. Найти наибольшее количество идущих подряд символов кириллицы.")
print("2. Найти минимальное натуральное число в строке.")
print("3. Найти наибольшее количество идущих подряд цифр.")

choice = input("Введите номер задачи (1/2/3): ")
if choice == '1':
    string = input("Введите строку: ")
    max_cyrillic = max(len(s) for s in string.split() if all(c.isalpha() and c.isalpha() for c in s))
    print(f"Наибольшее количество идущих подряд символов кириллицы: {max_cyrillic}")
elif choice == '2':
    import re
    string = input("Введите строку: ")
    numbers = [int(s) for s in re.findall(r'\d+', string)]
    min_number = min(numbers)
    print(f"Минимальное натуральное число в строке: {min_number}")
elif choice == '3':
    import re
    string = input("Введите строку: ")
    max_digits = max(len(s) for s in re.findall(r'\d+', string))
    print(f"Наибольшее количество идущих подряд цифр: {max_digits}")
else:
    print("Некорректный выбор задачи.")

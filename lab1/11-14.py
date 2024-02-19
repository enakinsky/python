def get_average_ascii_weight(string):
    total_weight = 0
    for char in string:
        total_weight += ord(char)
        return total_weight / len(string)

def get_median(strings):
    ascii_weights = [get_average_ascii_weight(string) for string in strings]
    ascii_weights.sort()
    n = len(ascii_weights)
    if n % 2 == 1:
        return ascii_weights[n // 2]
    else:
        return (ascii_weights[(n-1) // 2] + ascii_weights[n // 2]) / 2

def get_quadratic_deviation(string):
    avg_weight = get_average_ascii_weight(string)
    max_avg_weight = 0
    for i in range(len(string)-2):
        weight_sum = ord(string[i]) + ord(string[i+1]) + ord(string[i+2])
        max_avg_weight = max(max_avg_weight, weight_sum/3)
    return (avg_weight - max_avg_weight) ** 2

def get_variance_deviation(strings):
    max_avg_weight = get_average_ascii_weight(strings[0][:3])
    for string in strings:
        weight_sum = 0
        for i in range(len(string)-2):
            weight_sum = max(weight_sum, (ord(string[i]) + ord(string[i+1]) + ord(string[i+2])) / 3)
            max_avg_weight = max(max_avg_weight, weight_sum)
    return (max_avg_weight - get_average_ascii_weight(strings[0][:3])) ** 2

print("Выберите задачу:")
print("1. В порядке увеличения среднего веса ASCII-кода символа строки.")
print("2. В порядке увеличения медианного значения выборки строк.")
print("3. В порядке увеличения квадратичного отклонения.")
print("4. В порядке квадратичного отклонения дисперсии.")

choice = input("Ваш выбор (1/2/3/4): ")

if choice == "1":
    strings = input("Введите строки через запятую: ").split(",")
    strings.sort(key=get_average_ascii_weight)
    print("Результат:", strings)
elif choice == "2":
    strings = input("Введите строки через запятую: ").split(",")
    strings.sort(key=lambda x: abs(get_average_ascii_weight(x) - get_median(strings)))
    print("Результат:", strings)
elif choice == "3":
    strings = input("Введите строки через запятую: ").split(",")
    strings.sort(key=get_quadratic_deviation)
    print("Результат:", strings)
elif choice == "4":
    strings = input("Введите строки через запятую: ").split(",")
    strings.sort(key=lambda x: abs(get_variance_deviation(strings) - get_variance_deviation([strings[0]])))
    print("Результат:", strings)
else:
    print("Ошибка! Неверный выбор задачи.")

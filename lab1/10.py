n = int(input("Введите количество строк: "))
strings = []
for i in range(n):
    string = input("Введите строку: ")
    strings.append(string)
sorted_strings = sorted(strings, key=lambda x: len(x.split()))
print("Строки, упорядоченные по количеству слов в строке:")
for string in sorted_strings:
    print(string)

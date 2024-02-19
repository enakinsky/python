n = int(input("Введите количество строк: "))  
strings = []
for i in range(n):
    string = input("Введите строку: ")
    strings.append(string)
sorted_strings = sorted(strings, key=len)
print("Строки, упорядоченные по длине:")
for string in sorted_strings:
    print(string)

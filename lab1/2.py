import random

def shuffle_string(input_string):
    shuffled_string = ''.join(random.sample(input_string, len(input_string)))
    return shuffled_string
def is_palindrome(input_string):
    letters = [char for char in input_string if char.isalpha()]
    return letters == letters[::-1]
def sort_words_by_length(input_string):
    words = input_string.split()
    sorted_words = ' '.join(sorted(words, key=len))
    return sorted_words
print("Выберите задачу:")
print("1. Перемешать все символы строки в случайном порядке.")
print("2. Проверить, образуют ли прописные символы строки палиндром.")
print("3. Упорядочить слова по количеству букв в каждом слове.")

choice = int(input("Введите номер задачи (1/2/3): "))

if choice == 1:
    input_string = input("Введите строку: ")
    result = shuffle_string(input_string)
    print("Перемешанная строка:", result)
elif choice == 2:
    input_string = input("Введите строку: ")
    if is_palindrome(input_string):
        print("Строка образует палиндром.")
    else:
        print("Строка не образует палиндром.")
elif choice == 3:
    input_string = input("Введите строку с словами через пробел: ")
    result = sort_words_by_length(input_string)
    print("Отсортированные слова по длине:", result)
else:
    print("Некорректный выбор задачи. Пожалуйста, выберите 1, 2 или 3.")

import random

def shuffle_string(input_string):
    shuffled_string = ''.join(random.sample(input_string, len(input_string)))
    return shuffled_string
def is_palindrome(input_string):
    letters = [char for char in input_string if char.isalpha()]
    return letters == letters[::-1]

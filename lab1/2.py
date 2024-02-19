import random

def shuffle_string(input_string):
    shuffled_string = ''.join(random.sample(input_string, len(input_string)))
    return shuffled_string

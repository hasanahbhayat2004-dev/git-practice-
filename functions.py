def is_even(number):
    return number % 2 == 0 

def get_initials(name):
    names = name.split()
    return names[0][0] + names[1][0]

def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

def filter_even_numbers(numbers):
    return []
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


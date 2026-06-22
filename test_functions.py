from functions import is_even

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

from functions import get_initials

def test_get_initials():
    assert get_initials("Hasanah Bhayat") == "HB"

def test_get_initials_john():
    assert get_initials("John Smith") == "JS"

from functions import find_longest_word

def test_find_longest_word():
    assert find_longest_word("The quick brown fox") == "quick"

from functions import filter_even_numbers
def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

from functions import reverse_string
def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def reverse_string(text):
    return text[::-1]

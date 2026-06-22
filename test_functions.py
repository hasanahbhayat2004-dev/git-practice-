from functions import is_even

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

from functions import get_initials

def test_get_initials():
    assert get_initials("Hasanah Bhayat") == "HB"
    
def test_get_initials_john():
    assert get_initials("John Smith") == "JS"
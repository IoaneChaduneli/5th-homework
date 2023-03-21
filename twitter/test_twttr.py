from twttr import shorten

def test_empty_input():
    assert shorten('') == ''

def test_with_vowels():
    assert shorten('AEIOU') == ''

def test_no_vowels():
    assert shorten('twitter') == 'twttr'

def test_digit_number():
    assert shorten('576840383') == ''

def test_symbols():
    assert shorten('$%#@') == ''

def letters_digit():
    assert shorten('65hjg645') == 'jg'

def digits_with_vowels():
    assert shorten('657ea73iou') == ''

def test_each_vowels():
    assert shorten('A') == ''
    assert shorten('E') == ''
    assert shorten('I') == ''
    assert shorten('O') == ''
    assert shorten('U') == ''


    
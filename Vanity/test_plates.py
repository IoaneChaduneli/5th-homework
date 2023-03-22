from plates import is_valid

def test_plates():
    assert is_valid('IO') == True
    assert is_valid('HELLO') == True
    assert is_valid('HE0') == True

def test_invalid_zero():
    assert is_valid('0hell') == False
    assert is_valid('hel057') == False

def test_invalid_digit_symbols():
    assert is_valid('76453') == False
    assert is_valid('%$#') == False

def test_invalid_alaphnum():
    assert is_valid('HE5L04') == False

def test_more_than_six():
    assert is_valid('GOODBYE') == False
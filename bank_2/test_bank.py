from bank import value

def test_one_char():
    assert value('h') == f'${100}'

def test_say_hello():
    assert value('hello') == f'${0}'
    assert value('hello, how are you?') == f'${0}'

def test_say_the_word_begin_h():
    assert value('hey') == f'${20}'
    assert value('hey, how are you?') == f'${20}'

def test_begin_with_digit():
    assert value('55') == f'${100}'
    
def test_begin_symbols():
    assert value('#%^&') == f'${100}'


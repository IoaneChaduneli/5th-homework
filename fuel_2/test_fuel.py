from fractions import Fraction
from fuel import convert, gauge

def test_convert():
    assert convert('3/4') == Fraction(3,4)
    assert convert('a/b') == f'You enter letters instead of digit or Y denominator is less than x counter or y is zero'
    assert convert('5/0') == f'You enter letters instead of digit or Y denominator is less than x counter or y is zero'
    assert convert('-5/10') == f'You enter letters instead of digit or Y denominator is less than x counter or y is zero'
    assert convert('-5/-10') == f'You enter letters instead of digit or Y denominator is less than x counter or y is zero'


def test_gauge():
    assert gauge('3/4') == f'{75}%'
    assert gauge('1/0') == 'Error'
    assert gauge('1/100') == f'E'
    assert gauge('99/100') == f'F'
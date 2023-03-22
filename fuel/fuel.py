from fractions import Fraction

def main():
    fraction = input("Fraction: ")
    result = gauge(fraction)
    print(result)
    
    


def convert(fraction):
    try:
        x , y = map(int, fraction.split('/'))
        if x <= y:
            return Fraction(x,y)
        else:
            raise ValueError
        
    except ValueError:
        return f'You enter letters instead of digit or Y denominator is less than x counter'



def gauge(percentage):
    try:
        percent = convert(percentage) * 100
        if 0 <= percent <= 100:
            if percent <= 1:
                return f'E'
            elif percent >= 99:
                return f'F'
            else:
                return f'{percent}%'
        else:
            raise TypeError
            
    except TypeError:
        return f'Error'


if __name__ == '__main__':
    main()
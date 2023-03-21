def main():
    greet = input("Say Greeting: ").lower()
    print(value(greet))

def value(greeting):
    if len(greeting) > 1:
        if greeting.startswith('hello'):
            return f'${0}'
        elif greeting.startswith('h'):
            return f'${20}' 
        else:
            return f'${100}'
    return f'${100}'
 
    
    
            
if __name__ == '__main__':
    main()

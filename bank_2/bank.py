def main():
    greet = input("Say Greeting: ")
    print(value(greet))

def value(greeting):
    if greeting[0] != 'h':
        return f'${100}'
    elif greeting[0:3] == 'hey' or 'hi':
        return f'${20}'
    elif greeting[0:5] == 'hello':
        return f'${0}'
    
    
            
if __name__ == '__main__':
    main()

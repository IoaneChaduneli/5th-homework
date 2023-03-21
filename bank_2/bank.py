def main():
    greet = input("Say Greeting: ")
    print(value(greet))

def value(greeting):
    if greeting[0] != 'h' or len(greeting) <= 1:
        return f'${100}' 
    elif greeting[0:5] == 'hello':
        return f'${0}'
    elif greeting[0:3] == 'hey' or 'hi':
        return f'${20}' 
 
    
    
            
if __name__ == '__main__':
    main()

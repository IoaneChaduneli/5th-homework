def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # length of input
    if len(s) < 2 or len(s) > 6:
        return False
        # check if input first and second letter isn't number
    if s[0].isdigit():
        return False
        # check if input contains both num and letters
    if not s.isalnum():
        return False
        # checks if input middle chars is not number
    if any(char.isdigit() for char in s[2:-2]):
        return False
    # check if above conditionals are false then everythin is okey
    return True





if __name__ == '__main__':
    main()
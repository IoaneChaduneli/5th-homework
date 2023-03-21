def main():
    word = input("word: ").upper()
    print(shorten(word))
    

def shorten(word):
    word = list(word)
    new_word = []
    vowels = ['A', 'E', 'I', 'O', 'U']

    for char in word:
        if char.isalpha():
            if char not in vowels:
                new_word.append(char)
    
    short_text = "".join(new_word).lower()

    return short_text


if __name__ == '__main__':
    main()
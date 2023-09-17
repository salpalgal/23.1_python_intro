def print_upper_words(words):
    '''looping through list of words in param to print each word in capitals'''
    for word in words:
        print(word.upper())


def print_e_upper_words(words):
    '''looping through list of words in param to print words that start with e or E in capitals.'''
    for word in words:
        if word[0]== "E"or word[0]== "e":
            print(word.upper())
       
def print_upper_letters(words,letters):
    for word in words:
        for l in letters:
            if word[0]== l:
                print(word.upper())





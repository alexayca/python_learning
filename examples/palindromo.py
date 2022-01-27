# Palindromo: un palabra u oracion que se lee al derecho y al reves igual.
#   luz azul
#   anita lava la tina
# Python file one module    ->  https://www.freecodecamp.org/espanol/news/python-if-name-main/


print("File __name__ is set to: {}" .format(__name__))


def isPalindrome(word):                         # As of Python 3.3
    word_parse = word.lower().replace(' ','')   # casefold() is a better alternative that lower()
    if(word_parse[::1]==word_parse[::-1]):      # slices <inicio : final : pasos>
        print(word, " SI es palindromo")
        return True
    else:
        print(word, " NO es palindromo")
        return False


def run():
    phrase="Anita Lava la Tina"
    print('Your phrase or word: "', phrase, f'" have {len(phrase)} characters.')
    print(isPalindrome(phrase))


# punto de entrada (entry point)
if __name__ == '__main__':
    run()

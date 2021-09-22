"""
https://en.wikipedia.org/wiki/List_of_Unicode_characters
Funções
    criar caractere especial baseado na tabela unicode
        Ranges: 32-47 58-64 91-96 123-126 -> [ -\/:-@\[-`{-~]
    criar letras maiúsculas baseado na tabela unicode
        Ranges: 65-90
    criar letras minúsculas baseado na tabela unicode
        Ranges: 97-122
    criar números baseado na tabela unicode
        Ranges: 48-57
    criar senha com:
        possibilidade de escolha dos caracteres (letras, números, etc)
        possibilidade de escolha do tamanho da senha (min = 4)
"""
from random import randint, choice, shuffle


def make_one_special_char():

    char_ranges = [
        randint(32, 47),
        randint(58, 64),
        randint(91, 96),
        randint(123, 126)
    ]

    return chr(choice(char_ranges))


def make_one_uppercase_letter():
    return chr(randint(65, 90))


def make_one_lowercase_letter():
    return chr(randint(97, 122))


def make_one_number():
    return chr(randint(48, 57))


def make_password(length=16, chars=True, lower=True, upper=True, numbers=True):
    assert isinstance(length, int), 'Length type must be int'
    assert length >= 4, 'Length must be at least 4 chars'
    assert chars or lower or upper or numbers, 'At least one param must be true'

    new_password = []

    for i in range(length):
        chars and new_password.append(make_one_special_char())
        lower and new_password.append(make_one_lowercase_letter())
        upper and new_password.append(make_one_uppercase_letter())
        numbers and new_password.append(make_one_number())

    new_password = new_password[:length]

    shuffle(new_password)

    return ''.join(new_password)


if __name__ == '__main__':
    for i in range(10):
        print(make_password())

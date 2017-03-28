
import string

alfal = "abcdefghijklmnopqrstuvwxyz"
alfau = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    letter = letter.lower()
    for eachletter in letter:
        result = alfal.index(eachletter)

        return result


def rotate_character(char, rot):

    new_str = ''
    if char.isupper():
        x = alphabet_position(char)
        y = x + rot
        indx = y % 26
        new_str = new_str + alfau[indx]
        return new_str
    elif char.islower():
        x = alphabet_position(char)
        y = x + rot
        indx = y % 26
        new_str = new_str + alfal[indx]
        return new_str
    else:

        return char


def encrypt(text, rot):
    result = ''
    for letter in text:
        result += rotate_character(letter, rot)
    return result

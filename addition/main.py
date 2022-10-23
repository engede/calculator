#!/usr/local/bin/python
""" addition """

import sys

def is_digit(c) :
    """ Check if character is a digit """
    return 48 <= ord(c) <= 57

def is_number(string) :
    """ Check if string is a number """
    position = 0

    if not isinstance(string, str) or len(string) == 0 :
        return False
    if string[0] == '-' :
        position += 1
    while position < len(string) and is_digit(string[position]) :
        position += 1

    return position == len(string)

def add(nb1, nb2) :
    """ Add 2 numbers """
    i = 0
    carry = False
    result = ''

    while i < len(nb1) or i < len(nb2) or carry :
        char1 = ord(nb1[i]) - ord('0') if i < len(nb1) else 0
        char2 = ord(nb2[i]) - ord('0') if i < len(nb2) else 0
        res = char1 + char2 + int(carry)
        carry = res >= 10
        result += chr((res % 10) + ord('0'))
        i += 1

    return reverse(result)

def reverse(string) :
    """ Reverse string """
    res = ''

    for _, char in enumerate(string) :
        res = char + res

    return res

def main(argv) :
    """ Entry point """
    number1 = ''
    number2 = ''

    if len(argv) != 2 :
        return 1

    number1 = argv[0]
    number2 = argv[1]

    if not is_number(number1) or not is_number(number2) :
        return 1

    print(add(reverse(number1), reverse(number2)))

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

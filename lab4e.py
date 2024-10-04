#!/usr/bin/env python3
# Author ID: 120352224

def is_digits(sobj):
    # Loop through each character in sobj
    for char in sobj:
        # Check if the character is not a digit
        if not char.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')

#!/usr/bin/env python3

"""Programme qui échange la casse d'une chaine de characteres en entrée"""

def main():
    """Echange la casse manuellement"""
    string = input("SwApCasE>> ")
    swap_str = ""
    for letter in string:
        nbr = ord(letter)
        if ord('A') <= nbr <= ord('Z'): 
            swap_str += chr(nbr + (ord('a') - ord('A')))
        if ord('a') <= nbr <= ord('z'): 
            swap_str += chr(nbr + (ord('A') - ord('a')))
        else:
            swap_str += letter
    print(swap_str)


if __name__ == '__main__':
    main()

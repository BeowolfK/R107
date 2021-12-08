#!usr/bin/env python3

"""
Retourne la somme des deux inputs
"""


def main():
    """Programme principal"""
    try:
        a = int(input("Premier nombre : "))
        b = int(input("Deuxieme nombre : "))
    except ValueError:
        raise ValueError("Vous n'entrer pas des entiers")
    print(f"{a}+{b}={a+b}")



if __name__ == '__main__':
    main()

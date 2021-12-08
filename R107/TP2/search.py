#!/usr/bin/env python3
import os
"""Jeu du plus ou moins grace a l'entrée utilisateur"""

def main():
    """Fonction qui compte le nombre de ccoups pour trover un nombre n en indiquant + ou - a caque fois"""
    n = int(input("Entrer n : "))  
    if not(1 < n < 100):
        return
    os.system("clear")
    bob = int(input("Bob:~/$ "))
    counter = 1
    while n != bob:
        if n > bob:
            print('+')
        else:
            print('-')
        bob = int(input("Bob:~/$ "))
        counter += 1
    print(f"Bob a trouvé en {counter} coups, le nombre était {n}")

if __name__ == '__main__':
    main()
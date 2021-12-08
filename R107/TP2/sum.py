#!/usr/bin/env python3
"""Calcul les n premiers entiers avec n l'entrée utilisateur"""


def main():
    """Renvoie la somme de 0 a n"""
    n = int(input("Entrer n : "))
    if n <= 0:
        return
    somme = 0
    for i in range(n+1):
        somme += i
    print(somme)

if __name__ == '__main__':
    main()
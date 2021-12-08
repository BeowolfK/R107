#!/usr/bin/env python3

from math import pi
import os

"""
Calcul des aires de différentes figures géométrique grace a un menu
"""
def menu():
    """Affiche le menue de choix des figures"""
    width = os.get_terminal_size(0)[0]
    print('-' * width)
    figures = ["Quel figure voulez-vous?","","1) Disque", "2) Triangle", "3) Rectangle"]
    for fig in figures:
        print(' ' * ((width - len(fig)) // 2 + 1) + fig)
    print('-' * width)
    return


def main():
    menu()
    choix = input('>> ')
    if choix == '1':
        rayon = int(input("Rayon ? "))
        print(f"L'aire du disque est de : {pi*rayon*rayon}")
    elif choix == '2':
        base = int(input("Base ? "))
        hauteur = int(input("Hauteur ? "))
        print(f"L'aire du disque est de : {base*hauteur/2}")
    elif choix == '3':
        long = int(input("Longueur ? "))
        larg = int(input("Largeur ? "))
        print(f"L'aire du disque est de : {long*larg}")
    else:
        print("Choix invalide !")

if __name__ == '__main__':
    main()
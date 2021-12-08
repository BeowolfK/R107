#!/usr/bin/env python3
"""TP7 programmation lecture de fichier"""
import os

def cat(chemin, size):
    """Exercice 1 TP7 lecture de fichier en fonction du chemin entrée par l'utilisateur qui se met en pause touts les 20lignes"""
    assert isinstance(chemin, str)
    with open(chemin, 'r', encoding='U8') as f:
        no = 1
        for line1 in f:
            print(f"{no} : {line1.strip()}")
            while no % size != 0:
                line = f.readline()
                if not line:
                    break
                no += 1
                print(f"{no} : {line.strip()}")

            input("appuyez sur entrée pour continuer")
            no += 1


def main():
    chemin = input("Entrer le chemin du fichier : ")
    if not os.path.exists(chemin) or not os.path.isfile(chemin) :
        print("fichier inexistant")
    else:
        cat(chemin)

if __name__ == '__main__':
    main()
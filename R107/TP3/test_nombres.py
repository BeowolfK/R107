#!/usr/bin/env python3
"""Exercice 6 module"""
import premier
from saisie import saisie_entiers

def main():
    running = True
    while running:
        n = saisie_entiers(1, 5000)
        print(premier.facteur_premier2(n))
        rep = input("Continuer ? (y/n) ")
        if rep == 'n':
            running = False
        elif rep != 'y':
            print("Reponse non valide, on continue.")


if __name__ == '__main__':
    main()
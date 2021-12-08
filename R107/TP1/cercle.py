#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renvoie le périmetre et l'aire du cercle
"""

from math import pi


def main():
    try:
        r = int(input("Entrer le rayon : "))
    except ValueError:
        raise ValueError("Vous n'entrer pas des entiers")
    print(f"Rayon = {pi*r*2}")
    print(f"Aire = {pi*r**2}")
    
if __name__ == "__main__":
    main()
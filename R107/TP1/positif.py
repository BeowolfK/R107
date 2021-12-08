#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Indique la positivité d'un nombre
"""

def main():
    try:
        r = int(input("Entrer un nombre : "))
    except ValueError:
        raise ValueError("Vous n'entrer pas des entiers")
    print("Positif" if r > 0 else "Négatif" if r < 0 else "Nulle")
    
if __name__ == "__main__":
    main()
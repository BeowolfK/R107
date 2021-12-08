#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Affiche le carré de l'entrée utilisateur
"""

def main():
    """Programme principal"""
    try:
        a = int(input("Entrer un nombre : "))
    except ValueError:
        raise ValueError("Vous n'entrer pas des entiers")
    print(f"{a}² = {a*a}")
    
if __name__ == '__main__':
    main()

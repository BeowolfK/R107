#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Informe l'heure et minute suivante a l'entrée utilisateur
"""

def main():
    try:
        h = int(input("Entrer les heures : "))
        m = int(input("Entrer les minutes : "))
    except ValueError:
        raise ValueError("Vous n'entrer pas des entiers")
    assert 0 <= h < 24 and 0 <= m < 60
    m += 1
    if m > 59:
        h += 1
        m = 0
        if h > 23:
            h = 0
    print(f"Dans 1min, il sera {h}h:{m}m")
if __name__ == "__main__":
    main()
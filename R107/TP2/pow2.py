#!/usr/bin/env python3

"""Calcul du premier entier supéreiru a l'entré utilisateur correspondant a une puissance de  2"""

def main():
    nbr = int(input("Saisissez un entier positif : "))
    if nbr <= 0:
        return
    pow2 = 2
    while pow2 < nbr:
        pow2 *= 2
    print(f"La premiere puissance de 2 supérieur ou égale a {nbr} est {pow2}")

if __name__ == '__main__':
    main()
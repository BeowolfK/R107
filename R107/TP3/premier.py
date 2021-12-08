#!/usr/bin/env python3
"""Programmes qui verifie si un nombre est premier ou non """


def est_premier(n):
    """Renvoie True si un entier est premier"""
    assert isinstance(n, int)
    assert n > 0
    counter = 2
    is_prime = True
    while is_prime and counter < n:
        if n%counter == 0:
            is_prime = False
        counter += 1
    return is_prime

def facteur_premier(n):
    assert isinstance(n, int)
    assert n > 0
    nbr = str(n) + " = 1"
    i = 2
    while n>1: 
        while n%i==0 and est_premier(i): 
            nbr += " * " + str(i)
            n=n/i 
        i=i+1
    return nbr

def facteur_premier2(n):
    assert isinstance(n, int)
    assert n > 0
    nbr = str(n) + " = 1"
    i = 2
    while n>1: 
        cpt = 0
        while n%i==0 and est_premier(i):
            cpt+=1
            n=n/i
        if cpt == 1:
            nbr += " * " + str(i)
        elif cpt > 1:
            nbr+= " * "+str(i)+'^'+str(cpt)
        i=i+1
    return nbr
def main():
    assert facteur_premier(234) == "234 = 1 * 2 * 3 * 3 * 13"
    assert facteur_premier(1000) == "1000 = 1 * 2 * 2 * 2 * 5 * 5 * 5"
    assert facteur_premier(666) == "666 = 1 * 2 * 3 * 3 * 37"
    assert facteur_premier(42) == "42 = 1 * 2 * 3 * 7"
    assert facteur_premier(7) == "7 = 1 * 7"
    
    assert facteur_premier2(234) == "234 = 1 * 2 * 3^2 * 13"
    assert facteur_premier2(64) == "64 = 1 * 2^6"
    



if __name__ == '__main__':
    main()
#!/usr/bin/env python3

def saisie_entiers(inf, sup):
    assert isinstance(inf,int) 
    assert isinstance(sup, int) 
    assert inf < sup
    nbr = int(input(f"Entrer un nombre compris entre {inf} et {sup}: "))
    while not(inf <= nbr <= sup):
        nbr = int(input(f"Entrer un nombre compris entre {inf} et {sup}: "))
    return nbr


def main():
    nbr1 = saisie_entiers(0, 10)
    nbr2 = saisie_entiers(-10 ,100)

if __name__ == '__main__':
    main()
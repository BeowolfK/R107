#!/usr/bin/env python3
"""Affiche une pyramid d'étoile de 2 maniere différente"""

def pyramide(n):
    """Affiche directement la pyramide"""
    assert isinstance(n, int) 
    assert n > 0
    star = 1
    for i in range(n):
        print(' '*(n-1-i)+'*'*star)
        star+=2
    return


def pyramide2(n):
    """Renvoie la chaine de char contenant la pyramide"""
    assert isinstance(n, int) 
    assert n > 0
    star = 1
    chr = ""
    for i in range(n):
        chr += ' '*(n-1-i)+'*'*star+'\n'
        star+=2
    return chr

def main():
    pyramide(int(input('1>> ')))
    print(pyramide2(int(input('2>> '))))

if __name__ == '__main__':
    main()
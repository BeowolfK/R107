#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercice 3 contennant la fonction nb_occurences

@author: Kénan Meylan TP4
"""

from typing import Counter


def nb_occurences(entier, liste):
    """Compte le nombre d'occurence d'un entier dans la liste"""
    assert isinstance(entier, int)
    assert isinstance(liste, list)
    counter = 0
    for i in liste:
        if entier == i:
            counter += 1
    return counter

def main():
    """Programme principal servant a testet les assertions"""
    l = [1, 20, 3, 4, 10, 3, 1, 1]
    assert nb_occurences(1, l) == 3
    assert nb_occurences(3, l) == 2
    assert nb_occurences(20, l) == 1
    assert nb_occurences(200, l) == 0
    
    l2 = [-7, 8, -6, 5, 6, 7, 8]
    assert nb_occurences(1, l2) == 0
    assert nb_occurences(8, l2) == 2
    assert nb_occurences(-7, l2) == 1


if __name__ == '__main__':
    main()
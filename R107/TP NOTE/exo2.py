#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercice 2 contennant la fonction rotation

@author: Kénan Meylan TP4
"""

def rotation(l):
    """Renvoie une liste dont le derniere élement de la liste passé en parametre se trouver en premier élément
    La liste passé en parametre reste inchangé"""
    assert isinstance(l, list)
    if l == []:
        return []
    l2 = [l[-1]]
    for i in range(len(l)-1):
        l2.append(l[i])
    return l2

def main():
    """Programme principal servant a testet les assertions"""
    l = [1, 2, 3, 4]
    assert rotation(l) == [4, 1, 2, 3]
    assert l == [1, 2, 3, 4]

    l2 = []
    assert rotation(l2) == []
    assert l2 == []

    l3 = [-3, -2, -1, 0, 'a', 'b', 'c', (1, 2)]
    assert rotation(l3) == [(1, 2), -3, -2, -1, 0, 'a', 'b', 'c']
    assert l3 == [-3, -2, -1, 0, 'a', 'b', 'c', (1, 2)]

if __name__ == '__main__':
    main()
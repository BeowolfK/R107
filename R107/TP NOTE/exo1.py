#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercice 1 contennant la fonction qui inverse une liste

@author: Kénan Meylan TP4
"""

def inverse(l):
    """Renvoie la liste inversé de celle passé en parametre"""
    assert isinstance(l,list)
    return l[::-1]

def main():
    """Programme principal servant a testet les assertions"""
    assert inverse([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert inverse([]) == []
    assert inverse([-3, -2, -1, 0, 'a', 'b', 'c', (1, 2) ]) == [(1, 2), 'c', 'b', 'a', 0, -1, -2, -3]

if __name__ == '__main__':
    main()
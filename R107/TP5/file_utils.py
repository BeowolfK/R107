#!/usr/bin/env python3
"""Exercice 8 (Partie Pile) du TP5"""
from file import enfiler, defiler
from pile import empiler, depiler

def inverser(fil):
    """Inversion de la file en utilsiantune pile intermédiare"""
    assert isinstance(fil, list)
    temp = []
    for i in range(len(fil)):
        empiler(temp, defiler(fil))
    f2 = []
    for i in range(len(temp)):
        enfiler(f2, depiler(temp))
    return f2
def main():
    assert inverser([2, 4, 5, 6, 7]) == [7, 6, 5, 4, 2]
    assert inverser([221564, 54354, -5,'' , (3, 2)]) == [(3, 2), '', -5, 54354, 221564]
    print("Fonction inverser ok!")

if __name__ == '__main__':
    main()
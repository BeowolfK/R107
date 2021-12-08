#!/usr/bin/env python3
"""Exercice 5 (Partie Pile) du TP5"""
from pile import empiler, depiler


def inverser(pile):
    """Renvoie la liste en parant de la fin"""
    l = []
    for i in range(len(pile)):
        empiler(l, depiler(pile))
    return l

def intercal(l1, l2):
    """Renvoie une liste de deux liste intercalé un sur 2"""
    assert isinstance(l1, list)
    assert isinstance(l2, list)
    if len(l1) != len(l2):
        return None
    l3 = []
    for index in range(len(l1)):
        empiler(l3, depiler(l2))
        empiler(l3, depiler(l1))
    return inverser(l3)

def main():
    assert inverser([2, 4, 5, 6, 7]) == [7, 6, 5, 4, 2]
    assert inverser([221564, 54354, -5,'' , (3, 2)]) == [(3, 2), '', -5, 54354, 221564]
    print("Fonction inverser ok!")

    p1 = [10, 5, 100, 3]
    p2 = [-10, -20, -30, -40]
    p3 = intercal(p1, p2)
    assert p3 == [10, -10, 5, -20, 100, -30, 3, -40]
    assert intercal([1, 2, 3], [1, 2, 3, 4]) is None
    print("Fonction intercal valide")

if __name__ == "__main__":
    main()
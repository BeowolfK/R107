#!/usr/bin/env python3
"""Exercice 7 (Partie Pile) du TP5"""

def est_vide(fil):
    """Retourne True dans le cas ou la pile et vide"""
    assert isinstance(fil, list)
    if fil == []:
        return True
    return False

def enfiler(fil, element):
    """enfile un element sur le fil en parametre"""
    assert isinstance(fil, list)
    fil.insert(0, element)

def defiler(fil):
    """defile le premier element saisie sur le fil en parametre"""
    assert isinstance(fil, list)
    if est_vide(fil):
        return None
    return fil.pop()
    
def main():

    fil = []

    assert est_vide(fil)

    enfiler(fil, 1)
    assert fil == [1]
    assert not est_vide(fil)
    print("Fonction est_vide valide")

    enfiler(fil, 2)
    assert fil == [2, 1]
    enfiler(fil, 3)
    assert fil == [3, 2, 1]
    print("Fonction enfiler valide")

    assert defiler(fil) == 1
    assert defiler(fil) == 2
    assert not defiler(fil) == 1
    assert defiler(fil) is None
    print("Fonction defiler valide")


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""Exercice 4 et 5 (Partie Pile) du TP5"""

def est_vide(pile):
    """Retourne True dans le cas ou la pile et vide"""
    assert isinstance(pile, list)
    if len(pile) == 0:
        return True
    return False  

def empiler(pile, element):
    """empile l'élément en parameter a la liste en parametre"""
    assert isinstance(pile, list)
    pile.append(element)

def depiler(pile):
    """dépile le derniere élément de la liste en parametre"""
    assert isinstance(pile, list)
    if est_vide(pile):
        return None
    return pile.pop()




def main():
    l = []
    assert est_vide(l)
    l.append(1)
    assert not est_vide(l)
    print("Fonction est_vide valide")

    empiler(l, 2)
    assert l == [1, 2]
    empiler(l, 3)
    assert not l == [1, 2]
    print("Fonction empiler valide")

    assert depiler(l) == 3
    assert depiler(l) == 2
    assert not depiler(l) == 2
    assert depiler(l) == None
    print("Fonction depiler valide")


if __name__ == '__main__':
    main()
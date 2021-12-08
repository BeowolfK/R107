#!/usr/bin/env python3
"""Recherche les adresse ipv4  en fonction des nom de domaines """

def cherche_domaine(dom, lst):
    """Renvoie l'adresse ip en fonction des nom de domaines"""
    assert isinstance(dom, str)
    assert isinstance(lst, list)
    try :
        return lst[1][lst[0].index(dom)]
    except ValueError:
        return None

def main():
    lst = [
            ["univ-amu.fr", "enseignementsup-recherche.gouv.fr", "seenthis.net"],
            [
                [139,124,244,38], 
                [185,75,143,29], 
                [217,182,178,243]
            ]
        ]
    assert cherche_domaine("univ-amu.fr", lst) == [139,124,244,38]
    assert cherche_domaine("seenthis.net", lst) == [217,182,178,243]
    assert not cherche_domaine("enseignementsup-recherche.gouv.fr", lst) == [127, 0, 0, 1]

if __name__ == "__main__":
    main()
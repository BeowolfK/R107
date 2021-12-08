#!/usr/bin/env python3
"""Exercice 1 (Partie 4) du TP6"""

def nettoie_liste(liste):
    assert isinstance(liste, list)
    for i in range(len(liste)):
        assert isinstance(liste[i], str)
        liste[i] = liste[i].strip()
    return liste


def main():
    test = ['une chaîne propre',
            'une chaîne à nettoyer à droite    ',
            '    une chaîne à nettoyer à gauche',
            '   une chaîne à nettoyer des deux côtés   ']
    assert nettoie_liste(test) == ['une chaîne propre', 
                                   'une chaîne à nettoyer à droite', 
                                   'une chaîne à nettoyer à gauche', 
                                   'une chaîne à nettoyer des deux côtés']
    
    test2 = ['une chaîne propre',
            'une chaîne à nettoyer à droite    ',
            '    une chaîne à nettoyer à gauche',
            '   une chaîne à nettoyer des deux côtés  ', 
            'une     chaine a    nettoyer       au milieu']

    assert not nettoie_liste(test2) == ['une chaîne propre', 
                                        'une chaîne à nettoyer à droite', 
                                        'une chaîne à nettoyer à gauche', 
                                        'une chaîne à nettoyer des deux côtés',
                                        'une chaine a nettoyer au milieu']

    print("Tous les test de nettoie_liste sont passés")

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""Reordonne une liste de maniere particuliere"""

def reordonne(l):
    """Reordonne les element a l'index paire de la liste en fonction de l'index a l'index impaire de la liste"""
    assert isinstance(l, list)
    liste = [None for i in range(len(l)//2)]
    for i in range(0, len(l)//2):
        index = l[i*2+1]
        if index < 1:
            return None
        liste[index-1] = l[i*2]
    return liste
    
def main():
    assert reordonne([10, 3, 12, 4, 36, 1, 44, 2]) == [36, 44, 10, 12]
    assert reordonne([10, 1, 12, 2, 36, 3, 44, 4]) == [10, 12, 36, 44]
    assert not reordonne([10, 1, 12, 2, 36, 3, 44, 4, 5]) == [10, 12, 36, 44]
    assert reordonne([]) == []
    

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""Différente opération sur une liste d'entier"""

def maximum(l):
    """renvoie le maximum d'une liste"""
    assert isinstance(l, list)
    try:
        max = l[0]
    except IndexError:
        return None
    for i in l:
        if i >= max:
            max = i
    return max

def variance(l):
    """Renvoie la variance d'une liste"""
    assert isinstance(l, list)
    try :
        mean = sum(l)/len(l)
    except TypeError:
        return None
    var = 0
    for i in l:
        var += (i-mean)**2
    return var/len(l)

def intercal(l1, l2):
    """Renvoie une liste de deux liste interalé un sur 2"""
    assert isinstance(l1, list)
    assert isinstance(l2, list)
    assert len(l1) == len(l2)
    l3 = []
    for index in range(len(l1)):
        l3.append(l1[index])
        l3.append(l2[index])
    l1 = l2 = []
    return l3

def main():
    assert maximum([10, 100, -5, 1]) == 100
    assert maximum([10, 10, -5, 1]) == 10
    assert maximum([-123, -56, -7, -46]) == -7
    assert maximum([]) is None

    assert variance([1000, 1, 1, 1]) == 187125.1875
    assert variance([12, 14, 6.5, 20, 5, 17.5]) == 29.333333333333332
    assert variance([12, 14, "Tutut", 20, 5, 17.5]) == None
    
    assert intercal([1, 2, 3, 4], ['a', 'b', 'c', 'd']) == [1, 'a', 2, 'b', 3, 'c', 4, 'd']

if __name__ == '__main__':
    main()
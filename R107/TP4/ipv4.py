#!/usr/bin/env python3
"""Check ipv4 compris entre 0 et 255"""

def check_ipv4(ipv4):
    """Check ipv4 compris entre 0 et 255"""
    if len(ipv4) == 4:
        return None
    check = True
    for i in ipv4:
        if i < 0 or i > 255:
            check = False
    return check

def ipv4_from_ints(a1, a2, a3, a4):
    """Renvoie une ipv4 grace au 4 entier en parametre"""
    assert isinstance(a1, int) and 0 <= a1 <= 255
    assert type(a1) == int
    assert isinstance(a2, int) and 0 <= a2 <= 255
    assert isinstance(a3, int) and 0 <= a3 <= 255
    assert isinstance(a4, int) and 0 <= a4 <= 255
    ipv4 = []
    for i in (a1, a2, a3, a4):
        ipv4.append(i)
    assert check_ipv4(ipv4)
    return ipv4

def main():
    assert check_ipv4([0,0,0,0])
    assert check_ipv4([127,0,0,1])
    assert check_ipv4([255,255,255,255])
    assert not check_ipv4([255,255,255])
    assert not check_ipv4([2048,56,78,-75])
    print("Test1 terminé")
    assert ipv4_from_ints(192, 168, 0, 1) == [192, 168, 0, 1]
    assert ipv4_from_ints(0,0,0,0) == [0, 0, 0, 0]
    assert ipv4_from_ints(255, 255, 255, 255) == [255, 255, 255, 255]
    # assert not ipv4_from_ints(2048,56,78,-75) == [2048,56,78,-75]
    print("Test2 terminé")

if __name__ == '__main__':
    main()
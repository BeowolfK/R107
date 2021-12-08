#!/usr/bin/env python3
"""TP7 Résolution locale d'hotes"""
import sys

def resoud(host):
    """itere dans le fichier pour trouver l'ip correspodnat a l'host"""
    assert isinstance(host, str)
    with open("/etc/hosts", 'r', encoding='U8') as f:
        for line in f:
            if line[0] == '#' or line[0] == '\n':
                continue
            else:
                current = line.split()
                if host in current:
                    return current[0]

def main():
    if len(sys.argv) != 2:
        print("resolution.py : nombre de paramètres incorrect\
              \nSyntaxe : resolution.py nom_d_hote")
    else:
        ans = resoud(sys.argv[1])
        if ans is not None:
            print(ans)

if __name__ == '__main__':
    main()

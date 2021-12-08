#!/usr/bin/env python3
"""TP7 programmation lecture de fichier"""
from affiche import cat
import os
import sys

def main():
    size = os.get_terminal_size()[1]
    for chemin in sys.argv[1:]:
        if not os.path.exists(chemin) or not os.path.isfile(chemin) :
            print("fichier inexistant")
        else:
            cat(chemin, size-1)

if __name__ == '__main__':
    main()
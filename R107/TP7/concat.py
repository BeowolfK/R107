#!/usr/bin/env python3
"""exo 5 tp 7"""
from sys import argv
import os
import sys


def copie(df_lect, df_ecr):
    """copie le contenu du fichier source dans un fichier destination"""
    if verifie_fichier(df_lect):
        with open(df_lect, 'r', encoding='U8') as l:
            with open(df_ecr, 'a+', encoding='U8') as w:
                for line in l:
                    w.write(line)


def verifie_fichier(chemin):
    """verification de l'existence et du type du chemin"""
    if not os.path.exists(chemin):
        print(f"fichier inexistant : {chemin}")
        return False
    elif not os.path.isfile(chemin):
        print(f"pas un fichier : {chemin}")
        return False
    else :
        return True

def main():
    if len(sys.argv) == 4:
        if verifie_fichier(sys.argv[3]):
            os.remove(sys.argv[3])
        copie(sys.argv[1], sys.argv[3])
        copie(sys.argv[2], sys.argv[3])
    else:
        print("nbr d'arguments incorrect")


if __name__ == '__main__':
    main()
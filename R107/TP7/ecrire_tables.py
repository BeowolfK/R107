#!/usr/bin/env python3
"""Ecriture des tabls de multiplication de 2 a 9 dans un fichier"""
from io import TextIOWrapper


def ecrire_table(df, num_table):
    """ecrit chaque ligne de calculs dans le fichier"""
    assert isinstance(df, TextIOWrapper)
    assert isinstance(num_table, int)
    for i in range(1, 10):
        df.write(f"{num_table} * {i} = {num_table*i}\n")
    df.write("\n")

def main():
    with open("tables.txt", 'w+', encoding='U8') as df:
        for i in range(2, 10):
            ecrire_table(df, i)

if __name__ == '__main__':
    main()
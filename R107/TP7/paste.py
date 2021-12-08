#!/usr/bin/env python3
"""exo 6 tp 7"""
from concat import verifie_fichier
import sys
import itertools

def fusion(in1, in2, output):
    """fusionne les fichier en printant et ecrivant dans le fichier d'output"""
    assert isinstance(in1, str)
    assert isinstance(in2, str)
    assert isinstance(output, str)
    if verifie_fichier(in1) and verifie_fichier(in2):
        with open(in1, 'r', encoding='U8') as i1:
            with open(in2, 'r', encoding='U8') as i2:
                with open(output, 'w+', encoding='U8') as output:
                    l = list(itertools.zip_longest(i1.readlines(), i2.readlines(), fillvalue=''))
                    for i in l:
                        i0 = i[0].strip('\n')
                        i1 = i[1].strip('\n')
                        paste = f"{i0}\t{i1}\n"
                        print(paste, end='')
                        output.write(paste)

def main():
    if len(sys.argv) == 4:
        fusion(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("nbr d'arguments incorrect")

if __name__ == '__main__':
    main()
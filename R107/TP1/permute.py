#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Permute 3 variables
"""

def main():
    a = 100
    b = -45
    c = "spam"
    print(f"a = {a}, b = {b}, c = {c}")
    temp = a
    a = c
    c = b
    b = temp
    # On peut aussi faire : 
    # a, b, c = c, a, b
    print(f"a = {a}, b = {b}, c = {c}")

if __name__ == '__main__':
    main()
    
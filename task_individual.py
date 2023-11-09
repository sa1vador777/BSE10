#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(A: set, B: set, C: set, D: set) -> str:

    U = set("abcdefghijklmnopqrstuvwxyz")
    X: set = (A.intersection(C).union(B.intersection(C)))
    
    nB: set = U.difference(B)
    Y: set = (A.intersection(nB).union(D.difference(C)))

    return f"X = {X}\nY = {Y}"


if __name__ == "__main__":
    A: set = {'b', 'e', 'f', 'k', 't'}
    B: set = {'f', 'i', 'j', 'p', 'y'}
    C: set = {'j', 'k', 'l', 'y'}
    D: set = {'i', 'j', 's', 't', 'u', 'y', 'z'}
    print(main(A, B, C, D))

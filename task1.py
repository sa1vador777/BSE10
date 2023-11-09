#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: str) -> int:
    vowels_set = set("aeiouyаеёиоуыэюя")
    set_inp = set(inp)

    vowels_count: int = len(set_inp.intersection(vowels_set))
    return vowels_count
    


if __name__ == "__main__":
    inp = input("Впишите любую строку: ")
    print(main(inp))

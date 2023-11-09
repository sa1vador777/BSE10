#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp: str) -> int:
    eng_vowels_set = {'a', 'e', 'i', 'o', 'u', 'y'}
    ru_vowels_set = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    vowels_count: int = 0
    for letter in inp:
        if letter.lower() in eng_vowels_set or letter.lower() in ru_vowels_set:
            vowels_count += 1
    return vowels_count


if __name__ == "__main__":
    inp = input("Впишите любую строку: ")
    print(main(inp))

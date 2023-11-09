#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp1: str, inp2: str) -> set[str]:
    result_set: set = set()
    for letter in inp1:
        if letter in inp2:
            result_set.add(letter)
    return result_set


if __name__ == "__main__":
    inp1 = input("Введите первую строку: ")
    inp2 = input("Введите вторую строку: ")
    print(main(inp1, inp2))

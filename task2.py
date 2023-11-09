#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(inp1: set, inp2: set) -> set:
    return inp1.intersection(inp2)


if __name__ == "__main__":
    inp1 = set(input("Введите первую строку: "))
    inp2 = set(input("Введите вторую строку: "))
    print(main(inp1, inp2))

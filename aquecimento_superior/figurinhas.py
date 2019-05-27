#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mdc(a, b):
    while (b != 0):
       r = a % b
       a = b
       b = r
       
    return a

n = int(input())
while n != 0:
    numbers = input().split()
    print(mdc(int(numbers[0]), int(numbers[1]),))
    n -= 1


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t = int(input())
while t != 0:
    _input = input().split()
    pa = int(_input[0])
    pb = int(_input[1])
    g1 = 1 + float(_input[2])/100
    g2 = 1 + float(_input[3])/100
    i = 0
    while i <= 100 and pa <= pb:
        pa = int(pa*g1)
        pb = int(pb*g2)
        i += 1
    
    print(i, "anos.") if i <= 100 else print("Mais de 1 seculo.")
    
    
    t -= 1



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
v_par = []
v_impar = []
while n != 0:
    _input = int(input())
    if _input % 2 == 0:
        v_par.append(_input)
    else:
        v_impar.append(-_input)
        
        
    n -= 1
v_par.sort()
v_impar.sort()
for i in v_par:
    print(i)

for i in v_impar:
    print(-i)



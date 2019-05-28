#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
cont = 0
k = 5

if n % 2 == 0:
    cont += 1
    while n % 2 == 0 :
        n = n/2

if n % 3 == 0:
    cont += 1
    while n % 3 == 0 :
        n = n/3

while k <= n and n > 1:
    if k >= n**0.5:
        cont += 1
        break
        
    if n % k == 0:
        cont += 1
        while n % k == 0 :
            n = n/k
            
    if n % (k+2) == 0:
        cont += 1
        while n % (k+2) == 0 :
            n = n/(k+2)
    k += 6
    
print(2**cont-(cont+1))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
v = [int(i) for i in input().split()]
v_visited = [False for i in range(n)]
i = 0
qtd = 0
carneiros_roubados = 0;
while(i > -1 and i < n):
    
    if not v_visited[i]:
        v_visited[i] = True
        qtd += 1
        
    if v[i] != 0:
        carneiros_roubados += 1
        if v[i]%2 == 0:
            # Par
            v[i] -= 1
            i -= 1
        else:
            # Ímpar
            v[i] -= 1
            i += 1
            
    else:
        # Valor zerado
        i -= 1
        

print(qtd, sum(v)) 


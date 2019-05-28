#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
while n != 0:
    p = int(input())
    time_pizzas = []
    while n != 0:
        _input = input().split()
        time_pizzas.append([int(_input[1]), int(_input[0])])
        n -= 1
            
    time_pizzas.sort()
    min_time = [[0 for j in range(p+1)] for i in range(len(time_pizzas))]
    for j in range(time_pizzas[0][0], p+1):
        min_time[0][j] = time_pizzas[0][1]
        
    for i in range(1, len(time_pizzas)):
        for j in range(1, time_pizzas[i][0]):
            if j <= p:
                min_time[i][j] = max(min_time[i-1][j], min_time[i][j-1])
            else:
                break
            
        for j in range(time_pizzas[i][0], p+1):
            min_time[i][j] = max(min_time[i-1][j], min_time[i][j-1], min_time[i-1][j-time_pizzas[i][0]] + time_pizzas[i][1])
            
    
    print(min_time[len(time_pizzas) - 1][p], "min.") 
    
    n = int(input())


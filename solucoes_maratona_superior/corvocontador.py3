#!/usr/bin/env python3
# -*- coding: utf-8 -*-

caw_caw_qtd = 0
soma = 0
while caw_caw_qtd != 3:
    number_bin = input()
    new_number_bin = [0,0,0]
    if number_bin == "caw caw":
        print(soma)
        soma = 0
        caw_caw_qtd += 1
    else:
        for i in range(3):
            
            if number_bin[i] == '*':
                new_number_bin[i] = 1
            else:
                new_number_bin[i] = 0
                
        soma = soma + new_number_bin[0]*4 + new_number_bin[1]*2 + new_number_bin[2]


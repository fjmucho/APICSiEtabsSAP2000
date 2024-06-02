#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
# ************* 0 *************
EtabsAPI illustration: 0.0.1 
Autor: Francisco J.Mucho
Date: 25/03/21
Time:
Modulo: funciones de ayuda.
# ************* 0 *************
"""
import os, platform

# ************* 0 *************
def plataforma():
    return platform.system()
    
def limpiar():
    if platform.system()=="Windows":
        os.system('cls')
    else: 
        os.system('clear') 


# test
if __name__ == '__main__':
    print(platform.system())
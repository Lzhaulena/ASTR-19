# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:10:28 2026

@author: Lukas
"""

def f(x):
    return x**3 + 8

def main():
    x_value = 9
    result = f(x_value)
    
    print(f"The result of f({x_value}) is {result}")
    
    if result > 27:
        print("YAY!")

if __name__ == "__main__":
    main()
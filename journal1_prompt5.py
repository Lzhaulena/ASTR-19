# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 08:46:27 2026

@author: Lukas
"""

import numpy as np

def generate_sin_table():
    x_values = np.linspace(0, 2*np.pi, 1000)
    sin_values = np.sin(x_values)
    
    print(f"{'x':<15} | {'sin(x)':<15}")
    for x, sin_x in zip(x_values, sin_values):
        print(f"{x:<15.6f} | {sin_x:<15.6f}")
        
def main():
    print("generating sin(x) table...")
    generate_sin_table()
   
if __name__ == "__main__":
    main()
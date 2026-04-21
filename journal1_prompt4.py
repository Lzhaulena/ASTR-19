# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:25:12 2026

@author: Lukas
"""

class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
       
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.num_eyes = int(num_eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)
        
    def describe_animal(self):
        print("Animal Physical Characteristic:")
        print(f" - Arm length: {self.arm_length} meters")
        print(f" - Leg Length: {self.leg_length} meters")
        print(f" - Number of Eyes: {self.num_eyes}")
        print(f" - Has a Tail: {'yes' if self.has_tail else 'No'}")
        print(f" - Is furry: {'yes' if self.is_furry else 'No'}")
        
Red_Panda = FavoriteAnimal(arm_length=0.5, leg_length=0.5, num_eyes=2, has_tail=True, is_furry=True)

Red_Panda.describe_animal()
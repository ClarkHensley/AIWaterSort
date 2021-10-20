#!/usr/bin/env python3

import random

class Water:
    
    def __init__(self, colors, color_ids, empty):

        self.empty = empty
        if self.empty:
            self.id = -1
            self.payload = " "
        
        else:
            self.colorset = random.choice(colors)
            self.id = self.colorset[0]
            while self.id in color_ids:
                self.colorset = random.choice(colors)
                self.id = self.colorset[0]
    
            color_ids.append(self.id)
    
            self.color = self.colorset[1][0]
            self.back = self.colorset[1][1]
    
            self.payload = self.color + self.back + "\u23F9"
    
    def __str__(self):
        return self.payload


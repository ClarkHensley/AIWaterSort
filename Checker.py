#!/usr/bin/env python3

from Vial import Vial

def canMove(from_vial, to_vial):

    if from_vial.index == to_vial.index:
        return False
    
    elif from_vial.empty:
        return False

    elif to_vial.empty:
        return True
    
    elif to_vial.won:
        return False

    elif from_vial.color_list[from_vial.top].id == to_vial.color_list[to_vial.top].id and to_vial.top < to_vial.depth - 1:
        return True

    else:
        return False


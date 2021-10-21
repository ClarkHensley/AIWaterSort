#!/usr/bin/env python3

from Vial import Vial
from Water import Water
from Checker import canMove

class Display:

    def __init__(self, color_list, depth, vial_number, extra_vials):
        self.color_list = color_list
        self.depth = depth
        self.vial_number = vial_number
        self.extra_vials = extra_vials

        self.vials = []
        for i in range(self.vial_number - self.extra_vials):
            self.vials.append(Vial(self.color_list, self.depth, False, i))

        for i in range(self.extra_vials):
            self.vials.append(Vial(self.color_list, self.depth, True, self.vial_number + i))

    def transfer(self, from_ind, to_ind):

        # If the transfer can be made:
        if canMove(self.vials[from_ind], self.vials[to_ind]):

            from_bottom = self.vials[from_ind].getBottomOfTop()

            # Catching a Corner Case (No Idea)
            if self.vials[from_ind].won and self.vials[to_ind].empty:
                temp = self.vials[to_ind]
                self.vials[to_ind] = self.vials[from_ind]
                self.vials[from_ind] = temp

            else:

                while (self.vials[from_ind].top >= from_bottom and canMove(self.vials[from_ind], self.vials[to_ind])) or self.vials[to_ind].empty:
                    self.vials[to_ind].color_list[self.vials[to_ind].top + 1] = self.vials[from_ind].color_list[self.vials[from_ind].top]
    
                    if self.vials[to_ind].top < self.vials[to_ind].depth - 1:
                        self.vials[to_ind].incrementTop()
                    self.vials[from_ind].color_list[self.vials[from_ind].top] = Water(None, None, True)
                    if self.vials[from_ind].top > -1:
                        self.vials[from_ind].decrementTop()
                    self.vials[to_ind].update()
                    self.vials[from_ind].update()
    
        #return self.checkSolved()

    def checkSolved(self):
        for vial in self.vials:
            if not(vial.won):
                return False

        return True

    def show(self):
        print()
        for i in range(self.depth + 2):
            for j in range(len(self.vials)):
                print(self.vials[j].display[i], end = "\t")
            print()
        print()
        for i in range(len(self.vials)):
            print(" " + str(i + 1), end = "\t")


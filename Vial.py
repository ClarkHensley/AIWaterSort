#!/usr/bin/env python3

from colorama import Fore, Back
import random

from Water import Water

class Vial:

    def __init__(self, colors, depth, empty, index):

        self.depth = depth
        self.empty = empty
        self.index = index

        self.won = False
        self.oneColor = False
        self.top = 0

        self.color_list = []

        if self.empty:
            for _ in range(depth):
                self.color_list.append(Water(None, None, True)) 
            self.won = True
            self.top = -1

        else:
            for _ in range(depth):
                choice = random.randint(0, len(colors) - 1)
                chosen_color = colors.pop(choice)

                self.color_list.append(chosen_color)

            self.top = self.depth - 1

        self.display = []

        self.drawDisplay()
        
    def update(self):
        self.drawDisplay()
        self.checkWon()
        self.checkOneColor()
        self.checkEmpty()

    def drawDisplay(self):

        self.display = []
    
        while len(self.color_list) < self.depth:
           self.color_list.append(Water(None, None, True)) 

        self.display.append(Fore.BLACK + Back.WHITE + "\u2502" + " " + "\u2502")
        for i in range(self.depth - 1, -1, -1):
            self.display.append(Fore.BLACK + Back.WHITE + "\u2502" + str(self.color_list[i]) + Fore.BLACK + Back.WHITE + "\u2502")
        self.display.append(Fore.BLACK + Back.WHITE + "\u2514" + "\u2500" + "\u2518")

    def checkWon(self):
        self.won = False
        goal_id = self.color_list[0].id

        for color in self.color_list:
            if color.id != goal_id:
                return

        self.won = True

    def checkOneColor(self):
        if self.empty:
            self.oneColor = False

        elif self.won:
            self.oneColor = True
        
        else:
            return self.getBottomOfTop() == 0


    def getTop(self):
        return self.top

    def incrementTop(self):
        self.top = self.top + 1

    def decrementTop(self):
        self.top = self.top - 1

    def getBottomOfTop(self):
        curr_top = self.getTop()
        goal_id = self.color_list[curr_top].id
        for i in range(curr_top, -1, -1):
            if self.color_list[i - 1].id != goal_id:
                return i

    def getHeightOfTop(self):
        return self.getTop - self.getBottomOfTop + 1

    def checkEmpty(self):
        flag = True
        for i in range(len(self.color_list)):
            if self.color_list[i].id != -1:
                flag = False
                break
        self.empty = flag
        if flag:
            self.top = -1


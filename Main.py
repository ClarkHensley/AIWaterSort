#!/usr/bin/env python3

# Library Imports
import colorama
from colorama import Fore, Back
from os import name
import subprocess
import time

# Testing
import random

# Class Imports
from Water import Water
from Display import Display
from Checker import canMove

def main():

    # Constants
    # No MAGIC NUMBERS
    VIAL_DEPTH = 4
    VIAL_NUMBER = 7
    EXTRA_VIALS = 2

    color_permutations = []
    fronts = [Fore.BLACK, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    backs = [Back.BLACK, Back.RED, Back.YELLOW, Back.GREEN, Back.BLUE, Back.MAGENTA, Back.CYAN]
    
    for i in range(len(fronts)):
        for j in range(len(backs)):
            if not i == j:
                color_permutations.append((fronts[i], backs[j]))
    
    color_permutations = list(enumerate(color_permutations))

    # Command to clear the screen based on the operating system
    if name == "nt":
        clear_string = "cls"
    else:
        clear_string = "clear"
    
    subprocess.run(clear_string)

    colorama.init(autoreset = True)

    solved = False

    # Generate the colors for this iteration:
    color_list = []
    color_ids = []
    for _ in range(VIAL_NUMBER - EXTRA_VIALS):
        temp = Water(color_permutations, color_ids, False)
        for _ in range(VIAL_DEPTH):
            color_list.append(temp) 

    main_display = Display(color_list, VIAL_DEPTH, VIAL_NUMBER, EXTRA_VIALS)

    while not(solved):

        main_display.show()
        #throwaway = input()
        #time.sleep(1)
        
        From = int(input("\nMove From Vial: ")) - 1
        To = int(input("\nMove To Vial: ")) - 1
        #options = [i for i in range(VIAL_NUMBER)]
        #From = options.pop(random.randint(0, len(options) - 1))
        #To = options.pop(random.randint(0, len(options) - 1))
        
        if From != To:
            solved = main_display.transfer(From, To)
        #temp = select(main_display.vials)
        #solved = main_display.transfer(temp[0], temp[1])

        #subprocess.run(clear_string)

    subprocess.run(clear_string)
    main_display.show()

    print("\nCompleted! Good Job!")



def select(vials):

    from_ind = 0
    to_ind = 0
    while not(canMove(vials[from_ind], vials[to_ind])):
        from_ind = random.randint(0, len(vials) - 1)
        to_ind = random.randint(0, len(vials) - 1)
    return (from_ind, to_ind)


    """scores = []
    for i in range(len(vials)):
        for j in range(len(vials)):
            if not i == j:
                scores.append([(i, j), 0])
    
    scores = list(enumerate(scores))

    # If there are empty vials:
    hasEmpty = False
    empties = []
    for v in range(len(vials)):
        if vials[v].empty:
            hasEmpty = True
            empties.append(v)

    if hasEmpty:
        longest = []
        # Case 1, a vial has the longest continuous section.
        print("case1")
        for v in range(len(vials)):
            if not(vials[v].empty or vials[v].won):
                top = len(vials[v].color_list) - 1
                while vials[v].color_list[top].id == -1:
                    top -= 1

                bottom = top
                while vials[v].color_list[top].id == vials[v].color_list[bottom - 1].id:
                    bottom -= 1

                if bottom != 0:
                    longest.append((v, top - bottom + 1))

        max = (0, 0)
        single_longest = True
        for l in longest:
            if l[1] > max[1]:
                max = (l[0], l[1])
                single_longest = True
            if l[1] == max[1]:
                single_longest = False

        if single_longest:
            return (max[0], empties[0])

        # Case 2, a vial has only n Groups, groups, 2 and up:
        print("case2")
        for n in range(2, len(vials[v].color_list)):
            for v in range(len(vials)):
                if not(vials[v].empty or vials[v].won):
                    temp_list = vials[v].color_list[:]
                    i = 0
                    while len(temp_list) > 0:
                        temp_val = temp_list[0]
                        while temp_val in temp_list:
                            c = 0
                            while c < len(temp_list):
                                if temp_list[c] == temp_val:
                                    temp_list.pop(c)
                                else:
                                    c += 1
                        i += 1
                    if i == n:
                        return((v, empties[0]))

    else:
        # If there are no empties:
        
        # Case 3, a vial has a base of only one color:
        print("case3")
        for v in range(len(vials)):
            print(v)
            approved = True
            check = vials[v].color_list[0].id
            for i in range(len(vials[v].color_list)):
                if vials[v].color_list[i].id == check or vials[v].color_list[i].id == -1:
                    check = vials[v].color_list[i].id
                    if vials[v].color_list[i].id != -1 and i == len(vials[v].color_list) - 1:
                        approved = False
                    pass
                else:
                    approved = False
            if approved:
                print("approved")
                for w in range(len(vials)):
                    print(w)
                    if not v == w:
                        for i in range(len(vials[w].color_list) -1, -1, -1):
                            if vials[w].color_list[i].id == -1:
                                pass
                            elif vials[w].color_list[i].id == check:
                                print("w, v", w, v)
                                return (w, v)
                            else:
                                pass
    
        # Case 4, move same colors to lower value
        print("case4")
        tops = []
        for v in range(len(vials)):
            for c in range(len(vials[v].color_list) -1, -1, -1):
                if vials[v].color_list[c].id != -1:
                    tops.append((v, c))
                    break

        while len(tops) > 0:
            head = (0, 0)
            for t in tops:
                if t[1] > head[1]:
                    head = t
            
            for c in range(len(tops)):
                if tops[c] == head:
                    head = tops.pop(c)
                    break

            for v in range(len(vials)):
                if v != head[0]:
                    for c in range(len(vials[v].color_list) -1, -1, -1):
                        if vials[v].color_list[c].id != -1:
                            if vials[v].color_list[c].id == vials[head[0]].color_list[head[1]].id:
                                return((v, head[0]))
                            else:
                                break
    
                



    print("default")"""

                            

if __name__ == "__main__":
    main()


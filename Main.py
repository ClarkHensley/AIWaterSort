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
from Checker import canMove, optimizeMoves

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
        possible_moves = []
        recursiveSolve(main_display, possible_moves, [None], [], [], 1)
        #time.sleep(1)
        
        subprocess.run(clear_string)

    subprocess.run(clear_string)
    main_display.show()

    print("\nCompleted! Good Job!")

def recursiveSolve(main_display, possible_moves, old_list, solution, first_solution, steps):

    temp_display = Display(color_list, VIAL_DEPTH, VIAL_NUMBER, EXTRA_VIALS)
    temp_display.vials = main_display.vials[:]
    for move in old_list:
        temp_display.transfer(move.f, move.t)

    if temp_display.checkSolved():
        if len(first_solution) == 0:
            first_solution = old_list[:]
            solution = old_list[:]
        elif len(old_list) < len(solution):
            solution = old_list[:]

    if len(old_list) == 0:
        # End the loop, return here
        return

    else:
        optimize_moves(main_display, possible_moves)
        # copy the display to have a main one and a test one.
        # Save a state of possible_moves every time before the recursion, return to that after


if __name__ == "__main__":
    main()


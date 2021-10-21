#!/usr/bin/env python3

# Library Imports
import colorama
from colorama import Fore, Back
from os import name
import subprocess
import time
import heapq

# Testing
import random
import sys

# Class Imports
from Water import Water
from Display import Display
from Checker import canMove, optimizeMoves

def main():

    sys.setrecursionlimit(2000)

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

    main_display = Display(color_list[:], VIAL_DEPTH, VIAL_NUMBER, EXTRA_VIALS)

    while not(solved):

        main_display.show()
        best_solution = []
        first_solution = []
        steps = -1
        best_solution, first_solution = recursiveSolve(main_display, color_list, [], [], best_solution, first_solution, 1)
        #time.sleep(1)
        
        print(len(first_solution))
        print(first_solution)
        print(len(best_solution))
        print(best_solution)
        input()

        subprocess.run(clear_string)

    subprocess.run(clear_string)
    main_display.show()

    print("\nCompleted! Good Job!")

def recursiveSolve(curr_display, color_list, possible_moves, current_path, best_solution, first_solution, steps):

    #DEBUG
    print(steps)

    if curr_display.checkSolved():
        if len(first_solution) == 0:
            first_solution = current_path[:]
            best_solution = current_path[:]
        elif len(current_path) < len(best_solution):
            best_solution = current_path[:]

    #if len(old_list) == 0:
        # End the loop, return here
        #return

    optimizeMoves(curr_display, possible_moves)

    # heapify possible_moves
    heapq.heapify(possible_moves)

    while len(possible_moves) > 0:
        next_move = heapq.heappop(possible_moves)

        current_path.append(next_move) 

        new_display = Display(color_list[:], curr_display.depth, curr_display.vial_number, curr_display.extra_vials)
        new_display.vials = curr_display.vials[:]
        new_display.transfer(next_move.f, next_move.t)

        # ???
        lower_finished = recursiveSolve(new_display, color_list, [], current_path, best_solution, first_solution, steps + 1)
        heapq.heapify(possible_moves)
        del current_path

    if steps == 1:
        return best_solution, first_solution
    return True


if __name__ == "__main__":
    main()


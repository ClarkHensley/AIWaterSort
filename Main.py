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
from State import State
from Checker import canMove, optimizeMoves, scoreState

def main():

    sys.setrecursionlimit(20000)

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
        solution = []
        solution = recursiveSolve(main_display, color_list, [], [], solution, 1)
        #time.sleep(1)
        
        print(len(solution))
        print(solution)
        input()

        subprocess.run(clear_string)

    subprocess.run(clear_string)
    main_display.show()

    print("\nCompleted! Good Job!")

def recursiveSolve(curr_display, color_list, possible_moves, current_path, solution, steps):

    if curr_display.checkSolved():
        solution = current_path[:]
        return solution

    optimizeMoves(curr_display, possible_moves)

    # heapify possible_moves
    heapq.heapify(possible_moves)

    list_of_states = []
    while len(possible_moves) > 0:
        '''print(steps)
        for i in range(len(possible_moves)):
            print(steps)
            print("move " + str(i + 1))
            print(possible_moves[i].score)
            print(possible_moves[i].f)
            print(possible_moves[i].t)
            print()'''
        next_move = heapq.heappop(possible_moves)

        current_path.append(next_move) 

        new_display = Display(color_list[:], curr_display.depth, curr_display.vial_number, curr_display.extra_vials)
        new_display.vials = curr_display.vials[:]
        new_display.transfer(next_move.f, next_move.t)

        list_of_states.append(State(new_display, 0, current_path[:])) 
        scoreState(list_of_states[-1])
        
    heapq.heapify(list_of_states)
    while len(list_of_states) > 0:
        next_state = heapq.heappop(list_of_states)
        return recursiveSolve(next_state.state, color_list, [], next_state.path, solution, steps + 1)
    
    return "No Solution Could Be Found"


if __name__ == "__main__":
    main()


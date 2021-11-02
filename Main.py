#!/usr/bin/env python3

# Library Imports
import colorama
from colorama import Fore, Back
from os import name
import subprocess
import time
import heapq
from copy import deepcopy
import timeit

# Class Imports
from Water import Water
from Display import Display
from State import State
from Checker import canMove, optimizeMoves, scoreState, compareMoves, checkVisited

def main():

    # Constants
    # No MAGIC NUMBERS
    VIAL_DEPTH = 4
    VIAL_NUMBER = 14
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

    # Generate the colors for this iteration:
    color_list = []
    color_ids = []
    for _ in range(VIAL_NUMBER - EXTRA_VIALS):
        temp = Water(color_permutations, color_ids, False)
        for _ in range(VIAL_DEPTH):
            color_list.append(temp) 

    color_list_copy = deepcopy(color_list)
    main_display = Display(color_list_copy, VIAL_DEPTH, VIAL_NUMBER, EXTRA_VIALS)

    color_list_copy = deepcopy(color_list)
    curr_display = Display(color_list_copy, VIAL_DEPTH, VIAL_NUMBER, EXTRA_VIALS)

    del curr_display.vials
    curr_display.vials = deepcopy(main_display.vials)

    start = timeit.default_timer()    
    solution, stop = recursiveSolve(curr_display, color_list)

    if type(solution) == str:
        subprocess.run(clear_string)
        main_display.show()
        print(solution)

    else:

        subprocess.run(clear_string)
        print("\nInitial State:\n")
        main_display.show()
        time.sleep(0.5)

        for i in range(len(solution)):

            subprocess.run(clear_string)

            print("\nStep " + str(i + 1) + "\n")
            
            main_display.transfer(solution[i].f, solution[i].t)
            main_display.show()
    
            time.sleep(0.5)
    
        subprocess.run(clear_string)
        print("\nDone!\n")
        main_display.show()

        print("\nTime to find this solution: " + str(stop - start) + " seconds.")
        print("This Solution is: " + str(len(solution)) + " steps long.")
    
        print("\nCompleted! Good Job!\n")
    
def recursiveSolve(curr_display, color_list, current_path=[], visited_states = []):

    if curr_display.checkSolved():
        return current_path, timeit.default_timer()

    if len(current_path) > 0:
        if checkVisited(curr_display.check_list, visited_states): 
            return "Previously Visited State", None

    visited_states.append(deepcopy(curr_display.check_list))

    possible_moves = []
    optimizeMoves(curr_display, possible_moves)

    # heapify possible_moves
    heapq.heapify(possible_moves)

    list_of_states = []
    while len(possible_moves) > 0:
        next_move = heapq.heappop(possible_moves)

        color_list_copy = deepcopy(color_list)

        new_display = Display(color_list_copy, curr_display.depth, curr_display.vial_number, curr_display.extra_vials)
        del new_display.vials
        new_display.vials = deepcopy(curr_display.vials)
        new_display.transfer(next_move.f, next_move.t)

        new_path = deepcopy(current_path)
        new_path.append(next_move)
        list_of_states.append(State(new_display, 0, new_path)) 
        scoreState(list_of_states[-1])
        
    heapq.heapify(list_of_states)
    while len(list_of_states) > 0:

        # Display during the run!
        #subprocess.run("clear")
        #print("\n" + str(len(current_path)))
        #curr_display.show()
        #time.sleep(0.2)

        next_state = heapq.heappop(list_of_states)
        next_path = deepcopy(next_state.path)
        result, stop = recursiveSolve(next_state.state, color_list, next_path, visited_states)
        if type(result) != str:
            return result, stop

        heapq.heapify(list_of_states)
            
    return "No Solution Could Be Found", timeit.default_timer()


if __name__ == "__main__":
    main()


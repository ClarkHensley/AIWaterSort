#!/usr/bin/env python3

from copy import deepcopy
import subprocess

from Vial import Vial
from Move import Move

def canMove(from_vial, to_vial):

    if from_vial.index == to_vial.index:
        return False
    
    elif from_vial.empty:
        return False

    elif to_vial.empty:
        return True
    
    elif to_vial.won:
        return False

    elif from_vial.oneColor:
        return False

    elif from_vial.color_list[from_vial.top].id == to_vial.color_list[to_vial.top].id and to_vial.top < to_vial.depth - 1:
        return True

    else:
        return False

def compareMoves(first_move, second_move, first_color = None, second_color = None):
    if not(first_move.f == second_move.t):
        return False
    if not(first_move.t == second_move.f):
        return False
    if first_color is not None and second_color is not None:
        if not (first_color == second_color):
            return False

    return True

def optimizeMoves(main_display, possible_moves):
    
    for i in range(len(main_display.vials)):
        for j in range(len(main_display.vials)):
            if canMove(main_display.vials[i], main_display.vials[j]):
                possible_moves.append(Move(0, i, j))

    testMoves(possible_moves, main_display)

def testMoves(possible_moves, main_display):
    for move in possible_moves:
        # Test for One-Color vials
        if main_display.vials[move.f].oneColor:
            move.score += 1000000
        # Move appropriate tops into One-Color Vials
        elif main_display.vials[move.t].oneColor:
            move.score -= 10000
            move.score -= 100 * main_display.vials[move.f].getHeightOfTop()
            move.score += 50 * main_display.vials[move.f].numberOfChunks
        # Move the tallest tops to the lowest lows, with a slightly worse value for chunkiness
        else:
            move.score -= 20 * main_display.vials[move.t].top
            move.score += 4 * main_display.vials[move.f].top
            move.score += 1 * (main_display.vials[move.f].numberOfChunks + main_display.vials[move.t].numberOfChunks)  

def scoreState(state):
    
    if state.state.checkSolved():
        state.score -= 100000
        return

    for vial in state.state.vials:
        if vial.oneColor:
            state.score -= 25 * vial.getHeightOfTop()
        state.score -= 10 * vial.getHeightOfTop()
        state.score += 2 * vial.numberOfChunks 

def checkVisited(state, visited_states):

    for s in range(len(visited_states)):
        test_list = deepcopy(state)
        while len(test_list) > 0 and test_list[0] in visited_states[s]:
            del test_list[0]
        
        if len(test_list) == 0:
            return True

    return False


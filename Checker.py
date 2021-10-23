#!/usr/bin/env python3

from copy import deepcopy

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
            move.score += 100000
        # Move appropriate tops into One-Color Vials
        elif main_display.vials[move.t].oneColor:
            move.score -= 1000
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

def checkCycle(history, depth):

    for i in range(len(history)):
        temp = deepcopy(history)
        temp = temp[:i]
        for j in range(len(temp)):
            if history[i].f == temp[j].f and history[i].t == temp[j].t:
                hist_ind_new = i
                hist_ind_prev = j
                size = 1
                while hist_ind_new < len(history):
                    i += 1
                    j += 1
                    if history[i].f == temp[j].f and history[i].t == temp[j].t:
                        size += 1
                        if size > depth:
                            return True
                    else:
                        break
    return False
                
        

    '''values = []
    pairs = []
    pairs = set(pairs)
    for i, move in enumerate(history):
        for old_move in values:
            if move.f == old_move.f and move.t == old_move.t:
                pairs.add(i)
        values.append(move)'''

    pairs = list(pairs)
    print(pairs)
    size = 0
    for num in range(1, len(pairs)):
        if pairs[num - 1] == pairs[num]:
            size += 1
            if size > depth:
                #DEBUG
                print("Stuck in a loop")
                return True
        else:
            size = 0

    return False


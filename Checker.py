#!/usr/bin/env python3

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
        if main_display.vials[moves.f].oneColor:
            move.score += 100000
        # Move appropriate tops into One-Color Vials
        elif main_display.vials[moves.t].oneColor:
            move.score -= 1000
            move.score -= 100 * main_display.vials[moves.f].getHeightOfTop()
            move.score += 50 * main_display.vials[moves.f].numberOfChunks
        # Move the tallest tops to the lowest lows, with a slightly worse value for chunkiness
        else:
            move.score -= 20 * main_display.vials[moves.f].top
            move.score += 4 * main_display.vials[moves.t].top
            move.score += 1 * (main_display.vials[moves.f].numberOfChunks + main_display.vials[moves.t].numberOfChunks)  


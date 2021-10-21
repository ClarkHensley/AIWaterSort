#!/usr/bin/env python3

class Move:

    def __init__(self, score, f, t):
        self.score = score
        self.f = f
        self.t = t

    def __lt__(self, other):
        return self.score < other.score
    def __le__(self, other):
        return self.score <= other.score
    def __gt__(self, other):
        return self.score > other.score
    def __ge__(self, other):
        return self.score >= other.score
    def __eq__(self, other):
        return self.score == other.score
    def __ne__(self, other):
        return self.score != other.score


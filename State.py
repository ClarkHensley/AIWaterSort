#!/usr/bin/env python3

class State:

    def __init__(self, state, score, path):
        self.state = state
        self.score = score
        self.path = path

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


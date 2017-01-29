#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Solving Week 2 Assignment - n-puzzle game

Author: Bruno G. Eilliar

Notes:
    - Code for grading (everything must be on a single file)
    - 'UDLR' stands for  [‘Up’, ‘Down’, ‘Left’, ‘Right’]
    - Breadth-First Search. Enqueue in UDLR order; dequeuing results in UDLR order.
    - Depth-First Search. Push onto the stack in reverse-UDLR order; popping off results in UDLR order.
"""

import sys, ast, math

######################################################
# Classes
######################################################
class State(object):
    def __init__(self, initialState):
        self.iState = initialState
        self.currentState = initialState
        self.dim = len(initialState)    # State Dimension
        self.parent = None

    def current(self):
        return self.currentState

    def parent(self):
        pass

    def children(self):
        pass

    def get_legal_moves(self):
        moves = []
        # Size of the board
        n = math.sqrt(self.dim)
        # Find empty space position on board
        zero = self.find(0)
        # if not in row 0: can go U (pos -n)
        if not(zero <= n-1):
            moves.append("U")
        # if not in row n-1: can go D (pos +n)
        if not(zero >= (n**2) - n):
            moves.append("D")
        # if not in col 0: can go L (pos -1)
        if not(zero%n == 0): 
            moves.append("L")
        # if not in col n-1: can go R (pos +1)
        if not((zero+1)%n == 0):
            moves.append("R")

        return moves

    def find(self, value):
        return self.currentState.index(value)

class Queue(object):
    def __init__(self, state):
        pass

######################################################
# Functions
######################################################
def goalTest(state):
    """
    """
    goal = range(0, state.dim)
    if state.current() == goal:
        return True
    else:
        return False
    
def Breadth_First_Search(initialState, goalTest):
    """Use BFS to solve n-puzzle

    Inputs:
    - initialState ->
    - goalTest -> Function to test if the current state is the goal.
    Outputs:

    """
    frontier = Queue(initialState) # Queue.new(initialState)
    explored = Set.new()

    while not frontier.isEmpty():
        state = frontier.dequeue()
        explored.add(state)

        if goalTest(state):
            print("Success! Goal State: {}".format(state))
            return state

        for neighbor in state.neighbors():
            if (neighbor not in frontier) or (neighbor not in explored):
                frontier.enqueue(neighbor)

    return -1


if __name__ == '__main__':
    # Get input parameters
    arg_list = sys.argv
    solver = arg_list[1]
    initial_board = list(ast.literal_eval(arg_list[2]))
    print("Method: {}\tBoard Initial State: {}".format(solver, initial_board))

    state = State(initial_board)
    print("Is the initial state the goal state? {}".format(goalTest(state)))

    print("Zero position: {}".format(state.find(0)))

    print("Available moves: {}".format(state.get_legal_moves()))

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""



from itertools import cycle
import queue
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    from util import Stack


    stack = util.Stack() # calls the class stack with easy QOL
    #note that stack sometimes is frontier and frontier[] is just the directions of stack
    visited = [] #squares visited
    frontier = [] # squares around
    stack.push((problem.getStartState(),[])) #pushes the current square cords to the list in stack, also separates the coords x,y from direction strings(west and etc)
    g = True #loop
    while g == True: #loop
        if stack.isEmpty(): # check if stack is empty
            g = False # if the stack empty aka no start state(somehow) the code ends
        node,frontier = stack.pop() #node store the coords x and y while frontier is gonna store as a string the position west, south and etc
        visited.append(node) # marks of the x and y coords as visited
        if problem.isGoalState(node): #with the goal state is = true the code ends
            g = False #ends the loop
            return frontier #no idea why but if I remove this the code stops working, thanks google!
        else: #if the goal is not achieved
            child = problem.getSuccessors(node) # we store the currents x and y children on child, this line gave me so much trouble I almost gave up, but my error was storing both direction and coords in the same variable
            for item in child: #for every item in child
                if item[0] not in visited and item[0] not in frontier: # it checks if the currently being check item in child was not visited and is not in the frontier
                    nextmove = frontier + [item[1]] #here it adds every other item in child(aka the directions) with the frontier directions to calculate the next possible move
                    print("next move: ", nextmove) # print that
                    stack.push((item[0],nextmove)) # pushes onto the stack the x and y cords and directions
    print("winning path: ", visited)
    #This code gave me a lot of trouble mainly because functions such as get state, get successor and so on not only gave x,y cords but also string which complicates when managing variables and lead to bugs.
    #depth first research is better for shorter mazes as in bigger mazes it doesnt nessecerally find the better path
    util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    from util import Queue
    #everything here is the same just changed the stack to queue

    queue = util.Queue() # calls the class stack with easy QOL
    #note that stack sometimes is frontier and frontier[] is just the directions of stack
    visited = [] #squares visited
    frontier = [] # squares around
    queue.push((problem.getStartState(),[])) #pushes the current square cords to the list in stack, also separates the coords x,y from direction strings(west and etc)
    g = True #loop
    while g == True: #loop
        if queue.isEmpty(): # check if stack is empty
            g = False # if the stack empty aka no start state(somehow) the code ends
        node,frontier = queue.pop() #node store the coords x and y while frontier is gonna store as a string the position west, south and etc
        visited.append(node) # marks of the x and y coords as visited
        if problem.isGoalState(node): #with the goal state is = true the code ends
            g = False #ends the loop
            return frontier #no idea why but if I remove this the code stops working, thanks google!
        else: #if the goal is not achieved
            child = problem.getSuccessors(node) # we store the currents x and y children on child, this line gave me so much trouble I almost gave up, but my error was storing both direction and coords in the same variable
            for item in child: #for every item in child
                if item[0] not in visited and item[0] not in frontier: # it checks if the currently being check item in child was not visited and is not in the frontier
                    nextmove = frontier + [item[1]] #here it adds every other item in child(aka the directions) with the frontier directions to calculate the next possible move
                    print("next move: ", nextmove) # print that
                    queue.push((item[0],nextmove)) # pushes onto the stack the x and y cords and directions
    print("winning path: ", visited)
    #This code gave me a lot of trouble mainly because functions such as get state, get successor and so on not only gave x,y cords but also string which complicates when managing variables and lead to bugs.
    #breath first reasearch is better for bigger mazes as it normaly finds a better path than depth first research and it finds it quicker
    util.raiseNotDefined()
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    # print("Hello World")
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # print("Test:", problem.getSuccessors(problem.getStartState())[0][2])
    stack = Stack()
    stack.push((problem.getStartState(), []))
    visited = [problem.getStartState()]
    while True:
        if stack.isEmpty():
            break
        currentNode = stack.pop()
        visited.append(currentNode[0])
        if problem.isGoalState(currentNode[0]):
            break
        for successor in problem.getSuccessors(currentNode[0]):
            if successor[0] not in visited:
                # print("Successor:", successor)
                newMoveList = currentNode[1].copy()
                newMoveList.append(successor[1])
                stack.push((successor[0], newMoveList))
    moves = []
    # print(currentNode)
    if currentNode[1][0] == 'S' or currentNode[1][0] == 'N' or currentNode[1][0] == 'E' or currentNode[1][0] == 'W':
        for move in currentNode[1]:
            if move == 'North':
                moves.append(Directions.NORTH)
            elif move == 'South':
                moves.append(Directions.SOUTH)
            elif move == 'East':
                moves.append(Directions.EAST)
            elif move == 'West':
                moves.append(Directions.WEST)
    else:
        for move in currentNode[1]:
            moves.append(move)
    return moves
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue
    queue = Queue()
    queue.push((problem.getStartState(), []))
    visited = [problem.getStartState()]
    while True:
        if queue.isEmpty():
            break
        currentNode = queue.pop()
        while (not queue.isEmpty()) and (currentNode[0] in visited):
            currentNode = queue.pop()
        visited.append(currentNode[0])
        if problem.isGoalState(currentNode[0]):
            break
        for successor in problem.getSuccessors(currentNode[0]):
            if successor[0] not in visited:
                newMoveList = currentNode[1].copy()
                newMoveList.append(successor[1])
                queue.push((successor[0], newMoveList))
    moves = []
    if currentNode[1][0] == 'S' or currentNode[1][0] == 'N' or currentNode[1][0] == 'E' or currentNode[1][0] == 'W':
        for move in currentNode[1]:
            if move == 'North':
                moves.append(Directions.NORTH)
            elif move == 'South':
                moves.append(Directions.SOUTH)
            elif move == 'East':
                moves.append(Directions.EAST)
            elif move == 'West':
                moves.append(Directions.WEST)
    else:
        for move in currentNode[1]:
            moves.append(move)
    return moves
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue
    queue = PriorityQueue()
    queue.push((problem.getStartState(), [], 0), 0)
    visited = [problem.getStartState()]
    while True:
        if queue.isEmpty():
            break
        currentNode = queue.pop()
        while (not queue.isEmpty()) and (currentNode[0] in visited):
            currentNode = queue.pop()
        visited.append(currentNode[0])
        if problem.isGoalState(currentNode[0]):
            break
        for successor in problem.getSuccessors(currentNode[0]):
            if successor[0] not in visited:
                newMoveList = currentNode[1].copy()
                newMoveList.append(successor[1])
                queue.push((successor[0], newMoveList, currentNode[2] + successor[2]), currentNode[2] + successor[2])
    moves = []
    if currentNode[1][0] == 'S' or currentNode[1][0] == 'N' or currentNode[1][0] == 'E' or currentNode[1][0] == 'W':
        for move in currentNode[1]:
            if move == 'North':
                moves.append(Directions.NORTH)
            elif move == 'South':
                moves.append(Directions.SOUTH)
            elif move == 'East':
                moves.append(Directions.EAST)
            elif move == 'West':
                moves.append(Directions.WEST)
    else:
        for move in currentNode[1]:
            moves.append(move)
    return moves
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue
    queue = PriorityQueue()
    queue.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))
    visited = [problem.getStartState()]
    while True:
        if queue.isEmpty():
            break
        currentNode = queue.pop()
        while (not queue.isEmpty()) and (currentNode[0] in visited):
            currentNode = queue.pop()
        # print(currentNode)
        visited.append(currentNode[0])
        if problem.isGoalState(currentNode[0]):
            break
        for successor in problem.getSuccessors(currentNode[0]):
            if successor[0] not in visited:
                newMoveList = currentNode[1].copy()
                newMoveList.append(successor[1])
                queue.push((successor[0], newMoveList, currentNode[2] + successor[2]), currentNode[2] + successor[2] + heuristic(successor[0], problem))
    moves = []
    if currentNode[1][0] == 'S' or currentNode[1][0] == 'N' or currentNode[1][0] == 'E' or currentNode[1][0] == 'W':
        for move in currentNode[1]:
            if move == 'North':
                moves.append(Directions.NORTH)
            elif move == 'South':
                moves.append(Directions.SOUTH)
            elif move == 'East':
                moves.append(Directions.EAST)
            elif move == 'West':
                moves.append(Directions.WEST)
    else:
        for move in currentNode[1]:
            moves.append(move)
    return moves
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

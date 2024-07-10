# @author: seanpcox

# Using numpy for its array and permutation functionality
import numpy as np
from numpy.random import permutation

'''
Question: You are given a 2D array that represents a maze. It can have 2 values - 0 and 1. 
1 represents a wall and 0 represents a path. 
The objective of the maze is to reach the bottom right corner, or A[A.length-1][A.length-1]. 
You start from A[0][0] and can only go in 4 directions - up, down, left or right. Find if a path exists.
'''

# Root function to check valid input and initiate maze traversal
def solveMaze(m):
    if len(m) == 0 or len(m[0]) == 0:
        raise Exception("Invalid maze supplied!")
    else:
        return solveMazeRecursion(m,0,0)

# Function to print puzzle in a readable format
def printPuzzle(m):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in m]))
    print()

# Recursive function to solve the maze problem
def solveMazeRecursion(m,i,j):
    # Check position is in bounds
    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]):
        return False
    
    # Check it is a valid position to move to
    if m[i][j] != 0:
        return False
    
    # Mark the current position as currently visiting
    m[i][j] = '2'
    
    # If we have reached the bottom right corner we have solved the maze, return true
    if(i == len(m)-1 and j == len(m)-1):
        return True
    
    # The four directions we can move in
    nextPositions = ((0,1),(1,0),(0,-1),(-1,0))

    # Search for a path in each direction
    # Looping through the positions randomly to help ensure program operates correctly
    for r in permutation(4):
        # If we found a valid path return true
        if solveMazeRecursion(m,i+nextPositions[r][0],j+nextPositions[r][1]):
            return True
    
    # Mark current position as visited, we do not need to check it again
    m[i][j] = '3'
    
    # We tried each position and could not find a valid path
    return False

'''
Test Cases
'''

testCase1 = np.array([
        [0,1,1,1],
        [0,0,0,1],
        [1,0,0,1],
        [1,1,0,0]
    ])

testCase2 = np.array([
        [0,1,1,1],
        [0,0,0,1],
        [1,0,0,1],
        [1,1,0,1]
    ])

testCase3 = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

testCase4 = np.array([[0]])

testCase5 = np.array([[1]])

testCase6 = np.array([[1,0],
                      [0,0]])

testCase7 = np.array([[]])

testCases = [testCase1, testCase2,testCase3,testCase4,testCase5,testCase6,testCase7]

for testCase in testCases:
    try:
        print(solveMaze(testCase))
        printPuzzle(testCase)
    except Exception as e:
        print(e)
        
'''
Clarifications:
    * What should be returned? True if a path exists else False
    * What if more than one path exists? That is fine, return True
    * Can I assume a valid array will be supplied? Yes
    
Solution:
    * We will use backtracking here
    * If we are at a zero value we will check if we can go right, down, left, or up
    * This will be determined by a zero being present or not at these positions
    * If we cannot find a zero we will backtrack to the previous position
    * We will keep track of positions already visited to avoid cycling in a loop
    * We will keep track of positions already visited in-place to keep space complexity to O(1)
    * We will use 2 to represent currently visiting and 3 to represent visited
    * We must check we do not go out of the bounds of the puzzle 
'''        
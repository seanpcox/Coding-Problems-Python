# @author: seanpcox

'''

Question
--------
Design a solution for a Sudoku puzzle

'''

# We need to use the math library for square root functionality
import math
# Use numpy for arrays
import numpy

# Global variables
sSize = 1
rVals = [[]]
cVals = [[]]
bVals = [[]]

# Function to print puzzle in a readable format
def printPuzzle(m):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in m]))
    print()

# Function to reset any global values from previously input puzzles
def initPuzzle(m):
    # Record the N size of the N*N matrix
    global sSize
    sSize = len(m)
    
    # Record used values in each row: -1 fixed, 0 available, 1 used
    global rVals 
    rVals = numpy.zeros(shape=(sSize,sSize)).astype(bool)
    
    # Record used values in each column: -1 fixed, 0 available, 1 used
    global cVals 
    cVals = numpy.zeros(shape=(sSize,sSize)).astype(bool)
    
    # Record used values in each box: -1 fixed, 0 available, 1 used
    global bVals 
    bVals = numpy.zeros(shape=(sSize,sSize)).astype(bool)
    
    # Mark all values supplied with the puzzle
    markFixedValues(m)

# Method to get the box index for a position i and j
def getBoxIndex(i, j):
    # Note the operator // means floor divide
    boxIndex = i // math.sqrt(sSize) + ((j // math.sqrt(sSize)) * math.sqrt(sSize))
    # We need an integer, not a float created by floor divide, returned for list index access
    return int(boxIndex)

# Function to set a value as used or unused at a particular row, column, and box
def setUsedValue(m,i,j,isSet):
    # Note: We subtract 1 from the value due to zero indexing
    rVals[i][m[i][j] - 1] = isSet
    cVals[j][m[i][j] - 1] = isSet
    bVals[getBoxIndex(i,j)][m[i][j] - 1] = isSet

# Function to determine if a value may be used at a particular row, column, and box
def isValid(x,i,j):
    # Note: We subtract 1 from the value due to zero indexing in our lists
    if rVals[i][x - 1]:
        return False
    if cVals[j][x - 1]:
        return False
    if bVals[getBoxIndex(i,j)][x - 1]:
        return False
    return True

# Method to note the fixed values in our puzzle
def markFixedValues(m):
    for j in range(sSize):
        for i in range(sSize):
            # If we have a non zero value this value is fixed in the puzzle and cannot be altered
            if m[i][j] > 0:
                # Check that the value is valid in that particular row, column, and box
                if not isValid(m[i][j],i,j):
                    raise Exception("Invalid Sudoku Puzzle! Supplied Values Fail!")
                
                # Set that value used in that particular row, column, and box
                setUsedValue(m,i,j,True)
                # We use negative values to mark fixed values so we know not to update them
                m[i][j] = 0 - m[i][j]

# Recursive function to solve Sudoku puzzle
def sudokuRecursion(m,i,j):
    # If i is equal to the puzzle size then we need to move on to the next column
    if i == sSize:
        i = 0
        j += 1
    
    # Exit condition if end of puzzle, puzzled solved successfully
    if j == sSize:
        return True
    
    # If a value is negative it is a fixed value so we do not alter it but move to the next position
    if m[i][j] < 0:
        return sudokuRecursion(m,i+1,j)
    
    # We attempt all values for a position from 1 to N (in an N*N puzzle)
    for x in range(sSize):
        # We add 1 to the value as range beings at 0
        x += 1
        # Check this value may be used in that particular row, column, and box
        if isValid(x,i,j):
            # Set the value in the puzzle
            m[i][j] = x
            # Set the value used in that particular row, column, and box
            setUsedValue(m, i, j, True)
            
            # Move on to the next position
            result = sudokuRecursion(m,i+1,j)
            
            # If the result is true we have reached the end and solved the puzzle so return
            if result:
                return True
            # Else this value does not work to find a solution so we un-set it and update the puzzle
            else:
                setUsedValue(m, i, j, False)
                m[i][j] = 0

    # We have attempted all values for a position and none are valid so return false
    # If we have reached the first position then this puzzle cannot be solved
    return False

# Root function to solve an N squared * N squared Sudoku puzzle
def sudoku(m):
    initPuzzle(m)
    if not sudokuRecursion(m,0,0):
        raise Exception("Invalid Sudoku Puzzle! No Solution Possible!")
    return

'''

Test Cases
----------

'''

empty1X1TestCase = numpy.zeros(shape=(1,1), dtype=int)

empty4X4TestCase = numpy.zeros(shape=(4,4), dtype=int)

empty9X9TestCase = numpy.zeros(shape=(9,9), dtype=int)

empty16X16TestCase = numpy.zeros(shape=(16,16), dtype=int)

empty25X25TestCase = numpy.zeros(shape=(25,25), dtype=int)

valid4X4TestCase = numpy.array([
    [1, 2, 0, 0],
    [3, 4, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])

valid9X9TestCase = numpy.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

invalid4X4TestCase1 = numpy.array([
    [1, 2, 3, 0],
    [3, 4, 2, 1],
    [4, 3, 1, 2],
    [2, 1, 0, 4]
])

invalid4X4TestCase2 = numpy.array([
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
])

testCases = [empty1X1TestCase, empty4X4TestCase, empty9X9TestCase, empty16X16TestCase, 
             valid4X4TestCase, valid9X9TestCase, invalid4X4TestCase1, invalid4X4TestCase2]


# Run Test Cases Through Solution
for testCase in testCases:
    try:
        sudoku(testCase)
    except Exception as e:
        print(e)
    printPuzzle(testCase)

'''

Examples
--------
4 * 4

[
    [1, 0, 0, 4],
    [0, 0, 3, 0],
    [0, 3, 0, 0],
    [4, 0, 0, 2]
]

9 * 9

[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

Clarifications
-------------
* Is this a classic 9x9 puzzle? It can be any N squared * N squared size puzzle. 
* So (1^2) 1x1, (2^2) 4x4, (3^2) 9x9, (4^2) 16x16 etc? Yes
* Can we assume the matrix will be of a correct size? Yes
* Will there be pre-filled entries? There can be, or it may be empty to start
* What will represent a non pre-filled position? 0
* Will the input, with pre-filled values, always have a solution? No
* What to do in case of an input with no solution? Throw an error

Solution
--------
* We will use backtracking for this problem
* We will solve the puzzle in-place in the input matrix
* We will need to keep track of what values have already been used in each row, column, and box
* We will need to store the fixed values in the input, so we do not override them when solving
* We will use negatives to represent fixed values in the matrix
* For each empty position we will attempt the values 1 -> N (where N*N is the size of the puzzle)
* We will only try values that have not already been used in that position's row, column, and box
* If we can find no valid value for a position then we need to go back and try a different value for the previous position (backtracking)
* If we can not get to the last position this way that means the puzzle is invalid and we throw an error
* Row and Column positions are provided, but we need a calculation to find which box a particular row and column belongs to
* Time Complexity worst case is O(n^(​n^2)​), where ​n​ is one dimension of the puzzle, in practice this is less due to contraints
* Space Complexity is O(n^2), where ​n​ is one dimension of the puzzle .We use this space both on the recursion stack and on the checkers.


Box Calculation
---------------

4 * 4 Sudoku

(i) // 2 (sqrt 4)
0,0,1,1
+
((j) // 2) * 2
0,0,2,2 

9 * 9 Sudoku

(i) // 3 (sqrt 9)
0,0,0,1,1,1,2,2,2
+
((j) // 3) * 3
0,0,0,3,3,3,6,6,6

N * N Sudoku

boxIndex = i // sqrt(N) + ((j // sqrt(N)) * sqrt(N))


'''
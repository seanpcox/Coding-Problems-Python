# @author: seanpcox

'''
Question: Given a number N, find the Nth Fibonacci number.
'''

# Function to calculate the Nth result in the Fibonacci sequence
def fibonacci(n):
    # If a negative N return error result
    if n < 0:
        return -1
    
    # Stores the last two calculated results of the Fibonacci sequence
    store = [0,1]
    
    # The first two results are fixed and already stored so return them directly if prompted
    if n < 2:
        return store[n]
    
    # Otherwise loop from 2 to N (inclusive) to calculate the Nth result
    # Note: __ indicates a throw-away/unused variable
    for __ in range(2,n+1,1):
        # result(N) = result(N-2) + result(N-1)
        nResult = store[0] + store[1]
        # Update our last two results store
        store[0] = store[1]
        store[1] = nResult
    
    # Return the answer, which is the latest value in our store
    return store[1]

'''
Test Cases 
'''

testCases = (-1,0,1,2,5,10,40)
results = (-1,0,1,1,5,55,102334155)

for i in range(len(testCases)):
    print(fibonacci(testCases[i]) == results[i])

'''
Clarifications:
    * The equation is N = (N-1) + (N-2) I believe? Correct
    * What to do in case of an invalid number, example < 0? Return -1
    * This can be done via recursion or dynamic programming, do you have a preference? The most efficient
    * Results can get very large with fibonacci, can I assume result will be in integer range? Yes, also note python can handle very large ints using variable byte length to store
    * Can I assume the first two numbers are 0 and 1? Yes
    * Can I assume the first index is 0, which would result in 0? Yes
    
Solution:
    * We will use dynamic programming to solve this. O(n) time, O(1) space
    * We will start with 0 and 1 as the first two numbers
    * We will then loop through from 2 -> N (if needed) to calculate the answer_challenge: O(n) time
    * We will store the previous two answers only, which we need to get the next answer: O(1) space
'''
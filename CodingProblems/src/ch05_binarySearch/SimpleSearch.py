# @author: seanpcox

'''
Question: Implement a simple binary search
'''

import numpy as np

# Function to find the index of a target in a sorted array
def binarySearch(t, a):
    # Check the input array is valid
    if len(a) == 0:
        return -1
    
    # Set our initial search start and end points
    s = 0
    e = len(a)
    
    # Ensure start is less or equal to end
    # Otherwise we have searched the array and not found the target
    while s <= e:
        # Find the mid point of our search scope
        mid = s + ((e - s) // 2)
        
        # If target is greater than our midpoint value, we can exclude all values to the left of array from search scope
        if t > a[mid]:
            s = mid + 1
        # If target is less than our midpoint value, we can exclude all values to the right of array from search scope
        elif t < a[mid]:
            e = mid - 1
        # Else we have found our target, return the index
        else:
            return mid
    
    # Target not found, return -1    
    return -1

'''
Test Cases
'''

testCase1 = np.array([1,2,3,4,5,6,7,8,9])
print(binarySearch(3,testCase1))
print(binarySearch(8,testCase1))
print(binarySearch(1,testCase1))
print(binarySearch(9,testCase1))
print(binarySearch(0,testCase1))

testCase2 = np.array([])
try:
    print(binarySearch(1,testCase2))
except Exception as e:
    print(e)

'''
Clarifications:
    * What will be the input? An array of integers
    * Will the array be sorted? Yes
    * What to do in case of an empty array? Raise an exception
    * What shall we return? The index of the target in the array
    * What shall we return if target is not in array? -1
    
Solution:
    * We will implement a simple binary search
    * Binary search is O(logn) time
'''
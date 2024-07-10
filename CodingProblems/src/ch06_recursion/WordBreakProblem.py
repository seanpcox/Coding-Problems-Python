# @author: seanpcox

'''
Question: Given a String S, which contains letters and no spaces, find if it can be broken it into valid words. 
Return one such combination of words. Assume you are provided a dictionary of English words.
'''

dictSet = {"i","like","man","mango","go","tan","tango","got","gob"}

# Root method to solve word break problem, check input and call recursive function
def wordBreakProblem(s):
    if len(s) == 0:
        raise Exception("Invalid input!")
    
    return workBreakRecursion(s, 0, [])

# Method to find a valid word in a string of letters given a start point
def workBreakRecursion(s, sp, result):
    # We have reached the end of the string, return result
    if sp == len(s):
        return result
    
    # Store our new word
    word = ""
    
    # Loop through each character from the listed start point in the string to find a word
    for i in range(sp, len(s), 1):
        # Append the new character to our test word
        word += s[i]
        
        # Check if our new word is a valid word
        if word in dictSet:
            # Add word to our result
            result.append(word)
            
            # Try and find the next word in our string, start point moves forward
            subResult = workBreakRecursion(s,i+1,result)
            
            # If we found new words then we can return
            if(len(subResult) > 0):
                return result
            # If we did not find more words then discard the last result and continue add characters to our new word
            # We may find another valid word that will then lead to other valid words further up the string
            else:
                result.pop()
    
    # If we have exhausted all characters in the string and not found a word return an empty list to indicate this        
    return []

'''
Test Cases
'''

s1 = "ilikemangotango"
s2 = "mangot"
s3 = "mango"
s4 = "mantangoi"
s5 = "mangoman";
s6 = "mangobman";
s7 = "milikemangotango"
s8 = "ilikemangotangoz"
s9 = "milikemangotangoz"
s10 = "ilikemangoztango"
s11 = ""

testCases = (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11)

for testCase in testCases:
    try:
        print(wordBreakProblem(testCase))
    except Exception as e:
        print(e)

'''
Clarifications:
    * What to return if there are no valid words to be created? Empty string
    * What to return if there are some words in string but there are remaining letters that don't? Empty string
    * What data structure is the dictionary in, can I assume a set? You can assume a set
    * What to do on invalid input, empty string? Return an error
    * How should the words be returned, can I use a list? Yes you can use a list
    
Solution:
    * We will use backtracking for this solution
    * Starting at the first letter we will check if it is in the dictionary
    * If so we will move to the next character and check if it is in the dictionary
    * If not we will store this value and keep adding letters to it until we come to a word in the dictionary
    * If we reach the end of the string and have not found a word we need to backtrack to the first character
    * We will add letters to the first character until we find another valid word, then from there we will start with next character in sequence
    * Repeat this until we get to the end of the string, if we do and the last combination of letters we have a solution, return words
    * Use a list to contain the words, we will need to be able to add and remove them as required
    * If we get to the end of string and could not find a list of word/s to use all the characters return empty string, no solution
'''
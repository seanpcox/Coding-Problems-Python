# @author: seanpcox

'''
Question: Given a sentence, reverse the words of the sentence.
'''

# Method to reverse the words in a string
def reverseWords(s):
    # Return original input if string empty or only one char
    if s == None or len(s) <= 1:
        return s
    
    # Result string is empty to begin
    rs = ""
    # Variable to contain each word in order
    word = ""
    
    # Use reverse traversal to check each string character
    for i in range(len(s) - 1, -1, -1):
        # If we encounter a space add it to the result
        if s[i] == " ":
            rs += s[i]
        # Else we have encountered a character    
        else:
            # Prepend the character to any existing, or new, word
            # Note prepend vs append ensures the word does not get reversed
            word = s[i] + word
            
            # If we are on the last string character or the next character is a space
            # Then we must append the word to the result
            if i == 0 or s[i-1] == " ":
                rs += word
                word = ""
    
    # Return the result
    return rs

'''
Test Cases
'''

# Define our test cases
testCases = [
    None,
    "",
    "sean",
    " sean  ",
    "hey sean",
    " hey sean",
    "hey sean ",
    "  how are you  sean? "
    ]

# Run our test cases
for testCase in testCases:
    print(testCase,"->",reverseWords(testCase))
    
'''
Clarifications:
    * Are we dealing with ASCII characters only? Yes
    * Do capitals or punctuation matter? No, just copy characters and punctuation as-is
    * Can the word contain multiple spaces between words? Yes
    * Can the word contain spaces before and after the sentence? Yes
    * What shall we do with None input or empty string input? Return as-is
    
Solution:
    * We will create a new string to hold the result. Python strings are immutable. O(n) space
    * We will use reverse traversal for this problem and loop through each string character once. O(n) time
    * If we encounter a space we will append it to our result
    * If we encounter a character we will prepend it (so it stays in correct order) to a word variable
    * If we have reached the end of the string or the next character will be a space we append the word to the result
    
'''
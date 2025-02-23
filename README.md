# Recursion

## Recursive function definitions and specifications

You will write five recursive functions for this lab. Each one is specified below. One example test will be given, but you should write 3 - 5 explicit tests for each function (think of various interesting cases when writing your tests!).

Note: You must write each function recursively in order to receive any credit, even if Gradescope’s tests pass. For this lab, you may not (and need not) define additional helper functions.

integerDivision(n, k) - The parameters n and k are positive integers (you may assume n is >= 0 and k is > 0). This function recursively returns the quotient (n // k) without explicitly using the // or / operators, or a pre-defined function.
### Example test
assert integerDivision(27,4) == 6
collectEvenInts(listOfInt) - The parameter listOfInt is a list containing positive integer values. This function will return a list containing only even values in listOfInt in the order that they appear in listOfInt. If there are no even values in listOfInt, then this function should return an empty list.
### Example test
assert collectEvenInts([1,2,3,4,5]) == [2,4]
countVowels(someString) - This function will take a string value (someString) and return the number of vowels (‘A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’) that exists in someString.
### Example test
assert countVowels("This Is A String") == 4
reverseString(s) - The parameter s is a string. This function will return a string in the reverse order of s. Note that the reverse of an empty string is an empty string.
### Example test
assert reverseString("CMPSC9") == "9CSPMC"
removeSubString(s, sub) - The parameters s and sub are strings that contain at least one character. This function will return a string where all occurrences of sub are removed in the order it appears in the string s (see example test below for an interesting case). Your solution SHOULD NOT use the string’s replace method and follow the three laws of recursion.
Example test
assert removeSubString("Lolololol", "lol") == "Loo"
# The first "lol" is removed, which reduces the string 
# to: "Loolol". Then the 2nd "lol" is removed, which 
# reduces the string to: "Loo"
testFile.py pytest
This file will contain unit tests using pytest to test if your functionality is correct. Write your own tests first in order to check the correctness of your recursive function. Again, Gradescope requires testFile.py to be submitted before running any autograded tests. You should write 3 - 5 tests per function.

"""
Given an array of integers, 
return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 

If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

arrayInput = [1, 2, 3, 4, 5]
#arrayInput = [3, 2, 1]
arrayOutput = []

i = 0
j = 0
mul = 1 # for the first number to not be multiplied by zero

while j < len(arrayInput) :
    while i < len(arrayInput) :
        if i == j :
            i = i + 1 # if i equals to j then they are the current number to not multiply
            continue
        mul = mul * arrayInput[i] # keeps multiplying
        i = i + 1
    arrayOutput.append(mul)
    mul = 1 # reset vars
    i = 0
    j = j + 1

print(arrayOutput)

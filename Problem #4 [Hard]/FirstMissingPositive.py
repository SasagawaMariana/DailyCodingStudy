"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

time (hh:mm:ss):    01:08:38 - first attempt
                    00:11:02 - second attempt (implementation of sort and commentaries)
"""

array = [3, 4, -1, 1]
#array = [1, 2, 0]

i = 0
size = len(array)
next_number = 0
stop = 0

print("organized list")
array.sort() # does the same as bubble sort
print(array)

i = 0
calc = 0
missing_number = 0

# someday this will be optimized
while i < size :
    if i < size - 1 :
        # if the compared numbers are negative then they dont fit as a missing positive
        if array[i] < 0 or array[i + 1] < 0 :
            i = i + 1
            continue
        else :
            calc = array[i + 1] - array[i]
            # if the substraction is greater than 1 then the number after the current one is the first missing
        if calc > 1 :
            missing_number = array[i] + 1
            break
    # if reaches the end and the substraction remains as 1 then the number after the last one is the first missing
    if (i == size - 1 and calc == 1) :
        missing_number = array[i] + 1
    i = i + 1

print("the missing number is ")
print(missing_number)
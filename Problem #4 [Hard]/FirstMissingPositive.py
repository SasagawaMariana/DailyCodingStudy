"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

time (hh:mm:ss): 01:08:38
"""

array = [3, 4, -1, 1]
#array = [1, 2, 0]

i = 0
size = len(array)
next_number = 0
stop = 0

# for now its gonna be a bubble sort
while i < size :
    if i < size - 1 :
        if array[i] > array[i + 1] :
            next_number = array[i + 1]
            array[i + 1] = array[i]
            array[i] = next_number
        else :
            stop = stop + 1
        i = i + 1
    else : 
        i = 0
    if stop == size :
        break

print("organized list")
print(array)

i = 0
calc = 0
missing_number = 0
while i < size :
    if i < size - 1 :
        if array[i] < 0 or array[i + 1] < 0 :
            #calc = array[i + 1] + array[i]
            i = i + 1
            continue
        else :
            calc = array[i + 1] - array[i]
        if calc > 1 :
            missing_number = array[i] + 1
            break
    if (i == size - 1 and calc == 1) :
        missing_number = array[i] + 1
    i = i + 1

print("the missing number is ")
print(missing_number)
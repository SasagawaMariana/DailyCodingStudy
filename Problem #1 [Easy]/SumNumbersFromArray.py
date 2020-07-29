"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

Bonus: Can you do this in one pass?
"""

k = 17
list = [10, 15, 3, 7]

i = 1
j = 0
b = False

while j < len(list) :
    while i < len(list) :
        if j == i : # dont let same number be add up
            i = i + 1
            continue
        s = list[j] + list[i]   # add current number to next one

        """
        # uncomment these lines to debug
        print("j:" + str(list[j]))
        print("i:" + str(list[i]))
        print("s:" + str(s))
        print()
        """
        if s == k : # if sum is equal to k, goes out the first while
            b = True
            break
        i = i + 1
    if b == True :  # since found sum, goes out the second while
        break
    j = j + 1
    i = 0   # after paired with current number reset second counter to start all over
print(b)
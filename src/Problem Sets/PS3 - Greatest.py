# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list):
    if len(list) == 0:
        return 0
    else:
        j = 0
        for i in list:
            if i > j:
                j = i
        return j




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    

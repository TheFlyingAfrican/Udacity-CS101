# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(num):
    #i = 0
    sum = 0
    #while i < len(num):
    #    sum += num[i]
    #    i += 1
    
    for e in num:
        sum += e
    return sum



print sum_list([1, 7, 4])
#>>> 12

#print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134


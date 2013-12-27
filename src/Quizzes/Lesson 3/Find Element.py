# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

#using enumerate
# def find_element(list, value):
#     for index, item in enumerate(list):
#         if item == value:
#             return index
#     return -1 

#using list index options
def find_element(list, value):
    #for item in list:
    if value in list:
        return list.index(value)
    return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
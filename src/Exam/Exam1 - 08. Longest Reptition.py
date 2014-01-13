# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition (list):
    if list == [] : return None
    elif len(list) == 1 : return list[0]
    else:
        max_count = 0
        max_element = None
        current_element = list[ 0]
        current_count = 1
        for i in range(1, len(list)):
            if list[i] == current_element:
                current_count += 1
            elif current_count > max_count:
                max_count = current_count
                max_element = list[i- 1]
                current_count = 1
                current_element = list[i]
            else:
                current_element = list[i]
        if current_count > max_count:
            max_count = current_count
            max_element = list[i- 1]

        return max_element
           
           
#         rep_count = {}
#         for element in list:
#             if element in rep_count:
#                 rep_count[element] += 1
#             else:
#                 rep_count[element] = 1
#         max_count = 0
#         for element in list:
#             if rep_count[element] > max_count:
#                 max_count = rep_count[element]
#                 max_element = element
#         return max_element




#For example,

print longest_repetition([2 ,2, 3,3 ,3])

print longest_repetition([2 ])

print longest_repetition([1 , 2, 2, 3 , 3, 3, 2 , 2, 1])
# 3

print longest_repetition(['a' , 'b', 'b', 'b' , 'c', 'd', 'd' , 'd'])
# b

print longest_repetition([1 ,2, 3,4 ,5])
# 1

print longest_repetition([])
# None
  

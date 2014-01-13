# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    i = 0
    found = False
    while i < len(index) and found == False :
        if index[i][0] == keyword:
            return index[i][1]
        else:
            i += 1
    if not found:
        return []

print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']


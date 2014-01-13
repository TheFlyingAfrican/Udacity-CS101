# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    return [[]] * nbuckets # wrong, makes a list of references to the same empty list
#     htable = []
#     for i in range(0, nbuckets):
#         htable.append([])
#     return htable
    
        
table = make_hashtable(10)
print table
table[0] = ['hello']
table[1] = ['bye']
print table



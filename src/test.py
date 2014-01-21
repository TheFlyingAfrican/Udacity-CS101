# table = [['a', 1],['b',2],['c',5]]
# 
# for e in table:
#     print e
#     if 'c' in e:
#         print 'found' + str(e[1])
        
# dict = {
#         'a':1,
#         'aa':2,
#         'aaa':3,
#         'bb':4,
#         'cc': {'name':'nick'}
#         }
# 
# print dict['c']
# 
# print 'a' in 'aa'

# graph = {'index.html' : ['aaa','bbb','ccc'],
#          'hummus.html' : ['ddd','eee','fff']}
# 
# print graph
# 
# for page in graph:
#     print graph[page]
# 
# row = [1,2,3,4]
# print row[:]
# row = []
# new_row =[[1]]
# row.append([1])
# new_row[0].append(2)
# 
# print row
# print new_row
# 
# for i in range(1,2):
#     print i
#     
# def test_proc(a,b,c):
#     "this is a test of documentation for test_proc"
#     return [a,b,c]
# 
# print test_proc(1,2,3)
# 
# 
# for j in range(10, 0, -1):
#     print j
# 
# print row


a = [1,2,3,4,5]
b = [5,6,7,3,2]

c = set(a)
c.add(9)
# print c
print c

print c.union(a)
print c.union
print dir(c)
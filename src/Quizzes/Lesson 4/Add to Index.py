# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    i = 0
    found = False
    while i < len(index) and found == False :
        if index[i][0] == keyword:
            found = True
            index[i][1].append(url)
        else:
            i += 1
    if found == False:
#         element = []
#         element.append(keyword)
#         element.append([url])
#         index.append(element)
        index.append([keyword,[url]])
        


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]



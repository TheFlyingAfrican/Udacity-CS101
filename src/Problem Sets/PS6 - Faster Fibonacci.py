#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    current = 1
    prev = 0
    while n > 1:
#         current,prev,n = current+prev,current,n-1
        a = current
        current = current + prev
        prev = a
        n -= 1
    return current
    



print fibonacci(36)
        

#print fibonacci(36)
#>>> 14930352
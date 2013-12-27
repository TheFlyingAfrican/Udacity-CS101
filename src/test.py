def print_abacus(value):
      #print int(str("%010d" % value)[4])
      for i in range(0, 10): 
          print "|"+"00000*****"[0:(10-int(str("%010d" % value)[i]))]+"   "+"00000*****"[10-int(str("%010d" % value)[i]):10]+"|"

#print_abacus(100)

# print str('%010d' % 10)
# print '%(language)s has %(#)03d quote types.' \
# % {'language': "Python", "#": 2}

print '%(test)s has %(xyz)s blah blahs.' % {'test' : 'hello', 'xyz' : 'world'}
# garbage collection
a = 5
#refcount=1
b = 5
#refcount=2
c = 5
#refcount=3

a = 10
#refcount=2
b = 10
#refcount=1
c = 10
#refcount=0
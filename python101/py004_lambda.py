print("lambda")
print('\n')
print((lambda i:i*5)(3))

print((lambda *args:sum(args))(5,7,12))

print((lambda *args : list(map(lambda i : i * 10,args)))  (11,22,33))


x = lambda i :i*5

print(x(7))
print('\n')

def myfunc (n):
    return lambda i:i*n

mydoubler = myfunc(2)

print(mydoubler(7))

mytriple = myfunc(3)

print(mytriple(7))
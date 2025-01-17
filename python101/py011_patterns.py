def star_maker(n,t=1):
    arr = []

    for i in range(1,n+1):
        arr.append("-"*(n-i)+ '*'*(2*i-1) + '-'*(n-i))

    for i in range(2,n+1):
        arr.append('-'*(n-(n-i+1)) + '*'*((2*n-i)-(i-1)) + '-' *(n-(n-i+1)))

    # for _ in range(t):
    for i in arr:            
        print(i*t)

star_maker(7,3)
def star_maker(n=1,t=1):
    arr = []

    for i in range(1,n+1):
        arr.append("-"*(n-i)+ '*'*(2*i-1) + '-'*(n-i))

    for i in range(2,n+1):
        arr.append('-'*(n-(n-i+1)) + '*'*((2*n-i)-(i-1)) + '-' *(n-(n-i+1)))

    # for _ in range(t):
    for i in arr:            
        print(i*t)

# star_maker(7,3)
# flag=True

while True:
    print("\n Menu")
    print("press 1 to make patterns")
    print("press 2 to exit")
    
    choice = input('Enter here:-')
    
    
    if choice == '2':
        print("Exiting this while loop interface...")
        break
        
    elif choice =='1':
        usr_input = int(input("Enter size of the star..."))
        usr_t = int(input('how many times....:-'))
        star_maker(usr_input,usr_t)
        
    else:
        print("Enter valid number, either 1 or 2 ...")
        # flag = False
        # print("nikal jaldi")
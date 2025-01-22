def finder(arr):
    dis_arr = arr
    uniq = list(set(arr))

    a_dict={}

    for i in uniq:
        a_dict[i]=0
        for j in dis_arr:
            if j==i:
                a_dict[i] +=1

    print(a_dict) 


while True:
    print()
    print('press 1 to find no. of repeats in a array :-')
    print('press 2 to exit :-')
    print()

    choice = input('press 1 or 2 :-')

    if choice=='2':
        print('Exiting program...')
        break

    elif choice=='1':
        usr = input("enter csv's for ur array :-")
        polished_usr = list(usr.split(','))
        # print(polished_usr)
        finder(polished_usr)

    else:
        print('invalid input,enter either 1 or 2 ')

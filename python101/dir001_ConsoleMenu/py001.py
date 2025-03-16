a_list=[]
a_dict={}

x = '*'*21
while True:
    print(f''' 
    {x}
    1. Show list
    2. Add item
    3. Delete item
    4. Exit
    5. Show Dictionary/object
    6. add to dictionary
    7. delete from dictionary
    {x}    
    ''')



    choice = int(input('👉 Enter the option:-'))

    if choice==4:
        print('Exiting this interface...')
        break

    elif choice==1:
        print(a_list)


    elif choice == 2:
        usr_input = input("item to be added:-").strip()
        if usr_input:  # Check if the input is not empty or just spaces
            a_list.append(usr_input)


    # elif choice==2:
    #     usr_input = input("item to be added:-").strip()
    #     if usr_input:
    #         pass
    #     else:
    #         a_list.append(usr_input)

    elif choice==3:
        usr_input = input("item to be deleted:-").strip()
        try:
            a_list.remove(usr_input)
        except Exception as e:
            print(f"an error named :{e}")


    elif choice==5:
        print(a_dict)

    elif choice==6:
        usr_input_key = str(input("enter the key:- ")) 
        usr_input_value = str(input("enter the value:- ")) 
        a_dict[f"{usr_input_key}"] = f"{usr_input_value}"

    elif choice==7:
            try:
                usr_input_key= str(input('which key do you want todelete/remove:- '))
                del a_dict[f'{usr_input_key}']
                print(f"now the dictionary is :- {a_dict}")
            except Exception as e:
                print(f"may be this key not found or {e}\n new syntax \n unexceptd error {type(e).__name__} - {e}")


    else:
        print("Select  a valid option from 1,2,3,4,5,6,7")
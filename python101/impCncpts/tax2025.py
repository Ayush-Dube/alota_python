# in the budget for 2025 , new tax slabs are introduced , lets see how much anybody has to pay as taxes



def calculate_tax(usr):
    slab1 = 400000
    slab2 = 800000
    slab3 = 1200000
    slab4 = 1600000
    slab5 = 2000000
    slab6 = 2400000
    
    if usr <= slab1:
        print('No tax')

    elif usr <= slab2:
        rate = 0.05
        tax = (usr - slab1) * rate

        print(f'ur tax is {tax}')

    elif usr <= slab3:
        rate = 0.1
        tax = (usr-slab2) * rate + 20000

        print(f"ur tax {tax}")

    elif usr <= slab4:
        rate = 0.15
        tax = (usr-slab3)*rate + 60000
        print(f"ur tax {tax}")

    elif usr<=slab5:
        rate = 0.2
        tax = (usr-slab4)*rate + 120000
        print(f"ur tax {tax}")

    elif usr<=slab6:
        rate = 0.25
        tax = (usr-slab5)*rate + 200000
        print(f"ur tax {tax}")
        
    elif usr > slab6:
        rate = .3
        tax = (usr - slab6)*rate +300000
        print(f"ur tax {tax}")


while True:
    print('press 1 to start')
    print('press 2 to exit')
    choice = int(input('Enter ur choice bwtween 1 and 2 :- '))

    if choice == 2:
        print('Exiting...')
        break

    elif choice ==1:
        usr = int(input('Enter ur income:-'))
        calculate_tax(usr)
    else:
        print('Enter valid option 1/2')

        
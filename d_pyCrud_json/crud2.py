# with open('txtStore.txt','a') as f :
#     f.write("apple"+'\n')


# with open('txtStore.txt','a') as f :
#     f.write("banana"+'\n')

# with open('txtStore.txt','a') as f:
#     f.write('kiwi'+ '\n')

# with open('txtStore.txt','a') as f:
#     f.write('Pineapple'+'\n')

data = [] 

def add_it(name):
    data.append(name)

print(data)
add_it('apple1new')    
add_it('apple2')    
add_it('apple3')    
add_it('apple4new')    

print(data)

# this will ovewrite the previous values

with open('txtStore.txt','w') as f:
    f.write(f'{data}')
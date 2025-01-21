print('hi')

a_dict = {}


arr = ['a2','b1','c3','a2','b1','c2','a1','b2','c3','a1','b3','c1','a2','b2','c1','a1','b','c2','e1'] 
#string mistake, intially u did not  usedd these' values as string.

for i in arr:
    a_dict[f"{i}"] = 1

print(a_dict)

dict2 = {
    'key1':'aname',
    'key2':'bname',
    'key3':'cname',
    'key4':'dname',
    'key5':'ename'
            
            }


# print(dict2['key3'])

for i in dict2:
    print(dict2[f"{i}"])
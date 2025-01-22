# print('hi')


# a_dict = {}


# arr = ['a2','b1','c3','a2','b1','c2','a1','b2','c3','a1','b3','c1','a2','b2','c1','a1','b','c2','e1'] 
# #string mistake, intially u did not  usedd these' values as string.

# for i in arr:
#     a_dict[f"{i}"] = 1

# print(a_dict)

# dict2 = {
#     'key1':'aname',
#     'key2':'bname',
#     'key3':'cname',
#     'key4':'dname',
#     'key5':'ename'
            
#             }


# print(dict2['key3'])

# for i in dict2:
#     print(dict2[f"{i}"])
#     print(dict2.get(i))  # using get method 

# print()

# print(type(dict2.keys()))
# print(dict2.values())


# for i in dict2.keys():
#     print(i)


# print(dict2.items())


# for k,v in dict2.items():   # unpack dictionary
#     print(f"custom key:{k} with value: {v}")

##main code starts from here
#menu like console for finding repeated values

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

# finder(['a','d','e','r','a','e','p','p'])

usr = input("enter csv's for ur array :")
polished_usr = list(usr.split(','))
# print(polished_usr)

finder(polished_usr)



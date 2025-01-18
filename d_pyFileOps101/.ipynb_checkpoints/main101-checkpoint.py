# file operations 
# os module 
# rawx

# file_path = "text1.txt"
# file_object = open('test1.txt')
# print(file_object.read())
# file_object.close()


file_name = 'counting.txt'

with open(file_name,'a') as f:
    for i in  range(1,11):
        f.write(f"{i}\n")



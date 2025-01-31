with open('numbers.txt','r+') as f :
    f.seek(5)
    data = f.read(5)
    f.seek(0,2)
    f.write('-inTheEnd')

    f.seek(0)
    data2 = f.read()
    print(data)
    print(data2)
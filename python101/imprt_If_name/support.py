#here many functions will be written , which we will use in other python files for operations


def finder(arr):

    dis_arr = arr
    uniq = list(set(dis_arr))
    adict = {}
    for i in uniq:
        adict[i]=0
        for j in dis_arr:
            if j==i:
                adict[i] +=1

    print(adict)

def wordlen(arr):
    res = []
    for i in arr:
        res.append(len(i))
    print(res)

def sqrit(arr):

    res= []
    for i in arr:
        res.append(i*i)

    print(res)

if __name__== "__main__":

    finder(['a','c','b','c',])

    finder([1,1,00,0,2,3,3,4,2])

    wordlen(['aaa','bbbbb','sada0a'])

    sqrit([1,2,5,9,10])
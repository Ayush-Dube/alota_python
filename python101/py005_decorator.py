def decoFun (anyF):
    def wrp():
        print("from here ,the function given will be used")
        res = anyF() *10
        print(f"some operation on base function was performed and {res} was acheived")

    return wrp    



def base1 ():
    a = 5
    return a


varVip = decoFun(base1)


varVip()
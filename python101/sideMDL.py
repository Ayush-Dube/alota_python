def info(a):
    print(f"\n1.Coming from sideMDL.py file")
    print(f"2.__name__ = {__name__}")
    print(f"3.Parameter given = {a}")
    
    
    
def data2(x):
    print(f"\n1.Different Method coming from sideMDL.py ")
    print(f"2.__name__= {__name__}")
    print(f"3.Para given = {x}")
    
    
def sumD(*args):
    print(f"\n{sum(args)}")
    
    
    

    
def sqr(*args):
    print(f"\n{list(map(lambda i:i*i,args))}")

    
#since u have define all ur functions above , there is a high change u would want to check them here in this file itself.
# if u keep the below code uncommented , this code will run in other file as well.

info("a1")
info("a2")


# if __name__ =='sideMDL':
    #code below this will not run in the other file where u will do the import 
    # but it will run fine in here, if u use this file to run 
    # if u run this file itself,everything will run fine always ,
    # its just using this main name thing, u have the option to exclude some part of your code from exporting to other file 
    # direct run , indirect run of import file
if __name__=='__main__':  
   
    
    data2('x1')

    sumD(11,99)
    sqr(4,5)
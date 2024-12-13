class NewUsr:
    def __init__(self,name,age,amount):
        self.__name = name
        self.__age = age 
        self.__amount = amount
        print(f"New User {self.__name} created with {self.__amount}")
    
    def credit(self,x=0):  
        if x > 0 or x == 0: 
            self.__amount += x
        else:
            print("credit amount has to be  positive integer value")
            
            
    def debit(self,y=0):
        if y>= 0 and y <= self.__amount:
            self.__amount -= y 
        else :
            print('insufficient ballance or use positive interger value')
            
            
    def get_amount(self):
        return self.__amount
    
    
    
nc1 = NewUsr('Aname',19,100)
nc2 = NewUsr('Bname',20,500)
nc3 = NewUsr('Cname',21,1100)

nc1.credit(100)
nc1.credit(123)
print(nc1.get_amount())

nc2.debit(501)
print(nc2.get_amount())

nc2.debit(499)
print(nc2.get_amount())
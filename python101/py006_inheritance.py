class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender 
        print("a person object created")
        # self.info()
        
    def info(self):#every method will require self reference
        print(f"this persons name is '{self.name}', {'he' if self.gender == 'male' else 'she'} is a {self.age} yrs {self.gender}")
        
        

        
class Soldier(Person):
    def __init__(self,name,age,gender,service,rank):   #write all para's that will be used
    #the moment u write a init method for subclass ,it will destroy auto inhertance and u would have to use super to use inheritance  
        super().__init__(name,age,gender)  #here only super para's ,no self
        self.service = service 
        self.rank = rank
        print("a soldier object created")
        # super().info()
    
    def info(self):
        print("soldier  info method ")
        #method extention of inhertited methods
        super().info()

    
class Player(Person):
    
    def __init__(self,name,age,gender,game): #yanha sb cahiye
        pass
    
        


        
# p1 = Person('adam',26,'male')        

# p2 = Person ('bella',24,'female')

s1= Soldier('Josh',31,'male','army','major')
s2= Soldier('Reema',29,'female','army','captian')

s2.info()
print('\n')
s1.info()


# s2.Person.info()



# print(f"  let's try 'value'   \"quoates escape\"")
# bug alert --> even if u give anything else other than female it will still type 'she'
# extend functionality of a method
# method over riding  bottom to top
#
#
#
#
#

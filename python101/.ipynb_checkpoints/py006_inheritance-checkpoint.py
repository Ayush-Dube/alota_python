class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender 
        print("a person object created")
        # self.info()
        
    def info(self):#every method will require self reference
        print(f"\n this persons name is '{self.name}', {'he' if self.gender == 'male' else 'she'} is a {self.age} yrs {self.gender}")
        
        

        
class Soldier(Person):
    def __init__(self,name,age,gender,service,rank):   #write all para's that will be used
    #the moment u write a init method for subclass ,it will destroy auto inhertance and u would have to use super to use inheritance  
        self.service = service 
        self.rank = rank
        print(" \n a soldier object created")
        super().__init__(name,age,gender)
        # super().info()
    
    def info(self):
        print("soldier  info method ")
    
class Player(Person):
    pass
    
        


        
# p1 = Person('adam',26,'male')        

# p2 = Person ('bella',24,'female')

s1= Soldier('Josh',31,'male','army','major')
s2= Soldier('Reema',29,'female','army','captian')

s2.info()


# print(f"  let's try 'value'   \"quoates escape\"")
# bug alert --> even if u give anything else other than female it will still type 'she'
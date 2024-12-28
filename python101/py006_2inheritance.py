class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender 
        print("a person object created")
        
        
    def info(self):
        print(f"this persons name is '{self.name}', {'he' if self.gender == 'male' else 'she'} is a {self.age} yrs {self.gender}")
       
        
        

        
class Soldier(Person):
    def __init__(self,name,age,gender,service,rank): 
        super().__init__(name,age,gender) 
        self.service = service 
        self.rank = rank
        print("a soldier object created")
        
    
    def info(self):
        print(f"soldier  info method from {self.service} as a {self.rank} ")        
        super().info()

        

    
class Player(Soldier):    
    def __init__(self,name,age,gender,game,service,rank):
        self.game = game
        super().__init__(name,age,gender,service,rank)  
        print('a Player object created')
    
    def info(self):
        # print( f"1. \n {Person.info(self)} 2. \n {Soldier.info(self)} 3 . \n owm method of class Player")
    
            print("1. ")
            Person.info(self)  # Just call the method
            print("2. ")
            Soldier.info(self)  # Just call the method
            print("3.")
            print(f"Own method of class Player: Plays {self.game}")


        
# p1 = Person('adam',26,'male')        

# p2 = Person ('bella',24,'female')

# s1= Soldier('Josh',31,'male','army','major')
# s2= Soldier('Reema',29,'female','army','captian')

# s2.info()
# print('\n')
# s1.info()

p1= Player('Sam',28,'female','Tae-kondo','airforce','Sgt')


print(p1.info())

# you might be geting none as output because the function is print but not returning anything ,chage it to return 

"""
 def info(self):
        print("1. ")
        Person.info(self)  # Just call the method
        print("2. ")
        Soldier.info(self)  # Just call the method
        print("3.")
        print(f"Own method of class Player: Plays {self.game}")
"""

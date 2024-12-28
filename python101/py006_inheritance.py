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
        # suppose u have multiple super classes then use that class name and its method Person.info()  ,  Player.info() --> this did not work , apparently use Person.info(self)

    
class Player(Person,Soldier):    


    def __init__(self,name,age,gender,game): #yanha sb cahiye  old and new
        self.game = game
        Person.__init__(name,age,gender)  #yanha only new para's and no self 
        Soldier.__init__(name,age,gender,service,rank)
        print('a Player object created')
    
    def info(self):
        # extending functionality of the super method
        # res = Person.info()
        # print(f"{res} and plays {self.game} ")  
        print(f"1. \n {Person.info()} 2. \n {Soldier.info()} 3 . \n owm method of class Player")

        
# p1 = Person('adam',26,'male')        

# p2 = Person ('bella',24,'female')

# s1= Soldier('Josh',31,'male','army','major')
# s2= Soldier('Reema',29,'female','army','captian')

# s2.info()
# print('\n')
# s1.info()

p1= Player('Sam',28,'female','Tae-kondo')

p1.info()



# print(f"  let's try 'value'   \"quoates escape\"")
# bug alert --> even if u give anything else other than female it will still type 'she'
# extend functionality of a method
# method over riding  bottom to top
#

"""
Issues in the Player Class:

- super().__init__(name, age, gender) in Player initializes only one superclass (Person) because of the MRO.

- In multiple inheritance, super() follows the MRO and doesn't call Soldier's constructor unless explicitly done.
- Your info method in Player attempts to directly call Person.info() and Soldier.info() but lacks proper context (self).
     - it is because there can be many objects with class person 
"""

"""
-Why Soldier.__init__() Isn't Called in Player:
     - The MRO for Player(Person, Soldier) :- Player → Person → Soldier → object
     - This means super().__init__() in the Player class calls Person.__init__() (the next in the MRO), and it skips the Soldier.__init__().
     
- To Call Both Parent Initializers Explicitly:  
     - class Player(Person, Soldier):

            def __init__(self, name, age, gender, game, service, rank):

                Person.__init__(self, name, age, gender)  # Explicitly call Person's constructor

                Soldier.__init__(self, name, age, gender, service, rank)  # Explicitly call Soldier's constructor
                self.game = game
                print("A Player object created")


"""


"""
- this code will create problem Player is trying to inherit from class Person and class Soldier , wher the class soldier itself is inherting from class Person .  there a MRO conflict will occur 
- to avoid this 
     - try inherting from two independent classses that are not inheriting each other .(this may work)
"""
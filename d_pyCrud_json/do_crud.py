class Player():
    def __init__(self,name,age,height,weight,education,game):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__education = education
        self.game = game

    def show_plyr(self):
        print(f"'name':{self.__name},'age':{self.__age},'height':{self.__height},'weight':{self.__weight},'education':{self.__education},'game':{self.game}")
        


p1 = Player('adam',25,171,66,'btech','Archery')

print(p1)
print(p1.game)
print(p1.show_plyr())
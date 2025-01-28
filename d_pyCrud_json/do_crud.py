import json
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

    def plyr_dict(self):
        return        {
            'name': self.__name,
            'age': self.__age,
            'height': self.__height,
            'weight': self.__weight,
            'education': self.__education,
            'game':self.game
        }
        
    def str_dict(self):
        # return f"""{
        #     {"name": self.__name, "age": self.__age, "height": self.__height, "weight": self.__weight, "education": self.__education, "game": self.game}
        # }"""
        
        # another way
        data = {
            "name":{self.__name},
            "age":{self.__age},
            "height":{self.__height},
            "weight":{self.weight},
            "education":{self.__education},
            "game":{self.game}
        }
        return json.dumps(data)

p1 = Player('Adam',25,171,66,'btech','Archery')
p2 = Player('Bella',21,163,61,'bsc','BasketBall')

print(p1)
print(p1.game)
p1.show_plyr()
p2.show_plyr()

pd1=p1.plyr_dict()
pd2=p2.plyr_dict()

print(pd1['name'])
print(pd2)

psd1 = p1.str_dict()
psd2 = p2.str_dict()

print(psd1)

print(pd1['age'],type(psd2))
print(psd2['age'])
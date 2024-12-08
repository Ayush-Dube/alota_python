car1 = {
    'brand': 'Toyota',
    'model': 'corolla',
    'year': '2023',
    # 'funStart':lambda:print(f'{brand}{model}will start now')  this will not work
    'funStart':lambda:print(f'will start now')  
    # it seems we can not write proper function with def keyword.  
}

car2 ={
    'brand':'Honda',
    'model':'Civic',
    'year':2009,
    'funStart':lambda:print(f'will start now')  

}
car3 ={
    'brand':'Ford',
    'model':'Endavour',
    'year':2015,
    'funStart':lambda:print(f'will start now')  

}
# all these object were written manually, imagine writing thousands of these 
# also wrting functions inside the object is tricky and inconveinent
# we wil observe the utility of classes espeacially for using functions wrapped inside the object while creating it instantly.

# print(car1)

# car1['funStart']()

# print(car1.year)
print(car1['year'])


class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__done() # this run it @ the time of intialisation

    #hidden function
    def __done(self):
        print(f'{self.brand} {self.model} was added ')    

    def callit(self):
        print(f'this function can be aceessed outside ,ur car is {self.year} model')    

    # unhidden function can be called outside as well    

   
   
   
car11 = Car('BMW','3 series',2018)
car22 = Car('Audi','A4',2017)
car33 = Car('Nissan','Altima',2020)

# use Capital 
# carr11 was inside  the class ,error

car11.callit()
car22.callit()
car33.callit()
# car33.done()

car44 = Car('Hyundai','Creata',2022)

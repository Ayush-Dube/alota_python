class Rectangle:
    def __init__(self,length,width):
        self.length = length 
        self.width = width 
        self.__done()

    def __done(self):
            print(f'object with class created -->L:{self.length},W:{self.width}')

    def area(self):
        print(self.length*self.width)   

    def perimeter(self):
        print(self.length+self.length+self.width+self.width)     


# r1 = Rectangle(1,2)        
# r2 = Rectangle(2,3)        
# r3 = Rectangle(11,22)        
       

# r1.area()
# r1.perimeter()

# print(r2)


a= int(input('enter length:'))
b= int(input('enter width:'))

r4 = Rectangle(a,b)
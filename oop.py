class Car:
    #constructor
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    #method
    def drive(self):
        print(self.brand,f"is my dream Car and {self.color} in color")

# create object
car1=Car("Lexus","White")
car1.drive()

car2=Car("Ferarri","Black")
car2.drive()

car3=Car("Buggati","Pink")
car3.drive()

class Bike:
    # constructor
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    # method
    def drive(self):
        print(self.brand,f"is my favourite bike and {self.color} in color")

# create object
bike1=Bike("Ducati","Red")
bike1.drive()

bike2=Bike("Yamaha","Black")
bike2.drive()

class Fruits:
    # constructor
    def __init__(self,type,color,price):
        self.type=type
        self.color=color
        self.price=price
    # method
    def display(self):
        print(self.type,f"is my favourite fruit,{self.color} in color and {self.price} shillings")

# create object 
fruits1=Fruits("Mangoe","Yellow","30")
fruits1.display()

fruits2=Fruits("Apple","Green","40")
fruits2.display()

fruits3=Fruits("Pineapple","Yellow","20")
fruits3.display()

fruits4=Fruits("Blueberry","Blue","30")
fruits4.display()

fruits5=Fruits("Strawberry","Red","50")
fruits5.display()

fruits6=Fruits("Orange","Orange","10")
fruits6.display()




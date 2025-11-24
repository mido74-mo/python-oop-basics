class Calculator:#parent  super  main
    #we will create the consturctor 
    #the constructor works when you make and object from the class

    def __init__(self):
        pass

    def sum(self , x, y):#these are methods(functions)
        print(x + y)

    def mul(self , x ,y):
        print(x * y)

#now we will create the objects that will replace (self) in methods

my_calc = Calculator()
my_calc.sum(5 , 6)


# now it is time for Inheritance 
# in python you can make mulitple Inheritance

class Scientific(Calculator): #child  subclass  drivedclass

    def power(self,x,y):
        print(x ** y)

x = Scientific()
x.sum(7,10)
x.mul(1,3)
x.power(5,6)
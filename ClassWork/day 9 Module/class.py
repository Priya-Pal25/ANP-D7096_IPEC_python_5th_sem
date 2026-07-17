# defining a class to perfrom operations on rectangle

class Rectangle:

    # member variable
    length = 0
    breath = 0

    # method to initialize data
    def initialize (self,l,b):
        self.length = l
        self.breadth = b
    
    # method to display data
    def display_data(self):
        print("-------------------------- Rectangle--------------------------------")
        print("Length: ",self.length,"cm")
        print("Breadth: ",self.breadth , "cm")
    
#-------------------------------------------------------------------------------------------
#-----------------------------------Main program--------------------------------------------

# object creaation
rect = Rectangle()
rect.initialize(20,50)
rect.display_data()

#---------------------------------------------------------------------------------------------

'''Output:
-------------------------- Rectangle--------------------------------
Length:  20 cm
Breadth:  50 cm
'''


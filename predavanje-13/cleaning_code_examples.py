"""
Cleaning code example
"""
import naming_practices.example_file as calcs

class Car:
    """
    Describes car by only color.
    """
    def __init__(self,color):
        self.color = color


my_car = Car('blue')

def crash(car1,car2):  #pylint: disable=unused-argument
    car1.color ='burnt'

crash(Car('red'), my_car)


print(calcs.sabiranje(5,10))

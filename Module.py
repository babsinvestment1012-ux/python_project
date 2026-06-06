import random
#print(random.randint(1,10))   #generic import, random is the module name
from  random import randint    #function import
#print(randint(10,20))

from  random import*   #universal import
#print(random())
#challenge

from random import randint
fuel = randint(10,25)
miles = randint(200,400)
mgp = fuel//miles
print("the car can travel "+ str(fuel//miles)+" miles per gallon.")
print("the car can travel "+ str(miles))
print("The car's fuel can hold "+str(fuel))

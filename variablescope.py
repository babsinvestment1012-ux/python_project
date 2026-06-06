#animal = "cat"   #global variable
def function_var():
    animal = 'dog'   #variable inside the local scope
    return animal

#print(animal)
#function_var()
print(function_var())

#variable is in local scope
def coffee_num():
    coffe="Spanish Latte"
    print(coffe)


coffee_num()

#variable is in global scope
def coffee_num():
    return coffe


coffe="Pistachio Latte"
#coffee_num()
print(coffee_num())

#u can use same variable scope for different scopes,either local/global
def furniture_num1():
    #global furniture   #this is use when u want to change the value of the global variable to local V
    furniture="Chair"
    print(furniture)
def furniture_num2():
    furniture="Dinning Table"
    print(furniture)


furniture="Table"
furniture_num1()
furniture_num2()
print(furniture)

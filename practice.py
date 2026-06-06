# def tax_price(price):
#     num=0.1
#     percentage=price*num
#     print(f"Taxb4sum:{percentage}")
#     return f"Total_sum: {percentage+price}"






# print(tax_price(500))


#self.items is the main inventory dictionary

#self.items[item] = quantity is the line that adds or updates each fruit inside that dictionary
# class Inventory:
#     def __init__(self):
#         self.items={}
        

#     def fruits(self,item,quantity):
#         if quantity>0:
#             self.items[item]=quantity
#             print(f"Added:{item}-{quantity}")
#         else:
#             self.items.pop(item, None)
#             print(f"Removed: {item} (quantity is 0)")
               
    
        

    
            
#this will function will print out the result from the def init
        # print(f"Updated Inventory:{self.items}")
        # print("-" * 30)
        

# So Always Remember:
# Use square brackets [] for accessing dictionary keys
# Use = for assignment
# Use == for comparison
# Use () only to call functions

# jp=Inventory()
# jp.fruits("Pawpaw",60)
# jp.fruits("Pawpaw",5)
# jp.fruits("Orange",50)
# jp.fruits("Orange",10)
# jp.fruits("Pear",40)
# jp.fruits("Galic",0)



# class StoreInventory:
#     def __init__(self):
#         self.items={}

    
#     def add_item(self,item, quantity):
#         if quantity > 0:
#             self.items[item]=self.items.get(item,0)+quantity
#             print(f"Added:{item}-{quantity}")
#         else:
#             self.items.pop(item,None)
#             print(f"Removed:{item} (quantity is 0)")


#         print(f"Updated Inventory:, {self.items}")
#         print("-"*30)




# store = StoreInventory()
# store.add_item("Mango", 10)
# store.add_item("Mango", 5)     # total should be 15
# store.add_item("Apple", 7)
# store.add_item("Pawpaw", 0)


# class MyNumbers:
#     def __iter__(self):
#         self.num = 1
#         return self

#     def __next__(self):
#         if self.num <= 3:
#             result = self.num
#             self.num += 1
#             return result
#         else:
#             raise StopIteration

# obj = MyNumbers()
# itr = iter(obj)


#Automatically calls next() behind the scenes
#Keeps going until Python sees StopIteration
#Prints each returned value

# for x in itr:
#     print(x)


# class Vehicle:
#     def __init__(self, brand,speed):
#         self.brand=brand
#         self.speed=speed
    
#     def info(self):
#         return f"{self.brand} has a total limit of {self.speed}"
    
# class Car(Vehicle):
#     def __init__(self, brand,speed,type):
#         super().__init__(brand,speed)
#         self.type=type

#     def info(self):
#         return f"{self.brand} can go up to {self.speed} km/h and is a {self.type} car."
    
# class Bike(Vehicle):
#     def __init__(self, brand,speed,colour):
#         super().__init__(brand,speed)
#         self.colour=colour

#     def info(self):
#         return f"{self.brand} has {self.speed} km/h\    with {self.colour} colour"
       



# rt1=Vehicle("Toyota",40)
# rt2=Car("Corolla",60,"Hatchback")
# rt3=Bike("Yamaha",50,"Suv")
# print(rt1.info())
# print(rt2.info())
# print(rt3.info())

#create a class product define a variable with name,and price.
# class Product:
#     def __init__(self,name,price):
#         self.name= name
#         self.price= price
# #create a method final_price 
#     def final_price(self):
#        return f"Product Details:{self.name}:{self.price}" 

# #create a child class called DiscountProduct and also define with a variable name, price and discount.
# class DiscountProduct(Product):
#     def __init__(self, name, price,discount):
#         super().__init__(name, price)
#         self.discount=discount

# #create another method called final_price  under under child class
#     def final_price(self):
#         get_discount = self.price * self.discount
#         price_after_discount=self.price - get_discount
#         return f"Price_after_Discount: {price_after_discount}"



# x=Product("Mango", 50)
# y=DiscountProduct("Apple",100,0.20)
# print(x.final_price())
# print(y.final_price())

    
#seq=[0,1,2,3,4,5,6,7,8,9,10]
# num={x for x in seq if x%2==0}
# print(num)

#define the variable seq

# def f_num(n,y):
#     return n%2==0
#     return y%2!=0
    

# seq=[0,1,2,3,4,5,6,7,8,9,10]
# even_num=filter(f_num,seq)
# odd_num=filter(f_num,)
# print(list(even_num))



# class Person:
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age

#     def describe(self):
#         return f"Name: {self.name}, Age: {self.age}"

# class Teacher(Person):
#     def __init__(self,name,age, grade):
#         super().__init__(name,age)
#         self.grade= grade
        
#     def describe(self):
#         return f"Name: {self.name}, Age: {self.age},Grade: {self.grade}"
    
    

# class Student(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject= subject

#     def describe(self):
#         return f"Student: {self.name}, Age: {self.age}, Subject: {self.subject}"
    

    

     
    

# a=Person("John Peter", 59)
# b=Teacher("Mike Phelan", 40, "Nursery")
# c=Student("Mike Anderson", 50,"Math")


# print(a.describe())
# print(b.describe())
# print(c.describe())




# items = {
#     "Rice": 10,
#     "Beans": 5,
#     "Oil": 7
# }
# total=0
# for i in items:
#     print(f"{i:<5}:{items[i]}")
#     total+=items[i]
# print("-"*10)
# print(f"Total:{total}")
# items["Garri"]=50
# if "Garri" not in items:
#     print(items)
# else:
#     print("Item not found.")



# items = {
#     "Rice": 10,
#     "Beans": 5,
#     "Oil": 7,
#     "Garri": 50
# }

# # Show all available items
# print("Available items:")
# for item in items:
#     print(f"- {item}")

# # Ask the user to enter an item name
# item_name = input("\nEnter the name of an item to check its price: ")

# # Check if it's in the dictionary
# if item_name in items:
#     print(f"{item_name} costs {items[item_name]}")
# else:
#     print("Item not found.")
    

# items = {
#     "Rice": 10,
#     "Beans": 5,
#     "Oil": 7
# }
# total=0
# for i in items:
#     print(f"{i:<5}:{items[i]}")
#     total+=items[i]
# print("-"*10)
# print(f"Total:{total}")
# if "Garri" not in items:
#     items["Garri"]=50
# print(items)

#update price for old item or add new item with new price.
# items = {
#     "Rice": 10,
#     "Beans": 5,
#     "Oil": 7
# }
# total=0
# print("Item list:")
# for i in items:
#         print(f"{i:<5}:{items[i]}")
# item_new=input("Enter item name: ")
# if item_new in items:
#         print("Item exist in list")
#         new_price=int(input(f"Enter new price for {item_new}: "))
#         items[item_new]=new_price
#         print(f"{item_new} price updated.")
# else:
#         new_price=int(input(f"Enter new price for {item_new}: "))
#         items[item_new]=new_price
#         print(f"{item_new} price updated.")
# for x in items:
#                 print(f"{x:<5}:{items[x]}")
#                 total+=items[x] 
        
# print("-"*10)
# print(f"Total:{total}")
# print(items) 


# items = {
#     "Rice": 10,
#     "Beans": 5,
#     "Oil": 7
# }
# del_item=input("Enter item to be removed: ")
# if del_item in items:
#         del items[del_item]
# print(items)



# def account_balance(name, balance):
#     for _ in range(5):  # Limit to 5 transactions
#         print("\n--- ATM Menu ---")
#         print("1. Check Balance")
#         print("2. Deposit Fund")
#         print("3. Withdraw Fund")
        
#         choice = input("Enter choice (1-3): ")

#         if choice == "1":
#             print(f"{name}, your available balance is: {balance}")

#         elif choice == "2":
#             amount = float(input("Enter amount to deposit: "))
#             if amount > 0:
#                 balance += amount
#                 print(f"✅ {amount} deposited successfully. New balance = {balance}")
#             else:
#                 print("❌ Invalid deposit amount.")

#         elif choice == "3":
#             amount = float(input("Enter amount to withdraw: "))
#             if amount > balance:
#                 print("❌ Insufficient balance.")
#             elif amount <= 0:
#                 print("❌ Invalid withdrawal amount.")
#             else:
#                 balance -= amount
#                 print(f"✅ Withdrawal of {amount} successful. New balance = {balance}")
#         else:
#             print("❌ Invalid choice.")
    
#     print("\nTransaction limit reached. Goodbye!")

# # Start the ATM system
# user_name = input("Enter your name: ")
# account_balance(user_name, 0)


# print("1. Check Balance")
# print("2. Deposit Fund")
# print("3. Withdraw Fund")

# choice=input("Enter choice(1-3):")
# if choice=="1":
#     print("hello")
# elif choice=="2":
#     print("Hi")
# elif choice=="3":
#     print("Goodbye")


# import random  # to make the computer pick a random number

# # Step 1: Computer picks a number between 1 and 100
# secret_number = random.randint(1, 100)

# # Step 2: Keep track of attempts
# attempts = 0

# # Step 3: Loop until the user guesses correctly
# while True:
#     guess = int(input("Guess a number between 1 and 100: "))
#     attempts += 1  # add 1 to attempts each time

#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print(f"🎉 Correct! You guessed it in {attempts} attempts.")
#         break  # stop the loop when guessed correctly
    
# vowels="a, e, i, o, u"
# sentence_words= input("What is your name? ")
# for x in sentence_words:
#     print(sentence_words)


# colour= "yellow"
# vowels="aeiou"
# count=0
# for y in colour:
#     if y in vowels:
#         print(y)
#         count+=1
# print(f"Vowels are {count} on {colour}")

# import string

# username= "cuteibluvu"
# print(f"Username: {username}")
# password= input("Enter your password: ")
# has_symbols=any(ch in string.punctuation for ch in password)
# has_upper= any(ch.isupper() for ch in password)
# has_lower= any(ch.islower() for ch in password)
# has_digit = any(ch.isdigit() for ch in password) 
# if len(password)>=8 and has_upper and has_lower and has_symbols:
# #if all([len(password) >= 8, has_upper, has_lower, has_symbols, has_digit]):

#     print("Password is strong")
# else:
#     print("Password is weak")         

# num = int(input("Enter any number: "))
# print(f"Multiplation Table for {num}:")
# for multi in range(1,13):
#         print(f"{num} * {multi} =", multi*num)
        





#new practise
        
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(len(thisdict.keys))
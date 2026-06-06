# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age



#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=People("Mike",30)
# print(p1)


# class Car:
#     def __init__(self,brand, model, year):
#         self.brand= brand
#         self.model= model
#         self.year=year

#     def __str__(self):
#         return f"{self.brand}({self.model} {self.year})"


# dcar=Car("Toyota","Corolla", 2023)
# print(dcar)

# class Student:
#     def __init__(self, name, age, grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

    
# result= student("Mike",24,'A')
# print(result.name)
# print(result.age)
# print(result.grade)
# print(result.name ,"-",result.grade)


# class Book:
#     def __init__(self, title, author, pages):
#         self.title= title
#         self.author= author
#         self.pages=pages

#     def display_details(self):
#         return f"Title: {self.title},Author: {self.author},Pages: {self.pages}"



# nv=Book("The Lion", "Yinka Aye", "200")
# print(nv.display_details())


# class Employee:
#     def __init__(self, name, salary):
#         self.name= name
#         self.salary= salary

#     def show_details(self):
#         return f"Employee Name:{self.name}, Salary:{self.salary}"
    


# abc= Employee("Tobi Loba", 2500)
# print(abc.show_details())


# class Rectangle:
#     def __init__(self,length, width):
#             self.length= length
#             self.width= width

#     def area(self): 
#         return  self.length * self.width

#     def perimeter(self):
#          return 2* (self.length + self.width)
    

# y=Rectangle(5,6)
# print("Area: ",y.area())
# print("Perimeter:", y.perimeter())


# class BankAccount:
#     def __init__(self, account_name, balance=0):
#         self.account_name = account_name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return f"Deposited: {amount}"

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient funds"
#         self.balance -= amount
#         return f"Withdrawn: {amount}"

#     def get_balance(self):
#         return f"Current balance: {self.balance}"

#     def __str__(self):
#         return f"Account: {self.account_name}, Balance: {self.balance}"
    
# dd= BankAccount("Dele Olu",200)
# print(dd)
# print(dd.deposit(100))
# print(dd.withdraw(20))
# print(dd.get_balance())


# class Person:
#     def __init__(self,name, age):
#         self.name= name
#         self.age= age

#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         return False
        
#     def __str__(self):
#         return f"{self.name}({self.age})"

# pp=Person("John",10)

# print(pp.is_adult())
# print(pp)

        
# class Movie:
#     def __init__(self,title, rating):
#         self.title= title
#         self.rating= rating
    
#     def is_family_friendly(self):
#         if self.rating<13:
#             return True
#         return False
    
#     def __str__(self):
#         return f"{self.title}({self.rating})"
    

# kk=Movie("Lion and the Jewel",11)
# print(kk.is_family_friendly())
# print(kk)

# class Laptop:
#     def __init__(self, brand, cpu, ram):
#         self.brand= brand
#         self.cpu= cpu
#         self.ram= ram

#     def specs(self):
#         return f"{self.brand},{self.cpu},{self.ram}"
    

#     def __str__(self):
#         return self.specs()
    

# ku=Laptop("Intel Core i7","12700K", "32GB")
# print(ku.specs())
# print(ku.ram)
# print(ku.brand)
# print(ku.cpu)
# print(ku.specs())


# class Circle:
#     def __init__(self, radius, pie=3.14):
#         self.radius= radius
#         self.pie= pie

#     def area(self):
#         return self.radius**2 * self.pie
    
#     def circumference(self):
#         return 2 * self.pie * self.radius

# cc=Circle(10,pie=3.14)
# print(f"Area of a Circle: {cc.area()}")
# print(f"Pie: {cc.pie}")
# print(f"Circumference of a Circle: {cc.circumference():.2f}")



# class ShoppingCart:
#     def __init__(self):
#         self.items=[]

#     def add_item(self,name, price):
#         self.items.append((name,price))
#         return f"Added: {name} - ${price}"

#     def remove_item(self,name):
#         for item in self.items:
#             if item[0]==name:
#                 self.items.remove(item)
#                 return f"Removed: {name}"
#         return f"{name} not found in cart"
            
#     def get_total(self):
#         total=sum(price for _, price in self.items)
#         return f"Total: ${total}"

#     def list_items(self):
#         if not self.items:
#             return "Cart is empty"
#         return [f"{name} - ${price}" for name, price in self.items]
    
# jp= ShoppingCart()
# print(jp.add_item("Orange",20))
# print(jp.add_item("Mango",40))
# print(jp.add_item("Banana",10))
# print(jp.list_items())
# print(jp.remove_item("Mango"))
# print(jp.list_items())


# class Library:
#     def __init__(self):
#         self.books={}
#     def add_book(self,title):
#         self.books[title]=""
#         return f"Added: {title}"
    
#     def borrow_book(self,title):
#         for title in self.books:
#             if self.books[title]:
#                 return f"{title} -Available"
#             return f"{title} -Borrowed"
            
#     def return_book(self,title):
#         for title in self.books:
#             if self.books[title]==False:
#               return f"{title} -Available"
#         return f"{title} - Borrowed"
    
#     def list_books(self):
#         if not self.books:
#             return f"Book not in stock"
#         return {f"{title}" for title in self.books}
    

# reg=Library()
# print(reg.add_book("Lion"))
# print(reg.add_book("Cat"))
# print(reg.add_book("Dog"))
# print(reg.borrow_book(0))
# print(reg.return_book(2))
# print(reg.list_books())



# def student_report(name, *subjects, **scores):
#     print(f"Name:{name}")
#     print(f"subject: {subjects}")
#     total=0
#     count=0
    
#     for subject in subjects:
#         score=scores.get(subject,0)
#         print(f" - {subject}: {score}")
        
#         total+=score
#         count+=1
#         average=total/count
#     print(average)




# student_report("Joy Kent","Math", "Science","English",Math=80, Science=90, English=70)
# item_orders={"burger":2, "fries":3,"soda":2}




name = "Lara"
age = 16



# if  age<12:
#     ticket=5
# elif age>=12<=17:
#     ticket=7
# elif age>=18:
#     ticket=10
# print(f"{name} ticket cost £{ticket}")



#you need to remember the problem you encounter in this program
#at the withdraw level, i was having challenges of running withdraw amount,
#invalid amount, and insufficient balance together.

# def transactions(name, balance):
#     for _ in range(5):
#         print("1.Check Balance")
#         print("2.Deposit Money")
#         print("3.Withdraw Fund")
#         print("4.Exit App")
#         choice=int(input("Enter your choice (1-3): "))
#         if choice==1:
#             print(f"{name}, with available balance of {balance}")
#         elif choice==2:
#             amount=float(input("Enter amount for deposit: "))
#             if amount>0:
#                 balance+=amount
#                 print(f"{amount} deposited and new balance is {balance}")
#             else:
#                 print("Invalid amount")
#    #the two impossible will come first, before the positive one.     
#         elif choice==3:
#             amount=float(input("Enter amount for withdraw: "))
#             if amount > balance:
#                 print("Insufficient Balance")
#             elif amount <=0:
#                 print("Invalid withdrawal amount")
#             else:
#              amount<balance
#              balance-=amount
#              print(f"{amount} withdrawn and new balance is {balance}")
#         elif choice==4:
#             print("Exit app, Good bye")
#             break

#         else:
#             print("invalid choice")
                


# user_name=input("Enter your name: ")
# transactions(user_name, 0)


import getpass   # module that hides input

def transactions(name, balance):
    # Define a fixed PIN (in a real bank app, each user would have their own stored securely)
    PIN = "1234"  

    for _ in range(5):
        print("\n1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Fund")
        print("4.Exit App")
        choice=int(input("Enter your choice (1-4): "))

        if choice==1:
            print(f"{name}, your available balance is: {balance}")

        elif choice==2:
            amount=float(input("Enter amount for deposit: "))
            if amount>0:
                balance+=amount
                print(f"✅ {amount} deposited. New balance is {balance}")
            else:
                print("❌ Invalid amount")

        elif choice==3:
            amount=float(input("Enter amount for withdraw: "))

            # First check impossible cases
            if amount > balance:
                print("❌ Insufficient Balance")
            elif amount <=0:
                print("❌ Invalid withdrawal amount")
            else:
                # ✅ Case where balance is enough
                # Request PIN securely (hidden while typing)
                pin_entered = getpass.getpass("Enter your 4-digit PIN: ")

                if pin_entered == PIN:  # PIN correct
                    balance-=amount
                    print(f"✅ {amount} withdrawn successfully. New balance = {balance}")
                else:  # PIN wrong
                    print("❌ Incorrect PIN. Withdrawal cancelled.")

        elif choice==4:
            print("👋 Exit app, Goodbye!")
            break

        else:
            print("❌ Invalid choice")


# Start program
user_name=input("Enter your name: ")
transactions(user_name, 0)

#Variables & Input
# name=input("What is your name?" )
# age=input("How old are you?" )
# print(f"Hello {name}, you are {age} years old.")

#Even or Odd
# number=int(input("Write a number of your choice: "))
# if number%2==0:
#     print("Even Number ")
# else:
#     print("Old Number")

#Sum of Numbers
# number1=int(input("number one: "))
# number2=int(input("number two: "))
# sum_of_nums=number1+number2
# print(f"Sum: {sum_of_nums}")

#List Basics
# list_fruits=["Mango","Apple","Avocado","Pineapple","Banana"]
# print(list_fruits[0])
# print(list_fruits[-1])

# #Looping
# for i in range(1,11):
#     print(i)

# Largest of Three
# number1=input("Enter first number: ")
# number2=input("Enter second number: ")
# number3=input("Enter third number: ")

# if number1>=number2 and number1>=number3:
#     print(f"Number one is greater: {number1}")
# elif number2>=number1 and number2>=number3:
#     print(f"Number two is greater: {number2}")
# else:
#     print("Number three is greater")

#Reverse a String
# word=input("Your favorite fruit: ")
# print("reverse word:",word[::-1])


#Multiplication table
# number= int(input("Enter a number: "))
# for x in range(1,11):
#     print(f"{number} x {x} = {number*x}")


#vowel in word

# vowel="aeiou"
# word= "daimond"
# count=0
# for char in word:
#     if char in vowel:
#         print(char)
#         count+=1
# print(count)



#create a function
# def square(n):
#     return n**2



# print(square(5))

# multi=1
#Factorial Function
# for x in range(1,6):
#     print(f"{x} x {multi}")
#     multi*=x
# print(f"{multi}")

#✅ Correct factorial function version:
# def factorial(n):
#     multi = 1
#     for x in range(1, n+1):
#         multi *= x
#     return multi

# print(factorial(5))  # Output: 120 

#Palindrome Check
# word= input("enter any word: ")
# reserve_word= word[::-1]
# print(reserve_word)
# if reserve_word==word:
#     print("True") # It is a palindrome
# else:
#     print("False") # It is not a palindrome


#FizzBuzz
# for num in range(1,51):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)



#Find an Average

# list_no= [20,30,10]
# plus=0
# for i in list_no:
#     print(i)
#     plus+=i
# print(plus/3)

# Better solution
# def average(numbers):
#     return sum(numbers) / len(numbers)

# print(average([20, 30, 10]))   # 20.0
# print(average([5, 10, 15, 20])) # 12.5


#max and min
#Word Frequency
# sentence_list="this is a test this is"
# words_split= sentence_list.split()
# word_count={}
# for i in words_split:
#     word_count[i]= word_count.get(i,0) + 1
# print(word_count)


# shopping_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
# count_shoplist={}

# for fruit in shopping_list:
#     count_shoplist[fruit]= count_shoplist.get(fruit,0) + 1
# print(count_shoplist)


# num= [1, 2, 2, 3, 4, 4]

# remove_dup= list(set(num))
# print(remove_dup)

# num= [1, 2, 3, 3, 4, 4]
# dup_new= []


# fruits = ["apple", "banana", "cherry", "orange"]
# prices = [2, 1, 3, 2]

# for i in range(len(fruits)):
#     fruits[i] = f"{i+1}. {fruits[i]}"
# print(fruits)

# for i in range(len(fruits)):
#     print(f"{fruits[i]} - ${prices[i]}")


# for i in range(len(prices)):
#     prices[i] = prices[i] * 1.5

# for i in range(len(fruits)):
#       fruits[i]= f"{i+1}. {fruits[i]}"
#       print(fruits[i])
    
#enumerate(fruits) → gives both index and value together.
# for index, fruit in enumerate(fruits):
#     prices[index]= prices[index]*1.5
#     print(f"{fruit} - ${prices[index]}")

# students=["Ibrahim", "Sodik","Kafayat","Saheed","Sheri"]
# scores = [80, 60, 75, 90, 55]


# print("Updated Student Scores:")
# for score in range(len(scores)):
#     scores[score]= scores[score]+10
#     print(f"{scores[score]}")


# print("Updated Student Scores:")
# for score,student in enumerate(students):
#     scores[score]= scores[score]+10
#     print(f"{student} - {scores[score]}")

#A list comprehension has this basic format:
#new_list = [ expression  for item in iterable  if condition ]

# students=["Ibrahim", "Sodik","Kafayat","Saheed","Sheri"]
# new_student=[]

# for student in students:
#     if 's' in student.lower():
#         new_student.append(student)

# print(new_student)

# new_line=[x.lower() for x in students if "a" in x]
# print(new_line)




#key=myfunc is used to sort based on the result but original information won't change.

# numbers = [23, 11, 45, 72, 39, 8]

# def myfunc(n):
#     return n % 10   # last digit

# numbers.sort(key=myfunc)

# print(numbers)

# words = ["banana", "fig", "apple", "kiwi", "blueberry", "pear"]

# def myfunc(n):
#     return len(n)
# words.sort(key=myfunc)

# print(words)

# words = ["banana", "fig", "apple", "kiwi", "blueberry", "pear"]


# def myfunc(c):
#     return c[len(c)//2]
# words.sort(key=myfunc)
# print(words)


# list1 = ["milk", "eggs", "bread", "butter"]
# list2 = ["juice", "bread", "apples", "milk"]

# list1.extend(list2)
# set(list1)
# list1.sort()
# print(list1)

#🧩 Question 1 — Create and Access(list)
# fruits=["apple", "banana", "cherry", "orange"]

# fruits_update= fruits[0],fruits[-1]
# print(fruits_update)
# print(len(fruits_update))
# fruits[1]= "grape"
# print(fruits)

#🧩 Question 2 — Add, Insert, and Remove(List)

# numbers = [10, 20, 30]
# numbers.append(40)
# numbers.insert(0,5)
# numbers.remove(20)
# print(numbers)

#🧩 Question 3 — Loop and Condition
# scores = [55, 70, 89, 42, 90, 67]
# count=0
# for i in scores:
#     if i>60:
#         print(i)
#     if i>80:
#         count+=1
# print(f"Number of high scores: {count}")

#🧩 Question 4 — Sorting, Copying, and Joining

# list1 = ["milk", "bread", "butter"]
# print(f"First List: {list1}")
# list2 = ["eggs", "juice"]
# print(f"Second List: {list2}")
# list3= list1.copy()
# print(f"Third List: {list3}")

# list_join= list1 + list2
# list_join.sort()
# print(f"Join List: {list_join}")

#🧩 Question 5 — Removing Duplicates and List Comprehension

#Step 3: list comprehension for long items
items = ["pen", "book", "pen", "bag", "book"]
# item=list(set(items))
# item.sort()
# print(item)
# long_items = [i for i in item if len(i) > 3]
# print("Long items:", long_items)


# item=list(set(items))
# item.sort()
# print(item)


# long_items=[]
# for i in item:
#     if len(i)>3:
#         long_items.append(i)
    
# print("Long items:", long_items)

#🧩 Challenge 1 — Create and Access Elements
# fruits= ("apple", "banana", "cherry", "orange")
# new= fruits[0],fruits[-1]
# print(new)
# print(len(fruits))
# print(fruits[1:3])


# colors = ("red", "green", "blue")
# l_colors= list(colors)
# l_colors[1]= "yellow"
# colors= tuple(l_colors)
# print(colors)

#another method to change value in tuple
# colors = ("red", "green", "blue")
# colors = (colors[0], "yellow", colors[2])
# print(colors)

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# tuple_repeat= tuple3*2
# print(tuple3)
# print(tuple_repeat)
# print(len(tuple_repeat))

#dictionary practice
# x= {
#     "Sodik":{"math":100, "english":87},
#     "Saheed":{"math":98, "english":78}

# }
# x["Saheed"]={"Yoruba":39,"Science": 80}
# x["Sheri"]= {"math":100, "english":87}
# print(x)

# users: dict= {0: "Mario", 1: "Luigi", 2: "James"}

# print(users)


#7, 12, 21,22,23,31,37


# student={
#     "name": "Alice",
#     "age": 20,
#     "course": "Python"
#             }
# x=student["name"]
# print(x)
# #print(student["name"])

# car = {"brand": "Toyota", "model": "Camry"}
# car["year"]= 2020
# print(car)

# person = {"name": "John", "age": 25, "city": "London"}
# person["age"]= 30
# print(person)

fruits = {"apple": 3, "banana": 5, "orange": 2}


# for i in fruits.items():
#     print(i)


# for x,y in fruits.items():
#     print(f"{x}:{y}")


# user = {"username": "baba123", "email": "baba@mail.com"}

# user["password"] = "12345"


# if "password" in user:
#     print("password exist")
# else:
#     print("password not found")


#🧩 Challenging Dictionary Question
# scores = {
#     "Alice": {"Math": 85, "English": 78, "Science": 92},
#     "Bob": {"Math": 58, "English": 65, "Science": 70},
#     "Charlie": {"Math": 95, "English": 90, "Science": 85}
# }
    
# for name, subjects in scores.items():
#     total = 0
#     count = 0
    
#     for subject, mark in subjects.items():
#         total += mark
#         count += 1
    
#     average = total / count
    
#     if average < 70:
#         print(f"{name}: Average = {average:.1f} (Needs Improvement)")
#     else:
#         print(f"{name}: Average = {average:.1f}")



# sales = {
#     "James": {"January": 1200, "February": 1500, "March": 1000},
#     "Sarah": {"January": 2200, "February": 2100, "March": 2300},
#     "Tom": {"January": 800, "February": 950, "March": 1050}
# }
# #when we loop, Python automatically unpacks each pair into two variables:
# top=0
# top_employee=""
# for name, months in sales.items():
#     sum=0

#     for month, amount in months.items():
#         sum+=amount
#     print(f"{name} : Total Sum = {sum}")
#     if sum>top:
#         top=sum
#         top_employee=name
# print(f"Top Performer: {top_employee} with total sales of {top}")



# 🧠 1. If/Else Logic & Conditions
# num= int(input("Enter random number: "))
# if num>0:
#     print("number is positive")
# elif num<0:
#         print("number is negative")
# else:
#      print("number is zero")


# age = int(input("Enter your age: "))

# if age<13:
#     print("Child if under 13")
# elif age>=13 or age<=19:
#     print("Teenager if 13–19")
# elif age>=20:
#     print("Adult if 20 or older")
# else:
#     print("Age input is invalid")


# 📘 Rules to Check a Leap Year
# ✅ Divisible by 400 → Leap year
# ❌ Divisible by 100 (but not 400) → Not leap year
# ✅ Divisible by 4 (but not 100) → Leap year
# ❌ Everything else → Not leap year
# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# num= int(input("Enter random number: "))

# if num%3==0 and num%5==0:
#     print("Number is divisible by 3 and 5")
# elif num%5==0:
#     print("Number is only divisible by 5 only")
# elif num%3==0:
#     print("Number is divisible by 3 only")
# else:
#     print("Number is not divisible by 3 and 5")

# list1= [2,4,6]
# large=0
# for i in list1:
#     if i>large:
#         large=i
# print(large)


#🔁 2. Loops (for / while)
# for i in range(1,51):
#     if i%2==0:
#         print(i)


# add=0
# for i in range(1,101):
#     add+=i
# print(add)

# num= int(input("enter your number: "))
# for i in range(1,13):
#     table=num*i
#     print(f"{num}*{i}= {table}")


# num= int(input("enter your number: "))
# fac=1
# i=1
# while i<=num:
#     fac*=i
#     i+=1
#     print(fac)



# list2= [2,5,6,13,56,67,5,10]

# for i in list2:
#     if i>10:
#         print(i)


#looking for min, max, value in a list.
# list2= [2,5,6,13,56,67,5,10]

# maxx=list2[0]
# minn=list2[0]

# for x in list2:
#     if x>maxx:
#         maxx=x
#     elif x<minn:
#         minn=x
# print(f"max: {maxx}, min: {minn}")


#list of fruits, print only the onces that start "a".

# fruits= ["Mango", "Orange", "Pineapple","Apple","Lime","Grape"]
# for fruit in fruits:
#     if "a" in fruit.lower():
#         print(fruit)

#Remove all duplicate items from a list.

# animals= ["Goat", "Cow", "Sheep","Tiger","Lion","Cow"]
# animals= list(dict.fromkeys(animals))
# print(animals)

#using set method 
# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruits = list(set(fruits))
# print(unique_fruits)

# using for loop

# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruit= []
# for fruit in fruits:
#     if fruit not in unique_fruit:
#         unique_fruit.append(fruit)
# print(unique_fruit)

#extending two variable
# fruit_a= ["apple", "banana", "apple", "cherry", "banana"]
# fruit_b= ["Pineapple", "Avocado", "Lemon", "Lime"]

# fruit_a.extend(fruit_b)
# print(fruit_a)

#Sort a list manually (without using .sort() or sorted()).


# animals= ["Goat", "Cow", "Sheep","Tiger","Lion","Cow"]
# print(animals)

# numbers=[3,7,2,8,9,10]
# numbers.sort()
# print(numbers)
# sorted_list=sorted(numbers)
# print(sorted_list)

# items=[
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 12)

# ]
# print(items[1])

# items.sort()
# print(items)


# #map(function, iterable)
# number = [1,2,3,4,5]
# x= list(map(lambda x: x*2, number))
# print(x)

# #filter give result of what is true
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_num= list(filter(lambda x:x %2!=0, numbers))
# print(odd_num)

# #sorted(students, key=lambda x: x[1])
# #this use the tuple sort the list.
# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)


# x= lambda a: a + 10
# print(x(7))

# x = lambda a,b: a*b
# print(x(5,6))

# num= [10,4,5,3,2,6,7,8]
# x=list(filter(lambda a:a %2==0, num))
# print(x)


# x= lambda a:a**2
# print(x(5))

# list1= "john"
# print(list1[3])

# x = lambda list1: list1[-1]
# print(x("iron"))
# print(x("mango"))
# print(x("sugar"))


# numbers = [10, 20, 30, 40]

# for i in range(len(numbers)):
#     print("Index:", i, "Value:", numbers[i])


# numbers = [1, 2, 3, 4, 5]
# map_book= list(map(lambda a: a*2, numbers ))
# print(map_book)

# words = ["apple", "banana", "cherry"]
# x = list(map(lambda w: w.upper(), words))
# print(x)


# def outter():
#     a= 10
#     def inner():
#         if a<=15:
#             return a
#         else:
#             return "a is greater than 15"
#     return inner

# myfunc=outter()
# print(myfunc())


# def create_traffic_light_validator():  # outer function
#     traffic_light_colors = ("GREEN", "RED", "ORANGE",)

#     def is_valid_light(color):  # inner function
#         # Check if the passed color is a valid traffic light color
#         if color.lower() in list(map(str.lower, traffic_light_colors)):
#             return True
#         else:
#             return False

#     return is_valid_light


# # Create the validator function
# validator = create_traffic_light_validator()  # validator == is_valid_light

# color = "Red"

# if validator(color):
#     print(f"YES {color} is a valid traffic light color!")
# else:
#     print(f"NO {color} is NOT a valid traffic light color!")



# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello Sally"

# # myfunc = changecase(myfunction)
# print(myfunction())






# def add_exclamation(func):
#     def inner():
#         return func() + "!!!"
#     return inner

# @add_exclamation
# def greet():
#     return "Good morning"

# print(greet())


# def add(a):
#     def inner():
#         return a().lower()
#     return inner

# @add
# def thirdinner():
#     return "I LOVE YOU"



# print(thirdinner())



# def make_lowercase(fun):
#     def inner():
#         return fun().lower()
#     return inner

# @make_lowercase
# def say_name():
#     return "HELLO MY FRIEND"

# print(say_name())




# def modify_string(func):
#     def inner():
#         return func().upper() + "!!!"
#     return inner



# @modify_string
# def say_hi():
#     return "how are you"

# print(say_hi())


# def make_upper(func):
#     def inner():
#         result = func()         # call the original function
#         return result.upper()   # modify its result
#     return inner                # return the wrapper

# @make_upper
# def greet():
#     return "good evening"
# print(greet())  # 👉 GOOD EVENING




# # Explanation:

# # Here we manually pass greet (without parentheses!) to the decorator.

# # That means:
# # result = make_upper(greet) → returns the inner function.

# # Then result() calls inner(), which in turn calls greet() inside.


# def make_upper(func):
#     def inner():
#         result = func()         # call the original function
#         return result.upper()   # modify its result
#     return inner                # return the wrapper


# def greet():
#     return "good evening"
# red= make_upper(greet)
# print(red())  # 👉 GOOD EVENING



# In manual decoration, the variable points to the inner function directly,
# while with @decorator, the function name itself is replaced by inner.
# def add_exclamation(func):
#     def inner():
#         return func() + "!!!"
#     return inner

# @add_exclamation
# def say_hello():
#     return "hello"

# print(say_hello())


# #========================

# def upper_case(func):
#     def inner():
#         return func().upper()
#     return inner


# @upper_case
# def greet():
#     return "good day"
# print(greet())

# #========================


# def upper_case(func):
#     def inner():
#         return func().upper()
#     return inner



# def greet():
#     return "good day"
# result=upper_case(greet)
# print(result())

# #========================


# def add_prefix(func):
#     def inner():
#         return "Mr. " + func()
#     return inner


# @add_prefix
# def get_name():
#     return "John"
# print(get_name())

# #========================

# def repeat_twice(func):
    
#     def inner():
#         return f"{func()} | {func()}"
#     return inner



# @repeat_twice
# def greet():
#     return "Hi"
# print(greet())
# #========================


# def decorator(func):
#     def inner():
#         print("Before function runs")
#         result = func()
#         print("After function runs")
#         return result
#     return inner

# @decorator
# def say_hello():
#     print("Hello there!")

# say_hello() #we didn't put this in printing because it has already called the printing in line 878

# #========================
# def changecase(n):
#   def changecase(func):  #this act like a inner decorator this is why we return it early and also hold the func
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(1)
# def myfunction():
#   return "Hello Linus"

# print(myfunction())


# n=0
# def condition(func):
#     if n==1: 
#         return func.lower() 
    
#     else: 
#         return func.upper() 


# print(condition("Good"))


# def myfunction():
#     """This function returns a friendly message."""
#     return "Have a great day!"

# print(myfunction.__name__)  # shows the name of the function
# print(myfunction.__doc__)   # shows the docstring



#=============================
# def countdown(n):
#     if n<=0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(5)

# def fibonacci(n):
#   if n <= 1:
#     return n
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(7))


# even number
# def evennum(n):
#     print(n)
#     if n==2:
#         return n
#     else:
#         return evennum(n-2)
    

# evennum(10)

#countdown numbers : n-1 is the key
# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)
# countdown(10)


#sum up a list use the first index and add to the rest of the indexes
# def sum_list(numbers):
#     if len(numbers) == 0:  #the lenght of the list is 5 in defalt is when len is use as base till it get to 0
#         return 0
#     else:
#         return numbers[0] + sum_list(numbers[1:])
    
# print(sum_list([1,2,3,4,5]))




# #factorial : use the n to multiply the f
# def factorial(n):
#     if n == 1:  #the base is 1 because if we put it in 0 it will return 0 back to us
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(3))



# # Base case: When string is empty, stop.
# #Recursive case: Take last character + reverse the rest.
# def reverse_string(text):
#     if len(text) == 0:
#         return ""
#     else:
#         return text[-1] + reverse_string(text[:-1])
    
# print(reverse_string("mango"))


# #Base case: When number is 0, stop.
# #Recursive case: Add last digit (n % 10) to the sum of the rest (n // 10).
# ✅ Summary in your exact words:

# ✔ n % 10 keeps the last digit
# ✔ n // 10 removes the last digit
# ✔ This is how recursion reduces the number until it reaches 0
# ✔ That reduction is what allows the function to stop without loops
# def sum_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_digits(n // 10)
    
# print(sum_digits(123))



#practice 
# def count_down(n):
#     if n<=0:
#         print("Done!")
#     else:
#         print(n)
#         return count_down(n-1)
# count_down(10)


def sum_digits(n):
    if n==0:
        return n
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(128))
print(sum_digits(999))




# word = "banana"
# counted= 0
# for i in word:
#     if "a" in i:
#         counted+=1
# print(counted)


# def count_char(word):
#     if word=="":
#         return 0
#     first=1 if word[0]=="a" else 0
#     return first + count_char(word[1:])
        

# print(count_char("banana"))


# def sum_list(num):
#     if len(num)==0:
#         return 0
#     else:
#         return num[0] + sum_list(num[1:])

# print(sum_list([4, 1, 3, 7]))




# def reverse(word):
#     if word=="":
#         return ""
#     else:
#         return word[-1] + reverse(word[:-1])

# print(reverse("hello"))



# def is_palindrome(lst):
#     # Base cases
#     if len(lst) <= 1:
#         return True
    
#     # Compare first and last
#     if lst[0] != lst[-1]:
#         return False
    
#     # Recursive step
#     return is_palindrome(lst[1:-1])

# print(is_palindrome([1,2,3,2,1]))  # True
# print(is_palindrome([1,2,2,3]))    # False
# print(is_palindrome(["racecar"])) 

#n1
# def count_down(n):
#     if n<=0:
#         print("Done!")
#     else:
#         print(n)
#         count_down(n-1)
# count_down(10)

#n2
# def sum_digits(n):
#     if len(n)==0:
#         return 0
#     else:
#         return n[0] + sum_digits(n[1:])

# print(sum_digits([1,2,3]))
# print(sum_digits([9,9,9]))

#n4
# def reverse(word):
#     if word=="":
#         return ""
#     else:
#         return word[-1:] + reverse(word[:-1])

# print(reverse("hello"))

#5
# def sum_list(num):
#     if len(num)==0:
#         return 0
#     else:
#         return num[0] + sum_list(num[1:])
# print(sum_list([4, 1, 3, 7]))


#n9
# def multi(n,o):
#     if n*o==0:
#         return 0
#     else:
#         return n * o
# print(multi(4,3))


# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num * factorial(num-1)
    
# print(factorial(5))




def rev_fun(word):
    if word=="":
        return ""
    else:
        return word[-1] + rev_fun(word[:-1])

print(rev_fun("hello"))


def count_word(word):
    if word=="":
        return 0
    first=1 if word[0]=="a" else 0
    return first + count_word(word[1:])

print(count_word("babalola"))

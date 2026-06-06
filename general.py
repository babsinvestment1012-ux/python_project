
x= "lovely"
def myfunc():
   x="global Variable"  


myfunc()
print("X is: "+x)

x=5
y="color"
list_color=["blue","yellow","white","green"]
tuple_cars=("honda","benz","toyota","volvo")
print(list_color)
print(tuple_cars)

#Write a Python program that takes a user's age as input, stores it as a variable, casts it to an integer, adds 5 to it, and prints the result with a message.
#age=input("Enter your age:")
#print("In five years you wil be: ",int(age)+5)

#Write a Python program that stores a user's current age as a global variable, defines a function that casts it to an integer, 
#adds 5 using a local variable, and prints the result with a message.
#age= input("what is your age: ")
#def age_def():
   #global age
   #current_age=int(age)
   
   #print("In five years you wil be: ", current_age +5)
#age_def()

#Create a list of three fruits. Replace the second fruit with "mango" and print the updated list.
fruits=["orange","banana","watermelon"]
print(fruits)
fruits[1]="mango"
print(fruits)

#Create a tuple with three colors. Print the last item in the tuple.
colors=("blue","yellow","green")
print(colors[-1]) # when you start index from the back you start with -1.

#Create a dictionary with keys "name" and "age". Print the value of "name".
person= {"name":"Ibrahim","age":50}
person["class"]="JS1"
person["name"]="Babs"
print(person)

#F-string 
num="not"
txt=f"you are {num} making sense"
print(txt)

#format 
fruits= 12
xfruit= f"We have {fruits:.2f} Oranges with us"
print(xfruit)
yfruit= xfruit.format(12)
print(yfruit)
print("We have {:<8} chickens.".format(49))
print("We have {:>8} chickens.".format(49))
print("We have {:^8} chickens.".format(49))
txt = "You scored {:%}"
print(txt.format(0.25))

txt = "You scored {:.0%}"
print(txt.format(0.25))

#F-string Exercise
nam="Ibrahim Babalola"
text=f'Hello, my name is {nam}'
print(text)

num1= 40
num2=60
sum=num1+num2
print(format(sum))
print(f'The sum is: {sum}')
a = 10
b = 5
print(f"The sum is {a + b}")

amount=15
print(f'The price is {amount:.2f} dollars')
bag_rice="The cost of rice {cost:.2f}"
print(bag_rice.format(cost=55))

name= "John"
age= 25
info=f"{name} is {age} years old"
print(info)

score = 0.85
print(f"You scored {score:.2%}") #f-string method
result= f"You scored {score:.2%}" 
print(result.format(0.85))  #format method

#slicing string
text = "Programming"
print(text[3:7])

#String Concatenation
word="hello world"
print(word.upper())
print("hello " + "World")
#print(f"{word1} {word2}")

#Escape Characters
sam="She said \"Hello\""
print(sam)
#formating string
name="John"
age=30
age_name=f"My name is {name} and I am {age} years old."
print(age_name)

#boolean Exercise
a=bool(10>5)
print(a)

is_raining = True
if is_raining==True:
    print ("Take an umbrella")

num= int(input("Enter Number: "))
print(num==100)

a=int(input("enter your even number: "))
print(a<=10 and a<=20)

def is_even(num):
    return num % 2 == 0


print(is_even(7))
print(is_even(4))

sent="I am learning Python programming"
word="Python"
print(bool(word in sent))

fruits_list=["mango","banana","apple","alvocado"]
print(bool("apple" in fruits_list))

print(bool(0))
print(bool("hello"))
print(bool([]))

age=int(input("How old are you? "))
print((age>=18))

is_logged_in = False

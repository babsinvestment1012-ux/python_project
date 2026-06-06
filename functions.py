#def function_num(parameter):
    #print(parameter + 2)


#function_num(8)

first_str = "The number "

def function_num(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_num(first_str, 5, " is an integer.")

def default_num (num1=7, num2=8):
    print(num1 * num2)


default_num()

h_grt = "Hello world"   #exe
def hello_world_printer():
    print(h_grt)


hello_world_printer()



def name_printer(user_name): #exe1
    print(user_name)

name = input("please enter your name. ")
name_printer(name)   #the calling is here bcus we have an input statement

#second exe
length=int(input("Enter integer length: " + "\n"))
weight=int(input("Enter integer weight " + " \n"))
height=int(input("Enter integer height "+" \n"))


def volume_fun(length, weight, height):
    return length*weight*height


print(volume_fun(int(length), int(weight), int(height)))
print("The volume of a cube feet: "+ str(volume_fun((length), (weight), (height)))) #concatenate can only be done with str

#f = int(input("Enter Fahrenheit "))
c = int(input("Enter Celsius "))
num1= 18      #converted 1.8 to 18 by multiply by 10 so as to covert it to string and concatenate
num2= 320

def fahrenheit(c):
   #return (18*c+320)/10
    return round((1.8*c+32),1)    #return(round(1.8,1)*c+32)

print("The Fahrenheit equivalent of " + str(c) + " degrees Celsius is " + str(fahrenheit(c)) + ".")

def main():
    number= get_number()
    meow=(3)
def get_number():
    while True:
        n=int(input("what is n"))
        if n>0:
          break
    return  n

def meow(n):

 main()



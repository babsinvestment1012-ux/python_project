#fruits = input("Enter favorite fruit "+'\n')

#if fruits=="Mango":
    #print("The fruit is: "+ fruits)
#else:
    #print("Fruit is not Mango")
    #
score= int(input("Enter Student Score? "))
if score>=90:
    print("Student will receive A grade ")
else:
    if score>=80:
        print("Student will receive B grade ")
    else:
        if score>=70:
            print("Student will receive C grade")
        else:
            if score>=60:
               print("Student will receive D grade ")
            else:
              print("Student will receive F grade")
#if 5>2:
#print("This is five is greater than two")


full_name = "Ibrahim Babalola"


salary = 25000


withdraw = int(input("Enter amount to withdraw: "))


if withdraw > salary:
    
    print("You cannot withdraw an amount greater than your salary.")
else:
    
    balance = salary - withdraw 
    print(f"Withdrawal successful!")
    #print("Amount withdrawn: ₦withdraw")
    print(f"Balance left: ₦{balance}")
    print(f"Amount withdrwan is {withdraw}")

x=y=z=50
print(x)
print(y)
print(z)
x,y,z="London","Lagos","Yemen"
print(x)
print(y)
print(z)
x=y=z="school"
print(x)
print(y)
print(z)

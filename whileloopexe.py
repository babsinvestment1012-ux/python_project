#another exe
num = int(input("Enter a positive number "))
sum = 0
int_post = num
while num > 0:
        print(num)
        sum = sum + num  # this is the method to add up all numbers
        num -= 1
print("Positive value entered " + str(int_post))
print("Total sum of the number from entered " + str(sum))
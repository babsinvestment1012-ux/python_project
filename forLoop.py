greetings = "123456678"
for game in greetings:
    print(game)

word = input("Enter words: ")
for i in range(len(word)):
    print(word[i])

while True: #this is use when the condition is true
    n= int(input("enter your number here "))
    if n>5:
        break
for _ in range(n):
        print("meow")

def main():
    print_square(3)


def print_square(size):
        for i in range(size):
            for j in range(size):  #this loop is for i, it count i loop three times
                print("#",end="")
            print() #this means a new line


main()


def main():
    print_square(3)


def print_square(size):
        for i in range(size):
            print("#"* size)


main()
#SAsk the user for a username and password. If either the username or password is empty, 
#print "Username or password cannot be blank"
login=input(f"username: ")
pas=input(f"password: ")
print(login)
print(pas)
if login=="" or pas=="":
    print("username or password cannot be blank")


#Check if the word "Python" exists in the sentence "I love Python programming". Print True if it exists, otherwise False.
a="Python".lower()
b="I love programming".lower()
print(bool(a in b))


words="john203@gmail.com"
words.split("@")

_, domain = words.split("@")

webmail_url = f"https://webmail.{domain}"
print(webmail_url)
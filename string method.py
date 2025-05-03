#Strings are immutable
a = "ujjwal"
print(len(a))
print(a.upper()) 
print(a.lower())
#Strings rstrip
a = "Ujjwal!!!"
print(a.rstrip("!"))
a= "!!Ujjwal!!!"
print(a.rstrip("!"))
#Strings replace()
a = "Ujjwal"
print(a.replace("Ujjwal", "Shivam"))
# Strings Split()
a = "!!!Ujjwal !!!Shivam !!!!Shinu"
print(a.split(" "))
#Strings to capitalize()
blogheading = "introduction to js"
print(blogheading .capitalize())
blogheading = "introduction tO Js"
print(blogheading . capitalize())
#Strings Center()
str1 = "Welcome to Console!!!"
print(len(str1))
print(len(str1.center(50)))
#String count()
a = "Ujjwal Kushwaha"
print(a.count("a"))
#String endswith()
str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))
#String We can even also check for a value in-between the string by providing start and end position
str1 = "Welcome to the console"
print(str1.endswith("to", 4,10))
#String Find()
str1 = "He's name is Dan.He is an Honest man"
print(str1.find("is"))
print(str1.find("an"))
print(str1.find("ishh"))
#String index()
#str1 = "He's name is Dan. He is an honest man" 
#print(str1.ind#ex("ishh"))
#String isalpaha()
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())
#String isLower()
str1 = "hello world"
print(str1.islower())
#strings isprintable()
str1 = "We wish  you a merry Christmas\n"
print(str1)
print(str1.isprintable())
#String isspace
str1 = "We wish you a merry Christmas\n"
str1 = " " #using Spacebar
print(str1.isspace())

str2 = " " #Using Spacebar
print(str2.isspace())
#string istitle()

str1 = "World Health Organization"
print(str1.istitle())
#String startswith()
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))
#string.swapcase()
str1 = "Python is interpreted language"
print(str1.swapcase())
#string title()
str1 = "His name is dan. dan is  an Honest man"
print(str1.title())

#Mini Project ⭐
#Personal Profile Generator

#The program should ask for:
#Name
#Age
#Profession
#City
#Favorite Programming Language

#Then display something like:

#============================
#      MY PROFILE
#============================
#Name        : Harish
#Age         : 46
#Profession  : Software Engineer
#City        : Bengaluru
#Language    : Python
#============================

# Use comments to explain each section of your code.

# Ask the user for their name and store it in a variable
name = input("Enter your name: ")
# Ask the user for their age and store it in a variable
age = input("Enter your age: ")
# Ask the user for their profession and store it in a variable
profession = input("Enter your profession: ")
# Ask the user for their city and store it in a variable
city = input("Enter your city: ")
# Ask the user for their favorite programming language and store it in a variable
language = input("Enter your favorite programming language: ")

# Display the profile information in a formatted manner
print("============================")
print("      MY PROFILE")
print("============================")
print("Name        : " + name)
print("Age         : " + age)
print("Profession  : " + profession)
print("City        : " + city)
print("Language    : " + language)
print("============================")
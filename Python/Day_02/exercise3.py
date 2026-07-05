# Ask the user for their birth year. 
# Calculate their approximate age.
# (Hint: Use the current year, 2026.)

current_year = 2026
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("You are approximately " + str(age) + " years old.")

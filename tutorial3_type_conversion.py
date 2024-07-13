birth_year = input("What is your birth year? ")
age = 2024 - birth_year # Expect Error
print(age)

# Correct Solution:
# birth_year = input("What is your birth year? ")
# age = 2024 - int(birth_year) 
# print(age)

# Built-in data type conversion functions:
int() # Convert to integers like 10, 99 and 1.
float() # Convert to decimal numbers like 12.05, 1.5 and 0.55
bool() # Convert to True or False Boolean value
str() # Convert to a text based string
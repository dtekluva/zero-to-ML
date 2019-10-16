# DATATYPES

# INTEGERS
# FLOAT
# STRINGS
# BOOLEANS
# COMPLEX NUMBER

# + plus
# - minus
# / division
# * multiplication

#triangle side_a = 5, side_b = 4 find side_c - (PYTHAGORAS)
# side_a = input("Please enter side A : ") 
# side_b = input("Please enter side B : ")

# side_a = int(side_a) #CAST INPUT RESPONSES INTO INTEGERS FROM STRING FORMAT
# side_b = int(side_b)

# print(type(side_a))
# print(type(side_b))

# side_c = ???
# side_c = (side_a ** 2 + side_b ** 2) ** 0.5
# rounded_result = round(side_c, 3)
# print(side_c)
# print(rounded_result)

print()
print("Hello user please note that the")
print("program outputs 0 for a leap ")
print("year and any other number for a none leap year")
print()

year = int(input("Please enter a year to test : "))

remainder = year % 4

print(year, "--->", remainder)
print(year, "is a Leap year --->", not bool(remainder))

# WRITE A PROGRAM TO TAKE A PERSONS AGE, AND FIND THE CORRSPONDING YEAR OF BIRTH AND THEN TELL IF SAID PERSON WAS BORN IN A LEAP YEAR
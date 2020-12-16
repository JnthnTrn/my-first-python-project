# Calculate Age

# ## instructions
#  The function calculate_age in script.py creates a variable called age that is the difference between the current year, and a birth year, both of which are inputs of the function. Add a line to return age.
# Outside of the function, call calculate_age with values 2049 (current_year) and 2003 (birth_year) and save the value to a variable called my_age.
# Call calculate_age with values 2049 (current_year) and 1953(birth_year) and save the value to a variable called dads_age.

# Print the string "I am X years old and my dad is Y years old" to the console, with my_age where the X is and dads_age where the Y is.


# def calculate_age(current_year, birth_year):
#     age = current_year - birth_year
#     return age
 

# my_age = calculate_age(2049, 2003)

# dads_age = calculate_age(2049, 1953)

# print(my_age)
# print(dads_age)
# print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")



# Challenge 1 - Tenth Power
#-----------------------------------------------------

# Write a function named tenth_power() that has one parameter named num. 
# The function should return num raised to the 10th power.

# ## Instructions
# Uncomment these function calls to test your tenth_power function:
#print(tenth_power(1))
# 1 to the 10th power is 1
#print(tenth_power(0))
# 0 to the 10th power is 0
#print(tenth_power(2))
# 2 to the 10th power is 1024


# def tenth_power(num):
#     return num ** 10
 
# print(tenth_power(1))
# print(tenth_power(2))



# Challenge 2 - Square Root
#-------------------------------------
# ## Instructions
#  Write a function named square_root() that has one parameter named num. Use exponents (**) to return the square root of num.

# Write your square_root function here:

# Uncomment these function calls to test your square_root function:
#print(square_root(16))
# should print 4
#print(square_root(100))
# should print 10


# def square_root(num):
#     return num ** 0.5

# print(square_root(16))
# print(square_root(100))



# Challenge 3 - Win Percentage
#-------------------------------------
# ## Instructions
# Create a function called win_percentage() that takes two parameters named wins and losses. This function should return out the total percentage of games won by a team based on these two numbers.

# Write your win_percentage function here:

# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100


# def win_percentage(wins, losses):
#     return %

# print(win_percentage(5,5))
# print(win_percentage(10,0))
# ## Ternary Operators
# if(5 > 7):
#     print("hello")
# else:
#     print("goodbye")

# expression = "hello" if 6 >= 6 else "goodbye"
# print(expression) 

# sale = True
# store_message = "Hello, we have a sale today!" if sale else "We don't have a sale together"

# print(store_message)

# store_message = ""
# sale = True
# if(sale):
#     store_message = "Hello, we have a sale today!"
# else:
#     store_message = "We don't have a sale today"

# print(store_message)


# ## Bolean Operaters
# if((2**3 == 8) and (4**2 == 8)):
#     print("true")
# else:
#     print("false")


# if((2**3 == 8) or (4**2 == 8)):
#     print("true")
# else:
#     print("false")

# ## Bolean Operaters:not
# if(not (2**3 == 8) or (4**2 == 8)):
#     print("true")
# else:
#     print("false")


# ## If Statements
# def addTwoIf_Even(num):
#     if(num % 2 == 0):
#         return num + 2
#     return num

# x = 1
# y = 2
# print(addTwoIfEven(x))
# print(addTwoIfEven(y))

# ## Else if Statements
# def add_Two_If_Even_and_add_three_if_three(num):
#     if(num % 2 == 0):
#         return num + 2
#     elif(num == 3):
#         return num + 3
#     return num


# x = 1
# y = 2
# z = 3
# print(add_Two_If_Even_and_add_three_if_three(x))
# print(add_Two_If_Even_and_add_three_if_three(y))
# print(add_Two_If_Even_and_add_three_if_three(z))


## Try and Except Statements
# try:
#     a = 1
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero!")

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError: 
    print("b was equal to zero, computers can't divie by zero!")
    b = int(input("b: "))
    print(a/b)
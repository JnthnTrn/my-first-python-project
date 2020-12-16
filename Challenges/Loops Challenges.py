# https://repl.it/repls/MintcreamInternationalAmpersand

# # Challenge 1
# def divisible_by_ten(nums):
#     count = 0
#     for num in nums:
#         if num%10 == 0:
#            count += 1
#     return count
#  print(divisible_by_ten([20, 25, 30, 35, 40]))


# # Challenge 2
# def add_greetings(names):
#     lst = []
#     for name in names:
#         lst.append("Hello " + name)
#     return lst
# print(add_greetings(["Owen", "Max", "Sophie"])) 

# # Challenge 3
# def delete_starting_evens(lst):
#     index = 0
#     while len(lst) > 0 and lst[0] %2 == 0:
#         lst.pop(0)

#     return lst

# print(delete_starting_evens([4, 8, 10, 11, 12, 15])) # [11, 12, 15]
# print(delete_starting_evens([4, 8, 10])) # []

# def delete_starting_evens(lst):
#     print(lst)
#     index = 0
#     while index < len(lst):
#         if lst[index] % 2 == 0:
#             num = lst.pop(index)
#             index -= 1
#         print("popped: " + str(num))


#         index += 1

#     return lst

# print(delete_starting_evens([4, 8, 10, 11, 12, 15])) # [11, 12, 15]
# print(delete_starting_evens([4, 8, 10])) # []

# Challenge 4
# def odd_indices(lst):
#     empty = []
#     x = 0
#     for num in lst:
#         if x %2 == 1:
#            empty.append(lst[x])
#         x += 1
#     return empty

# print(odd_indices([4, 3, 7, 10, 11, -2]))

# # Challenge 5 
# def exponents(bases, powers):
#     final = []
#     for base in bases:
#         for power in powers:
#             final.append(base ** power)
#     return final
# print(exponents([2, 3, 4], [1, 2, 3]))

# Challenge 6

        


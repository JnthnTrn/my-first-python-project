# names = ["alex", "allistair", "andrew", "angelo", "elijah", "george", "jonathan"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
# print(names[6])

# names = ["alex", "allistair", "andrew", "angelo", "elijah", "george", "jonathan"]
# for name in names:
#     print(name)

# name = "alex"
# print(name)
# name = "allistair"
# print(name)
# name = "andrew"
# print(name)

# rng = list(range(6))
# print(rng)

# lst = [1, 2, 3, 4, 5, 6, 7 , 8]
# for num in lst:
#     print(num*2)
# print(lst)

# #range(6) --> [0, 1, 2, 3, 4, 5]
# #range(8) --> [0, 1, 2, 3, 4, 5, 6, 7, 8]
# # range(len(lstr)) --> [0, 1, 2, 3, 4, 5, ... len(lst) - 1]

# LENGTH LISTS
#  list_length = len(lst)
# for index in range(list_length):
#     lst[index] = 2 * lst[index]
#     print(lst[index])

# print(lst)


# FOR LOOP:

# # Infinite Loop
# my_favorite_numbers = [4, 8, 15, 42]

# for num in my_favorite_numbers:
#     my_favorite_numbers.append(1)
#     print("to infinity and beyond!")



# items_on_sale = ["blue_shirt", "striped_socks", "knit_dress",
#  "red_headband"]

## BREAK LOOPS - 
# for item in items_on_sale:
#     if item == "knit_dress":
#         print("Knit Dress is on sale!")
#         break 

# print ("end of search!")

## CONTINUE LOOPS -
# big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# for i in big_number_list:
#     if i < 0:
#         continue
#     print(i)
# # Notes - CONTINUE is basically skipping

# nums = [1, 2, 3, 4, 5, 6, 7]
# for num in nums:    
#     if num%2 == 0:
#         continue
#     print(num)


# # WHILE LOOPS - 
# dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle',
#  'collie']

# index = 0
# while index < len(dog_breeds):
#     print(dog_breeds[index])
#     index += 1


# # NESTED LOOPS - 
# project_teams = [["Ava", "Samantha", "James"], 
# ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
# for team in project_teams:
#     for student in team:
#         print(student)




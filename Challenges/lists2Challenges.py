# https://repl.it/@missionbit/Python-Lists-Challenges-Starter-Code#main.py
#
#    Challenge 1
# def append_sum(lst):
#     list.append([-1] + [-2])
#     list.append([-1] + [-2])
#     list.append([-1] + [-2])
#     return lst
# print(append_sum([1, 1, 2]))

# Challenge 2 
# Key takeaways
# 1. Learned how to traverse a list backwards [-1] that always gets us the last element of any size list
# 2. elifs (can use as many as we need/want)
# def larger_list(lst1, lst2):
#     if len(lst1) == len(lst2):
#         return (lst1)[-1]
#     elif len(lst1) < len(lst2):
#         return lst2[-1]
#     elif len(lst1) > len(lst2):
#         return (lst1)[-1]

# print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
#  --------------------------------
# Challenge 3
#  --------------------------------

# Create a function named more_than_n that has three parameters named lst, item, and n.

# The function should return True if item appears in the list more than n times. The function should return False otherwise.

#Write your function here

# def more_than_n(lst, item, n):
#     if (lst.count(item) > n):
#         return True
#     else:
#         return False


#Uncomment the line below when your function is done
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))



# --------------------------------
# Challenge 5
# --------------------------------

# Write a function named combine_sort that has two parameters named lst1 and lst2.

# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

#Write your function here

# def combine_sort(lst1, lst2):
#     lst3 = lst1 + lst2
#     # "hello" + " world" --> "hello world"
#     # [1, 2] + [3, 4] --> [1, 2, 3, 4]
#     sorted_lst3 = sorted(lst3)
#     # lst3.sort()
#     # return lst3
#     return sorted_lst3


#Uncomment the line below when your function is done
# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
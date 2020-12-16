#  https://repl.it/repls/HandmadeSufficientReentrant
# 
#  Challenge 1
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

# Challenge 3
# def more_than_n(lst, item, n):
#     if lst.count(item) > n:
#         return True
#     else:
#         return False
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Challenge 4
# def append_size(lst):
#     lst.append(len(lst))
#     return lst

# print(append_size([23, 42, 108]))

# Challenge 5
# def combine_sort(lst1, lst2):
#     lst3 = list(zip(lst1, lst2))
#     lst3.sort()
#     return lst3
# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


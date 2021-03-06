# https://repl.it/@missionbit/Python-Dictionaries-Challenges-Starter-Code#main.py

# --------------------
# Challenge 1: Sum Values
# --------------------
# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
# The function should return the sum of the values of the dictionary

# def sum_values(my_dictionary):
#     total = 0
#     for value in my_dictionary.values():
#         total += value
#     return total

# Uncomment these function calls to test your sum_values function:
# print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
# print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

#----------------------------------------------------------
# Challenge 2: Even Keys
#----------------------------------------------------------
# Create a function called sum_even_keys that takes a dictionary named my_dictionary, 
# with all integer keys and values, as a parameter. 
# This function should return the sum of the values of all even keys.

# def sum_even_keys(my_dictionary):
#     even_keys = 0
#     for key in my_dictionary.keys():
#         if key % 2 == 0:
#             even_keys += my_dictionary[key] 
#     return even_keys

# Uncomment these function calls to test your  function:
# print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
#print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#----------------------------------------------------------
# Challenge 3
#----------------------------------------------------------
# Create a function named add_ten that takes a dictionary
# with integer values named my_dictionary as a parameter.
# The function should add 10 to every value in my_dictionary and return my_dictionary

# def add_ten(my_dictionary):
#     for value in my_dictionary:
#         my_dictionary[value] += 10
#     return my_dictionary

# Uncomment these function calls to test your  function:
# print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
# print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#----------------------------------------------------------
# Challenge 4: Values That Are Keys
#----------------------------------------------------------
# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
# This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
    values_equals_keys = []
    for keys in my_dictionary:
        for values in my_dictionary.values():
            if keys == values:
                values_equals_keys.append(values)
    return values_equals_keys

# Uncomment these function calls to test your  function:
# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#----------------------------------------------------------
# Challenge 5: Largest Value
#----------------------------------------------------------

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
# The function should return the key associated with the largest value in the dictionary.

# def max_key(my_dictionary):


#----------------------------------------------------------
# Challenge 6: Word Length Dict
#----------------------------------------------------------

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

# def word_length_dictionary(words):
#     word_length_dictionary = {}
#     for word in words:
#         word_length_dictionary.update({
#             word: len(word)
#         })
#     return word_length_dictionary

# Uncomment these function calls to test your  function:
# print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
# print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
    
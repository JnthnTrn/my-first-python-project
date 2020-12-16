# names = {"tyler", "jacky", "ramiro", "kingsley"}
# print("jacky" in names)

#names[0] makes no sense

#looping through set with a for loop
#for name in names:

#elements in sets cannot be changed

#Changing a list
#names = ["tyler", "jacky", "ramiro", "kingsley"]
# names[2] = "jordan"

#adding new elements to a set: set.add(element), or set.update(1st)
#.add adds only one, whereas update can add multiple

# names.add("jordan")

# names_to_add = ("andrew", "jonathan", "george")

# names.update(names_to_add)

#removing items from a set

# names.remove("kingsley")

# names.remove("andrew") #gives us an error
# name.discard("andrew") #does nothing even though it doesn't exist

# names.clear()

#set unions

# names1 = {"tyler", "jacky", "ryan", "ramiro", "kingsley"}
# names2 = {"tyler", "jacky", "andrew", "george", "angelo"}

# names_union = names1.union(names2)
# names_intersection = names1.intersection(names2)

# print(names_union)
# print(names_intersection)
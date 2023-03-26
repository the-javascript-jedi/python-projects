# """Set are similar to lists but are unordered and cannot contain duplications - Use curly brackets"""
# my_set={
#     1,2,3,4,5,1,2
# }
# # duplicate elements are removed
# print('my_set',my_set)
# # length of the set - will not show duplicate lements
# print('len(my_set)',len(my_set))
# # print all elements in the set
# for x in my_set:
#     print('x',x)
# # remove element from set
# my_set.discard(3)
# print('my_set.discard(3)',my_set)
# # remove all elements from set
# print('my_set.clear()',my_set.clear())
# print('my_set',my_set)
# # add value to set
# my_set.add(6)
# print('my_set.add(6)',my_set)
# # add multiple values to set
# my_set.update([7,8])
# print('my_set.update([7,8])',my_set)
#
# # Tuples in Python
# #  tuples cannot be added or updated - it does not support assignment
# my_tuple=(1,2,3,4,5)
# print('my_tuple',my_tuple)
# # length of tuple
# print('len(my_tuple)',len(my_tuple))
# # call specific index of tuple
# print('my_tuple[1]',my_tuple[1])

# Lists Assignment
animals_list=['lion','tiger','buffalo','rhino','hippo','giraffe','zebra']
# Delete the animal at the 3rd index.
animals_list.pop(3)
# Append a new animal at the end of the list
animals_list.append
# Delete the animal at the beginning of the list.
animals_list.pop(0)
# Print all the animals
for x in animals_list:
    print('x',x)
# Print only the first 3 animals
print('x',animals_list[0:3])
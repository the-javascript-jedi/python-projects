"""
Lists are a collection of data
"""
# people_list=["Eric","Adil","Jeff"]
# print("people_list",people_list)
# # print first element
# print("people_list[0]",people_list[0])
#
# # print last element
# print("people_list[-1]",people_list[-1])
#
# #Print 0,1 and stop at 2 index without printing 2 index
# print("people_list[0:2]",people_list[0:2])

my_list=[80,96,72,100,8]
# append in the last
my_list.append(1000)
print('my_list',my_list)
# insert in the index position
my_list.insert(2,2000)
print('my_list',my_list)
# remove the first occurence specified item from the list
my_list.remove(1000)
print('my_list',my_list)
# remove the specified index element
my_list.pop(0)
print('my_list',my_list)
# sort the elements
my_list.sort()
print('my_list',my_list)


# map example
# my_list=[1,2,3]
# def multiply_by2(item):
#     return item*2
# print(list(map(multiply_by2,my_list)))
# print(my_list)
# filter
# my_list=[1,2,3]
#
# def only_odd(item):
#     return item%2!=0
#
# print("list(filter(only_odd,my_list))",list(filter(only_odd,my_list)))
# print("my_list",my_list)

# zip
# my_list = [1, 2, 3]
# your_list=[10,20,30]
# print(list(zip(my_list,your_list)))


# reduce
# from functools import reduce
# my_list=[1,2,3]
# def accumulator(acc,item):
#     print(acc,item)
#     return acc+item
#
# print(reduce(accumulator,my_list,0))

# # lambda expressions - map
# my_list=[1,2,3]
# print(list(map(lambda item:item*2,my_list)))

# # lambda expressions - filter
my_list=[1,2,3]
print(list(filter(lambda item:item%2,my_list)))
print(my_list)

# # lambda expressions - reduce
# from functools import reduce
# my_list=[1,2,3]
# def accumulator(acc,item):
#     print(acc,item)
#     return acc+item
#
# print(reduce(lambda acc,item:acc+item,my_list))
# print(my_list)


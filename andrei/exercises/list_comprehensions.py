# normal list
my_list=[]
for char in 'hello':
    my_list.append(char)
print("my_list",my_list)

# list comprehension
my_list=[char for char in 'hello']
print("my_list",my_list)

# create a list containing 100 values
my_list2=[num for num in range(0,100)]
print("my_list2",my_list2)

# create a list containing 100 values with the numbers multiplied by 2
my_list3=[num*2 for num in range(0,100)]
print("my_list3",my_list3)

# create a list with only even values whch are squared values
my_list4=[num**2 for num in range(0,100) if num%2==0]
print("my_list4",my_list4)
# # set comprehension
my_list={char for char in 'hello'}
print("my_list",my_list)

# create a set containing 100 values
my_list2={num for num in range(0,100)}
print("my_list2",my_list2)

# create a set containing 100 values with the numbers multiplied by 2
my_list3={num*2 for num in range(0,100)}
print("my_list3",my_list3)

# create a set with only even values whch are squared values
my_list4={num**2 for num in range(0,100) if num%2==0}
print("my_list4",my_list4)

# multiply a dictionary with a key and value pair and square the value
simple_dict={
    'a':1,
    'b':2
}
my_dict={key:value**2 for key,value in simple_dict.items()}
print("my_dict",my_dict)

# multiply a dictionary with a key and value pair and square the value only if it is even
my_dict2={key:value**2 for key,value in simple_dict.items() if value%2==0}
print("my_dict2",my_dict2)

# create a dictionary such that key is the item and the value is the squared list item of the dictionary
my_dict3=[1,2,3]
#  my solution
customObj={}
for num in my_dict3:
    customObj[num]=num*num
print("customObj",customObj)

# andrei solution
my_dict4={num:num*2 for num in [1,2,3]}
print("my_dict4",my_dict4)

# exercise solution
# remove duplicates
some_list=['a','b','c','b','d','m','n','n']
duplicates=list(set([x for x in some_list if some_list.count(x)>1]))
print("duplicates",duplicates)
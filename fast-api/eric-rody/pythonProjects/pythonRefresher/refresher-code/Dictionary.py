"""Dictionaries"""
user_dictionary={
    'username':'codingwithroby',
    'name':'Eric',
    'age':32
}
# get single key value
print("user_dictionary.get('username')",user_dictionary.get('username'))
# add value to dictionary
user_dictionary['married']=True
# get length of keys in user dictionary
print("len(user_dictionary)",len(user_dictionary))

# print elements in dictionary
for x,y in user_dictionary.items():
    print('x,y',x,y)
# # remove key value from dictionary
# user_dictionary.pop("age")

# copy a dictionary
user_dictionary2=user_dictionary.copy()
# remove key value from copied dictionary
user_dictionary2.pop("age")

# display dictionaries
print('user_dictionary',user_dictionary)
#  since we used copy function and did not do equals assignment
#  only the user_dictionary2.age key value data is deleted,
# the original data is not modifed
print('user_dictionary2',user_dictionary2)


# # clear values in user dictionary
# user_dictionary.clear()
# # delete dictionary
# del user_dictionary


# Dictionary Assignment
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
# Create a for loop to print all keys and values
for x,y in my_vehicle.items():
    print('x,y',x,y)
# Create a new variable vehicle2, which is a copy of my_vehicle
vehicle2=my_vehicle.copy()
# Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
vehicle2['number_of_tires']=4
# Delete the mileage key and value from vehicle2
vehicle2.pop("mileage")
# Print just the keys from vehicle2
for key in vehicle2:
    print('key',key)
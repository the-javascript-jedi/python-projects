# print loop using generators - intermediate loop will not consume memory
def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(1000):
    print("item using generator",item)

# print loop using for loop - will consume memory
def make_list(num):
    result=[]
    for i in range(num):
        result.append(i*2)
    return result

my_list=make_list(100)
print("my_list using for loop",my_list)
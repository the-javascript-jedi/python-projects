my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(len(my_list))
x=0
while x<3:
    x+=1
    for i in my_list:
        if i == 'Monday':
            print("------")
            continue
        print(i)

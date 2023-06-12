# ns method
def highest_even_ns(li):
    li.sort(reverse=True)
    for x in li:
        if(x%2==0):
            return x
            break
print("ns",highest_even_ns([10,2,3,4,8,11]))

# andrei method
def highest_even_andrei(li):
    evens=[]
    for item in li:
        if item%2==0:
            evens.append(item)
    return max(evens)


print("andrei",highest_even_andrei([10,2,3,4,8,11]))
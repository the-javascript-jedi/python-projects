# run the below code in terminal
#  python <filename>.py

my_file=open('test.txt')
print(":",my_file.read())
# after file read operation cursor will remain at end so to read again we need to reset the cursor
my_file.seek(0)
print(":",my_file.read())
my_file.seek(0)
print(":",my_file.read())
my_file.seek(0)

# readlines
print(my_file.readlines())
# close file after opening
my_file.close()

## open file amd write
## mode='a' - append; mode='r' - read; mode='w' -write
# with open('happy.txt',mode='a') as my_file:
#     text=my_file.write(":)")
#     print(text)

# Handling Exceptions
try:
    with open('updated.txt',mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err
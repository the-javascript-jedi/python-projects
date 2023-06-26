from random import randint
# generate a number 1 ~ 10
answer =randint(1,10)
print("answer",answer)
# check that input is a number 1~10
while True:
    try:
        # input from user
        guess = int(input('guess a number 1~10:  '))
        # check if number is right guess. Otherwise ask again
        #  if 0 < int(guess)>11: -- simplified if loop
        if guess>0 and guess<11:
            if guess==answer:
               print('you are a genius')
               break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')

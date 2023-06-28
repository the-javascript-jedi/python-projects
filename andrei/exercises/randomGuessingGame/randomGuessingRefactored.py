import random

def run_guess(guess, answer):
    if 0 < int(guess) < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False
# if we dont do this check even this block of code will be run even for unit tests
if __name__ == '__randomGuessingRefactored__':
    answer = random.randint(1, 10)
    print("answer",answer)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
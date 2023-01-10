from random import randint
from time import sleep

answer = randint(1,100)

username = input("Hi, what is your name? >>")
print("Hi, {}! Please be my guest".format(username))

guess = int(input("Just guess the number between 1 and 100 ! >>"))

print("So, you picked {}, the answer was {}".format(guess, answer))

#Comepare answer with user's guess
if guess == answer:
    print('********************')
    sleep(1)
    print('********************')
    sleep(1)
    print('********************')
    sleep(1)
    print(f'You got it right!! The answer is {answer}!!')
elif guess > answer:
    print(f'Keep going, man~! Too high, {username}..')
elif guess < answer:
    print(f'Keep going, man~! Too Low, {username}..')
else:
    print("Wrong answer!")

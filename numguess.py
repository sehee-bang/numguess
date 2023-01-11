from random import randint
from time import sleep

#getting random answer
answer = randint(1,100)

#getting user name
username = input("Hi, what is your name? >>")
print("Hi, {}! Please be my guest".format(username))
print("You can do this game just three times~")

#guessing function
def guessing():
    guess = int(input("Just guess the number between 1 and 100 ! >>"))

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

#doing recursive
i=0
for i in range(3):
    guessing()
    i+=1
    if i==3:
        print("The game is over~")

from random import randint

answer = randint(1,100)

username = input("Hi, what is your name? >>")
print("Hi, {}! Please be my guest".format(username))

guess = int(input("Just guess the number between 1 and 100 ! >>"))

print("So, you picked {}, the answer was {}".format(guess, answer))
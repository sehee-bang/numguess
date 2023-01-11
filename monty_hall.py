#Monty Hall Problem 
from random import shuffle, choice


doors=[0,0,1] #0: goat, 1:sportscar
result = {'stay_to_win' : 0, 'move_to_win' : 0}
iter_num = int(input("Enter some num(100-10000): "))

for _ in range(iter_num):
    shuffle(doors)
    user_choice=choice(doors)

    if user_choice == 0:
        result['move_to_win'] += 1
    else:
        result['stay_to_win'] += 1

    
print("{} times run : stay-{stay_to_win} switch-{move-to-win}".format(iter_num, **result))

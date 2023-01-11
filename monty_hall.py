#Monty Hall Problem 
from random import shuffle, choice

doors=[0,0,1]
result_list=[]

for i in range(1,100+1):
    shuffle(doors)
    result=choice(doors)
    result_list.append(result)

sportscar=result_list.count(1)
sheep=result_list.count(0)

sportscar_aval=sportscar/100
sheep_aval=sheep/100

print('스포츠를 선택할 확률은 !', end=' ')
print(sportscar_aval)
print('양을 선택할 확률은 !', end=' ')
print(sheep_aval)

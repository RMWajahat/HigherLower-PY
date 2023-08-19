# import fundamentals
from higher_lower_data import data
from random import choice
from higher_lower_art import logo,vs,SScore
from os import system


score=0
GAME_OVER=False
print("\t\t",logo)
A_object=choice(data)
B_object=choice(data)


def play():
    global score
    global A_object
    global B_object
    Choice=str(input(f'Who has more followers ?\nA : Name : {A_object["name"]}\n    Country : {A_object["country"]}\n    Description : {A_object["description"]}\n\n{vs}\n\nB : Name : {B_object["name"]}\n    Country : {B_object["country"]}\n    Description : {B_object["description"]}\n\nChoice: ')[0].upper())
   
    
    if Choice=="A" and (int(A_object["follower_count"])>int(B_object["follower_count"])):
        B_object=choice(data)
        score+=1
        print(f"Your are right {A_object['name']} has most followers")
    elif Choice=="B" and (int(A_object["follower_count"])<int(B_object["follower_count"])):
        A_object=choice(data)
        score+=1
        print(f"Your are right {B_object['name']} has most followers")
    else:
        global GAME_OVER
        GAME_OVER=True
        print("Un-Fortunately Wrong Answer😰")
        print("\n\tYOU MADE IT WELL")


while not GAME_OVER:
    system("pause")
    system("cls")
    play()
print(SScore,"        :   ",score)
system("pause")

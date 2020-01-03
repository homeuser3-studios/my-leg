# mY leG
# (c) Homeuser3 Studios 2020

import random

myleg = ["You jumped off a building and landed on your feet. 'MY LEG!'", "Someone drove over your leg. 'MY LEG!'", "You were in your car and you got a headon collision. Your leg went down too far... 'MY LEG!'", "You were in a shark cage and your feet went through one of the squares for a second. 'MY LEG!'"]

myhead = ["You were staring at the ground while running and you hit your head on the wall. 'MY HEAD!'", "You were jumping off a very high diving board into a pool and went head first into the shallow area. 'MY HEAD!'", "You were on a beach and were right on the cliff in the ocean where the water gets very deep. You dived into the cliff and accidentally hit the bottom. 'MY HEAD!'"]

print("Welcome to MY LEG!")
print("(c) Homeuser3 Studios 2020")
print("Check the file named 'cmdhelp' for help. Now, get started!")

while 1:

    choice = input("Please insert a command here: ")

    if choice.lower() == "leg":
        print(f'{random.choice(myleg)}')
    elif choice.lower() == "head":
        print(f'{random.choice(myhead)}')
    else:
        print('INVALID COMMAND.')

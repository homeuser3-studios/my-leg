# mY leG
# (c) Homeuser3 Studios 2020

import random

numbers = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

myleg = ["You jumped off a building and landed on your feet. 'MY LEG!'", "Someone drove over your leg. 'MY LEG!'", "You were in your car and you got a headon collision. Your leg went down too far... 'MY LEG!'", "You were in a shark cage and your feet went through one of the squares for a second. 'MY LEG!'", "A bull ran right at you and flipped you, and then you landed standing up. 'MY LEG!'", "You were walking past a dog who's nails hadn't been cut in 2 years, and then they scratched your leg. 'MY LEG!'", "You tripped and fell. Your legs got stuck in wet cement. 'MY LEG!'", "People threw tomatoes at you, and they hit your legs, knocking you on the ground and then tomatoes rained on your legs. 'MY LEG!'"]

myhead = ["You were staring at the ground while running and you hit your head on the wall. 'MY HEAD!'", "You were jumping off a very high diving board into a pool and went head first into the shallow area. 'MY HEAD!'", "You were on a beach and were right on the cliff in the ocean where the water gets very deep. You dived into the cliff and accidentally hit the bottom. 'MY HEAD!'", "Someone slammed a pot on your head. 'MY HEAD!'", "A UFO came and crashed on your head. 'MY HEAD!'", "Your head was the Earth and a meteor struck it. 'MY HEAD!'", "You poked your face with a knife. 'MY HEAD!'"]

easteregg = ["Darryl told you to go away from the baler, but you still played with it and you had some... serious limb damage. 'WOW THAT WAS A VERY NICE THE OFFICE (US) REFERENCE BUT EVERYTHING STILL HURTS!'", "The nuke had to hit you. 'OH NO I'M A BIG RADIOACTIVE MONSTER NOW! AND EVERYTHING HURTS!'"]

print("Welcome to MY LEG!")
print("(c) Homeuser3 Studios 2020")
print("Check the file named 'cmdhelp' for help. Now, get started!")

print("Notice: Some of the text may be inappropriate for children under the age of 13. Use this program at your own risk.")

while 1:

    choice = input("Please insert a command here: ")

    randomnumber = f"{random.choice(numbers)}"

    if randomnumber == "7":
        print(f'{random.choice(easteregg)}')
        print('\nNow time for what you asked...\n')
        
    if choice.lower() == "leg":
        print(f'{random.choice(myleg)}')
    elif choice.lower() == "head":
        print(f'{random.choice(myhead)}')
    else:
        print('INVALID COMMAND.')

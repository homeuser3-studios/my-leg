# my leg shell

import random
import myleg

print(" __\n|__|\n|__|")
print("The 8 is so pretty... 'Watch out!' MY LEG!!")
print("(c) Homeuser3 Studios 2020")

while 1:

    choice = input("MY LEG! >> ")

    if choice != "help":
        randomnumber = f"{random.choice(myleg.numbers)}"

        if randomnumber == "7":
            print(f'{random.choice(myleg.easteregg)}')
            print('\nNow time for what you asked...\n')
        
    if choice.lower() == "leg":
        print(f'{random.choice(myleg.myleg)}')
    elif choice.lower() == "head":
        print(f'{random.choice(myleg.myhead)}')
    elif choice.lower() == "help":
        print('HELP MENU')
        print('leg - Shows a random thing that can make your leg hurt.')
        print('head - Shows a random thing that can make your head hurt.')
        print('help - Shows this menu!')
    else:
        print('That is a invalid command. Do "help" for help.')

# What can we do to make Mozzarella happy

import random

funStuff = [
# Rainy Day
    ["Pet store", "Smell game", "Hide and seek"],
# Cold Day
    ["Hiking trip", "Dog park", "Long walk", "Off lead", "Frisbee"],
# Nice Day
    ["Go downtown", "Swiming", "Soccer"]
]

activity = []

tricks = [
    "Sit", "Sit pretty", "Down", "Stand", "Jump up",
    "Turn", "Paw", "Bow", "Back", "Stay",
    "Wait", "Hold", "Under/Over", "Crawl"
]

def motziHobby():
    answer = input("What are we doing with Mozzarella? (train, regular)\n\n")
    if answer == "train":
        print("\n" + str(tricks[random.randint(0, (len(tricks)-1))]) + "\n")
        motziHobby()
    elif answer == "regular":
        def condition():
            weather = input("\nHow is the weather outside? (rainy, cold, nice, <- back)\n\n")
            if weather == "rainy":
                activity = (funStuff[0])
                print("\n" + activity[random.randint(0, (len(activity)-1))])
                condition()
            elif weather == "cold":
                activity = (funStuff[0] + funStuff[1])
                print("\n" + activity[random.randint(0, (len(activity)-1))])
                condition()
            elif weather == "nice":
                activity = (funStuff[0] + funStuff[1] + funStuff[2])
                print("\n" + activity[random.randint(0, (len(activity)-1))])
                condition()
            elif weather == "back":
                print("\nwell okay :/\n")
                motziHobby()
            else:
                print("\nError: Please enter a valid weather type.")
                condition()
        condition()
    else:
        print("\nError: Please enter a valid action.\n")
    motziHobby()
motziHobby()

def displayIntro():
    print("Welcome to DoomsVille adventure game!")
    print("There are 6 doors for you to explore")
    print("All doors are filled with completely different things")
    print("Only way to find out is by entering the rooms")
displayIntro()

def answer_input(statement,input_q,a,b,output_string_a,output_string_b):
    print(statement)
    print()
    answer = input(input_q)
    if answer == a:
        print(output_string_a)

    elif answer == b:
        print(output_string_b)

    else:
        print('invalid, you die!')

answer_input('hello',"Are you ready to start? [yes/no]",'yes','no','goodbye','Lets play, choose a door')

print()
thislist = ["1", "2", "3", "4", "5", "6"]
print(thislist)
answer = input("Which door shall it be, choose?")

if answer == "1":
    answer_input("an animal comes towards you","fight the animal or run away? [fight/run]","fight","run"," the lion has teared you apart! you die!","you have ran away from he animal, your alive!")

elif answer == "3":
    answer_input("you are now in room full of water","hold your breathe or try to swim? [hold/swim]","hold","swim","you have drowned, you die!","you have drowned, you die!")
  
if answer == "4":
    message = "you have won the game, yay"
    print(message)
    breakpoint
    
if answer == "2":
    answer_input("the room is filled of gold and money"," keep it all or leave it? [keep/leave]", "keep","leave","the phantom ghost has woke up and killed you!","you can choose another door, your alive!")

elif answer == "5":
    answer_input("a stranger appear holding a knife coming at you","fight the stranger or try to calm? [fight/speak]","fight","speak","he has killed you! you die!"," you have been killed, you die!")
    
if answer == "6":
    answer_input("the room starts shaking"," attempt to leave the room or stay put and hope for the best? [leave/stay]", "leave","stay"," you were killed by the falling ceiling","You are now lost in space, unlucky!")

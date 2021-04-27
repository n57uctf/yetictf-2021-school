from random import choice
from select import select
from sys import stdin
from termcolor import colored

#if anyone read this govnocode - i'm really sorry.

round = 1
#count_loose = 0
 
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4

def number_to_name(number):     
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'


def main(user_choice, round): 

    user = name_to_number(user_choice)
    computer = choice([0,2,4]) if round < 100 else choice([0,1,2,3,4])
    comp_choice = number_to_name(computer);
    diff = (computer - user) % 5
    if( diff == 1 or diff == 2 ):
        return ["Computer wins!", comp_choice]
    elif ( diff == 4 or diff == 3 ):
        return ["Player wins!", comp_choice]
    elif( diff == 0 ):
        return ["Player and computer tie!", comp_choice]

print(colored("Hello! Welcome to the game RockPaperScissors!\n", "yellow"))


while round < 201:

    print(colored(f"Round {round}/200", "blue"))
#    print(colored(f"Number of losses {count_loose}/50", "blue"))

    if round == 100:
        print(colored("\n\nToo easy... Maybe we add a lizard and spock? :)\n\n", 'yellow'))
#    if count_loose == 50:
#        print(colored("\nTo many loose... Bye Bye", 'red'))
#        exit()

    if round < 100:
        print(colored("\nRock/Paper/Scissors?", 'magenta'))
        i, o, e = select( [stdin], [], [], 5)
        if len(i) == 0:
            print(colored('\n\nTime is up! Too slowly!', 'red'))
            raise Exception()
        rev = stdin.readline().strip().rstrip()
        if rev.lower() not in ['rock', 'paper', 'scissors']:
            print(colored("\nHmmm, i don't understand you... Bye bye.", 'red'))
            exit()

    else:
        print(colored("Rock/Paper/Scissors/Lizard/Spock?", 'magenta'))
        i, o, e = select( [stdin], [], [], 5)
        if len(i) == 0:
            print(colored('\n\nTime is up! Too slowly!', 'red'))
            exit()
        rev = stdin.readline().strip().rstrip()
        if rev.lower() not in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
            print(colored("\nHmmm, i don't understand you... Bye bye.", 'red'))
            exit()
        
    result = main(rev.lower(), round)
#    round += 1
    if result[0] == "Player wins!":
        round += 1

    print(f"\nYou choice: {rev}")
    print(f"Computer choice: {result[1]}")
    print(colored(f"\n{result[0]}\n", 'green'))

print("yetiCTF{do_you_like_lizard_spock_version?}")

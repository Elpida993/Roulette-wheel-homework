import random
import os

class NumColor:
	number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']
	color = ['red', 'black']

w1 = NumColor()

def once():
    random_num = random.choice(w1.number)
    random_color = random.choice(w1.color)
    user = input("pick a number or color:")
    print(random_num, random_color)
           
    if user == random_color:
        print("you won")
        
    elif user == random_num:
        print("you won")

    else:
        print("you lost")

def main():
    wins = 0
    losses = 0
    

    while wins >= 0:
        while losses >= 0:
            random_num = random.choice(w1.number)
            random_color = random.choice(w1.color)
            user = input("pick a number or color:")
            os.system("cls")
            print(random_num, random_color)
           
            if user == random_color:
                wins += 1
                print("you won", wins, "times")
                print(wins,"/",losses)
                try:
                    print("percentage", wins/losses, "\n\n")
                except ZeroDivisionError:
                    print("percentage over 100%") 
                                
            elif user == random_num:
                wins += 1
                print("you won", wins, "times")
                print(wins)
                print(wins,"/",losses)
                try:
                    print("percentage", wins/losses, "\n\n")
                except ZeroDivisionError:
                    print("percentage over 100%")
                
            else:
                losses += 1
                print("you lost", losses, "times")
                print(wins,"/",losses) 
                try:
                    print("percentage", wins/losses, "\n\n")
                except ZeroDivisionError:
                    print("percentage over 100%")
                
        else:
            print("while loss ended")
    else:
        print("while wins ended")

first = input("play multiple times? [y/n]:")
if first == 'y':
    main()
if first == 'n':
    once()
else:
    print("enter a valid option")
    first()

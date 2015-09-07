#!/usr/bin/python2.7
__author__ = 'Louvie'


import random
import time


rock, paper, scissors = 1, 2, 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():
    print "Let's play Rock, Paper, Scissors!"
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print
        player = raw_input("Rock = 1 \nPaper = 2\nScissors = 3\n")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass

        print "Invalid entry! Enter 1, 2, or 3."

def result(player, computer):
    print "1..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "3!"
    time.sleep(0.5)

    global player_score, computer_score

    print("The computer threw {0}. You threw {1}.".format(names[computer], names[player]))
    if player == computer:
        print "It's a TIE!"

    elif computer == rules[player]:
        print "You are victorious!"
        player_score += 1

    else:
        print "You are no match the the computer's superior intellect!"
        computer_score += 1



def play_again():
    ans = raw_input("Do you want to play again? (Y/N)")
    if ans in ("y", "Y", "Yes"):
        return True
    else:
        print "Thanks for playing!"


def scores():
    global player_score, computer_score
    print "Here is the scoring!"
    print "Player: ", player_score
    print "Computer: ", computer_score


if __name__ == '__main__':
    start()

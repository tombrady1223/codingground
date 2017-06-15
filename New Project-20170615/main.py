# "Rock, Paper, Scissors" demo for Python 2.x
# by Dan Kamins

import random

ROCK = 1
PAPER = 2
SCISSORS = 3

NAMES = { ROCK: 'Rock', PAPER: 'Paper', SCISSORS: 'Scissors' }
WHAT_BEATS_WHAT = { ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER }
WIN_ACTIONS = { ROCK: 'crushes', PAPER: 'smothers', SCISSORS: 'cuts' }

score_player = 0
score_computer = 0
score_ties = 0

def main():
    intro()
    while main_loop():
        pass
    summary()

def intro():
    print "Welcome to Rock, Paper, Scissors!"

def main_loop():
    player = get_player_input()
    computer = random.randint(1, 3)
    check_result(player, computer)
    return ask_play_again()

def check_result(player, computer):
    global score_player, score_computer, score_ties
    if player == computer:
        print "Tie!  Computer also chose {0}.".format(NAMES[computer])
        score_ties += 1
    else:
        if WHAT_BEATS_WHAT[player] == computer:
            print "Your massive {0} {1} the computer's {2}!".format(
                NAMES[player], WIN_ACTIONS[player], NAMES[computer])
            score_player += 1
        else:
            print "The computer's {0} {1} your pathetic {2}!".format(
                NAMES[computer], WIN_ACTIONS[computer], NAMES[player])
            score_computer += 1

def ask_play_again():
    again = raw_input("Enter Y to play again: ")
    return again in ('y', 'Y')

def get_player_input():
    while True:
        print
        player = raw_input("Enter 1 for Rock 2 for paper or 3 for Scissors: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "Please enter a number from 1 to 3."

def summary():
    global score_player, score_computer, score_ties
    print "Thanks for playing."
    print "Player won: ", score_player
    print "Computer won: ", score_computer
    print "Ties: ", score_ties

if __name__ == '__main__':
    main()
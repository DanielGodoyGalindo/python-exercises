"""
Rock, Paper, Scissors
Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

The input strings will always be "Rock", "Paper", or "Scissors".
"Rock" beats "Scissors".
"Paper" beats "Rock".
"Scissors" beats "Paper".
Return:

"Player 1 wins" if Player 1 wins.
"Player 2 wins" if Player 2 wins.
"Tie" if both players choose the same option.

1. rock_paper_scissors("Rock", "Rock") should return "Tie".
2. rock_paper_scissors("Rock", "Paper") should return "Player 2 wins".
3. rock_paper_scissors("Scissors", "Paper") should return "Player 1 wins".
"""


def rock_paper_scissors(player1, player2):
    r, p, s = "Rock", "Paper", "Scissors"
    p1, p2 = player1, player2
    if (p1 == r and p2 == s) or (p1 == p and p2 == r) or (p1 == s and p2 == p):
        return "Player 1 wins"
    elif (p2 == r and p1 == s) or (p2 == p and p1 == r) or (p2 == s and p1 == p):
         return "Player 2 wins"
    else:
        return "Tie"

print(rock_paper_scissors("Rock", "Paper"))
"""
Input Format:- A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A-Z].
Output Format:- Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
"""

"""
BANANA
"""


def minion_game(string):
    # your code goes here
    k = 0
    s = 0
    vowels = "AaEeIiOoUu"
    for i in range(len(string)):
        if string[i] in vowels:
            k = k + len(string) - i
        else:
            s = s + len(string) - i

    if k > s:
        print("Kevin", k)
    elif k == s:
        print("Draw")
    else:
        print("Stuart", s)


if __name__ == '__main__':
    s = input()
    minion_game(s)
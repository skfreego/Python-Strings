"""
Task:- You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
Input Format:- A single line containing a string S.
Output Format:-
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""

"""
qA2
"""


def pr(t):
    if t == 1:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    s = input()
    t = 0
    for i in s:
        if i.isalnum() == True:
            t = 1
            break
    pr(t)

    t = 0
    for i in s:
        if i.isalpha() == True:
            t = 1
            break
    pr(t)

    t = 0
    for i in s:
        if i.isdigit() == True:
            t = 1
            break
    pr(t)

    t = 0
    for i in s:
        if i.islower() == True:
            t = 1
            break
    pr(t)

    t = 0
    for i in s:
        if i.isupper() == True:
            t = 1
            break
    pr(t)
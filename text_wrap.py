"""
task:- Your task is to wrap the string into a paragraph of width w.
Input Format:-
The first line contains a string, S.
The second line contains the width, w.
Output Format:- Print the text wrapped paragraph.
"""

"""
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
"""

import textwrap

def wrap(string, max_width):
    return textwrap.TextWrapper(width=max_width).fill(text=string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
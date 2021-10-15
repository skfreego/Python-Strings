"""
Task:- You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Input Format:- The first line contains a string consisting of space separated words.
Output Format:- Print the formatted string as explained above.
"""

"""
this is a string   
"""

def split_and_join(line):
    # write your code here
    line=line.split(" ")
    return ('-'.join(line))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
"""
Task:- You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
Input Format:- The first line of input contains the original string. The next line contains the substring.
Output Format:- Output the integer number indicating the total number of occurrences of the substring in the original string.
"""

"""
ABCDCDC
CDC
"""


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        for j in range(len(sub_string)):
            if string[i + j] == sub_string[j] and j == (len(sub_string) - 1):
                count = count + 1
            if string[i + j] != sub_string[j]:
                break
        if i == len(string) - len(sub_string):
            break
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
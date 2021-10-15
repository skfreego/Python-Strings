"""
Input Format:- A single line of input containing the full name, S.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
Output Format:- Print the capitalized string, S.
"""

"""
chris alan
"""

import math
import os
import random
import re
import sys

# Complete the solve function below.

def solve(s):
    result = []
    name = re.split(r'(\s+)', s)

    for i in range(len(name)):
        result.append(str(name[i]).capitalize())

    return ''.join(str(ele) for ele in result)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    s = 'chris alan'
    result = solve(s)

    #fptr.write(result + '\n')
    print(result + '\n')
    #fptr.close()

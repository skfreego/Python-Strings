"""
Input Format:- A single integer denoting n.
Output Format:- Print n lines where each line i (in the range 1<=i<=n) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i.
 Each printed value must be formatted to the width of the binary value of n.
"""

"""
17
"""

def print_formatted(number):
    # your code goes here
    Length = len(bin(number)[2:]) # To control the spaces
    for i in range(1 , number + 1):
        print(str(i).rjust(Length , ' ') , end = " ")
        print(oct(i)[2:].rjust(Length,' ') , end = " ")
        print(((hex(i)[2:]).upper()).rjust(Length , ' ') , end = " ")
        print(bin(i)[2:].rjust(Length , ' ') , end = " ")
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
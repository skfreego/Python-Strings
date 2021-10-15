"""
Input Format:- Only one line of input containing N, the size of the rangoli.
Output Format:- Print the alphabet rangoli in the format explained above.
"""

"""
5
"""


def print_rangoli(size):
    Breadth = size * 4 - 3
    String = ''
    for i in range(1, size + 1):
        for j in range(0, i):
            String = String + chr(96 + size - j)
            if len(String) < Breadth:
                String = String + '-'
        for k in range(i - 1, 0, -1):
            String = String + chr(97 + size - k)
            if len(String) < Breadth:
                String = String + '-'
        print(String.center(Breadth, '-'))
        String = ''
    for i in range(size - 1, 0, -1):
        String = ''
        for j in range(0, i):
            String = String + chr(96 + size - j)
            if len(String) < Breadth:
                String = String + '-'
        for k in range(i - 1, 0, -1):
            String = String + chr(97 + size - k)
            if len(String) < Breadth:
                String = String + '-'
        print(String.center(Breadth, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
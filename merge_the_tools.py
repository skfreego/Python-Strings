"""
Input Format:- The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.
Output Format:- Print n/k lines where each line i contains string ui.
"""
"""
    AABCAAADA
    3
"""

def merge_the_tools(string, k):
    # your code goes here
    split_string=(string[i:i+k] for i in range(0,len(string),k))
    for i in split_string:
        u=[]
        u.append(i[0])
        for j in range(1,len(i)):
            if i[j] in u:
                continue
            else:
                u.append(i[j])

        print(''.join(str(e) for e in u))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
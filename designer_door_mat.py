"""
Input Format:- A single line containing the space separated values of M and N.
Output Format:- Output the design pattern.
"""

"""
7 21
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
c='|'
v='.'

n=int(n)
m=int(m)
j=n//2-1
for i in range(n):
    if i==n//2:
        print('WELCOME'.center(m,'-'))
    else:
        if i<n/2:
            print(((v+c+v)*(2*i+1)).center(m,'-'))
        else:
            print(((v+c+v)*(2*j+1)).center(m,'-'))
            j=j-1

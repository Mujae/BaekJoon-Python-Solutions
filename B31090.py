import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    s = n%100
    if s==0:
        print('Bye')
    else:
        if (n+1)%s==0:
            print('Good')
        else:
            print('Bye')

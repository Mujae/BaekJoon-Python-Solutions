import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = input().rstrip()

if n==k:
    print(s[::-1])
elif k==1:
    print(s)
else:
    if n%2==0:
        for i in range(k,n+1):
            print(s[i-1],end="")
        if k%2==0:
            print(''.join(s[k-2::-1]))
        else:
            print(''.join(s[:k-1]))    
    else:
        for i in range(k,n+1):
            print(s[i-1],end="")
        if k%2==0:
            print(''.join(s[:k-1]))
        else:
            print(''.join(s[k-2::-1]))
    
        
    
